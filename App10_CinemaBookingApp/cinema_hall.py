import random
import sqlite3
import string
from fpdf import FPDF


class Seat:
    """Represents a cinema seat that can be taken from a User"""

    database = "files/cinema.db"

    def __init__(self, seat_id):
        self.seat_id = seat_id

    def get_price(self):
        """Get the price of a certain seat"""
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "price" FROM "Seat" WHERE "seat_id" = ?""", [self.seat_id])
        price = cursor.fetchall()[0][0]
        return price

    def is_free(self):
        """Check in the database if a Seat is taken or not"""
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "taken" FROM "Seat" WHERE "seat_id" = ?""", [self.seat_id])
        result = cursor.fetchall()[0][0]

        if result == 0:
            return True
        else:
            return False

    def occupy(self):
        """Change the value of taken in the database from 0 to 1 if Seat is free"""
        if self.is_free():
            connection = sqlite3.connect(self.database)
            connection.execute("""
            UPDATE "Seat" SET "taken"=? WHERE "seat_id"=?""", [1, self.seat_id])
            connection.commit()
            connection.close()


class Ticket:
    """Represents a cinema Ticket purchased by a User"""
    def __init__(self, user, price, seat_number):
        self.id = "".join([random.choice(string.ascii_letters) for i in range(8)])
        self.user = user
        self.price = price
        self.seat_number = seat_number

    def to_pdf(self):
        """Creates a PDF ticket"""
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Insert title
        pdf.set_font(family="Times", size=24, style='B')
        pdf.cell(w=0, h=80, txt="Your Digital Ticket", align="C", ln=1, border=1)

        # Insert data
        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=25, txt="Name", border=1)
        pdf.set_font(family="Times", size=12, style='')
        pdf.cell(w=0, h=25, txt=self.user.name, border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=25, txt="Ticket ID", border=1)
        pdf.set_font(family="Times", size=12, style='')
        pdf.cell(w=0, h=25, txt=self.id, border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=25, txt="Price", border=1)
        pdf.set_font(family="Times", size=12, style='')
        pdf.cell(w=0, h=25, txt=str(self.price), border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=25, txt="Seat Number", border=1)
        pdf.set_font(family="Times", size=12, style='')
        pdf.cell(w=0, h=25, txt=str(self.seat_number), border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        pdf.output("your_ticket.pdf", 'F')