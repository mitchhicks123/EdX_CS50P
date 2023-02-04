
from fpdf import FPDF

"""
class PDF(FPDF):
    def header(self):
        ...
    def footer(self):
        ...
"""


def main():
    name = input("Name: ").strip().capitalize() + " took CS50 "

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.image("shirtificate.png", h=pdf.eph/1.5, y=pdf.eph/3, w=pdf.epw)

    pdf.set_font('helvetica', size=30, style="B")
    pdf.multi_cell(h=50, w=pdf.epw, txt="CS50 Shirtificate", align="c")

    pdf.ln()

    pdf.set_font(size=24)
    pdf.set_text_color(255, 255, 255)
    pdf.multi_cell(h=80, w=pdf.epw, txt=name, align="c")

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
