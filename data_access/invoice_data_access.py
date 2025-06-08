import model
from datetime import date
from data_access.base_data_access import BaseDataAccess

class InvoiceDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_invoice(self, issue_date: date, total_amount: float, booking_id: int) -> model.Invoice:
        if issue_date is None:
            raise ValueError("issue_date cannot be None")
        if total_amount is None:
            raise ValueError("total_amount cannot be None")
        if booking_id is None:
            raise ValueError("booking_id cannot be None")

        sql = """
              INSERT INTO Invoice(Issue_Date, Total_Amount, Booking_Id)
              VALUES (?, ?, ?) \
              """

        params = (issue_date, total_amount, booking_id)
        last_row_id, row_count = self.execute(sql, params)

        return model.Invoice(
            invoice_id=last_row_id,
            issue_date=issue_date,
            total_amount=total_amount,
            booking=booking_id
        )
    #User Story 5
    def delete_invoice(self, invoice_id: int):
        if invoice_id is None:
            raise ValueError("invoice_id cannot be None")
        sql = """DELETE FROM Invoice WHERE Invoice_Id = ?"""
        params = tuple([invoice_id])
        _,row_count = self.execute(sql, params)
        return row_count > 0
    #User Story 5/6
    def delete_invoice_by_booking_id(self, booking_id: int):
        if booking_id is None:
            raise ValueError("booking_id cannot be None")
        sql = """DELETE FROM Invoice WHERE Booking_Id = ?"""
        params = tuple([booking_id])
        _,row_count = self.execute(sql, params)
        return row_count > 0