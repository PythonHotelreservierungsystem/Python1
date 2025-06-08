import model
from datetime import date
from data_access.base_data_access import BaseDataAccess

class InvoiceDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_invoice(self, issue_date: date, total_amount: float, booking_id: model.Booking
                       ) -> model.Invoice:
        if issue_date is None:
            raise ValueError("issue_date cannot be None")
        if total_amount is None:
            raise ValueError("total_amount cannot be None")

        sql ="""
        INSERT INTO Invoice(Issue_Date, Total_Amount, Booking_Id)
        VALUES (?, ?, ?)"""

        params =tuple([issue_date, total_amount, booking_id])
        last_row_id, row_count = self.execute(sql, params)

        return model.Invoice(
            invoice_id=last_row_id,
            issue_date=issue_date,
            total_amount=total_amount,
            booking=booking_id

        )