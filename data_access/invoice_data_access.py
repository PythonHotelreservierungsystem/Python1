from datetime import date

import model

from data_access.base_data_access import BaseDataAccess


class InvoiceDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    #User Story 5
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

    #User Story 6
    def delete_invoice_by_booking_id(self, booking_id: int):
        if booking_id is None:
            raise ValueError("booking_id cannot be None")
        sql = """DELETE FROM Invoice WHERE Booking_Id = ?"""
        params = tuple([booking_id])
        _,row_count = self.execute(sql, params)
        return row_count > 0

    #User Story 10.3
    def update_invoice(self,invoice_id: int, issue_date: date, total_amount: float)-> model.Invoice:
        sql="""
        UPDATE Invoice SET Issue_Date = ?, Total_Amount = ? WHERE Invoice_Id = ?
        """
        params = (issue_date,total_amount,invoice_id)
        _,row_count = self.execute(sql,params)
        return row_count > 0

    #User Story 10.3
    def read_all_invoices(self)->list[model.Invoice]:
        sql="""
        SELECT Invoice_Id, Issue_Date, Total_Amount, Booking_Id FROM Invoice"""
        invoices = self.fetchall(sql)
        return_list = []
        for invoice_id, issue_date, total_amount, booking_id in invoices:
            return_list.append(model.Invoice(invoice_id, issue_date, total_amount, booking_id))
        return return_list