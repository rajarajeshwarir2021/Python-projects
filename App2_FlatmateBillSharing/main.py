from flat import Bill, Flatmate
from reports import PDFReport, FileSharer

if __name__ == '__main__':

    bill_amount = float(input("Hey user, enter the bill amount: "))
    bill_period = input("Enter the bill period E.g. December 2020: ")

    flatmate1_name = input("Enter your name: ")
    flatmate1_days = int(input("Enter the number of days you stayed in the house during the bill period: "))

    flatmate2_name = input("Enter the flatmate's name: ")
    flatmate2_days = int(input(f"Enter the number of days {flatmate2_name} stayed in the house during the bill period: "))

    the_bill = Bill(bill_amount, bill_period)
    flatmate1 = Flatmate(flatmate1_name, flatmate1_days)
    flatmate2 = Flatmate(flatmate2_name, flatmate2_days)

    print(f"{flatmate1.name} pays: ", flatmate1.pays(the_bill, flatmate2))
    print(f"{flatmate2.name} pays: ", flatmate2.pays(the_bill, flatmate1))

    pdf_report = PDFReport(filename=f"{bill_period}.pdf")
    pdf_report.generate(flatmate1, flatmate2, the_bill)

    file_sharer = FileSharer(filepath=pdf_report.filename)