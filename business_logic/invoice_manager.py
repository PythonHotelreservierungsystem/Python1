from datetime import date
from model.invoice import Invoice
from data_access.invoice_data_access import InvoiceDataAccess
from data_access.booking_data_access import BookingDataAccess


class InvoiceManager:
    def __init__(self,invoice_data_access: InvoiceDataAccess,
                 booking_data_access: BookingDataAccess):
        self.invoice_data_access = invoice_data_access
        self.booking_data_access = booking_data_access

    def create_invoice_for_existing_booking(self, booking_id: int) -> Invoice:
        booking = self.booking_data_access.get_booking_by_id(booking_id)
        if not booking:
            raise ValueError(f"Keine Buchung mit ID {booking_id} gefunden.")

        total_naechte = (booking.check_out_date - booking.check_in_date).days

        # Berechne Betrag aus booking.total_amount oder aus Zimmerpreis
        if hasattr(booking, "total_amount") and booking.total_amount:
            gesamtpreis = booking.total_amount
        else:
            gesamtpreis = total_naechte * booking.room.price_per_night

        issue_date = booking.check_out_date

        invoice = self.invoice_data_access.create_invoice(
            issue_date=issue_date,
            total_amount=gesamtpreis,
            booking_id=booking.booking_id
        )
        return invoice