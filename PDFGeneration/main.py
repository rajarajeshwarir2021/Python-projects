import pandas as pd
from fpdf import FPDF


df = pd.read_csv("data.csv", delimiter=';')
print(df)

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

for idx, row in df.iterrows():
    pdf.add_page()
    pdf.set_text_color(100, 100, 100)
    pdf.set_font(family='Times', style='B', size=24)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1)

    # Add lines
    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)

    # Set the footer for the page
    pdf.ln(265)
    pdf.set_font(family='Times', style='I', size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row['Topic'], align='R')

    for i in range(row['Pages'] - 1):
        pdf.add_page()

        # Add lines
        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

        # Set the footer for the page
        pdf.ln(277)
        pdf.set_font(family='Times', style='I', size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row['Topic'], align='R')

pdf.output("samplePDF.pdf")
