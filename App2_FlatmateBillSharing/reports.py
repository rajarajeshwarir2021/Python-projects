import os
import webbrowser
from fpdf import FPDF
from filestack import Client

API_KEY = "YOUR_API_KEY"


class PDFReport:
    """
    Creates a PDF file that contains data about the flatmates such as their names,
    their due amount and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate_1, flatmate_2, bill):

        flatmate1_pay = str(flatmate_1.pays(bill=bill, flatmate2=flatmate_2))
        flatmate2_pay = str(flatmate_2.pays(bill=bill, flatmate2=flatmate_1))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add image
        pdf.image("files/house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family="Times", size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmate Bill", align="C", ln=1)

        # Insert period label and value
        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period:")
        pdf.cell(w=150, h=40, txt=bill.period, ln=1)

        # Insert the flatmate details
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=flatmate_1.name.title())
        pdf.cell(w=150, h=25, txt=flatmate1_pay, ln=1)
        pdf.cell(w=100, h=25, txt=flatmate_2.name.title())
        pdf.cell(w=150, h=25, txt=flatmate2_pay, ln=1)
        pdf.cell(w=150, h=25, txt=str(bill.amount))

        os.chdir("files")

        # Save the PDF
        pdf.output(self.filename)

        # Open the PDF in a web browser
        webbrowser.open(self.filename)


class FileSharer:
    """
    Class to facilitate Cloud based file sharing
    """

    def __init__(self, filepath, api_key=API_KEY):
        self.api_key = api_key
        self.filepath = filepath

    def share(self):
        client = Client(self.api_key)
        new_file_link = client.upload(filepath=self.filepath)
        return new_file_link.url


