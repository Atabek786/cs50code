from fpdf import FPDF

class Shirtificate(FPDF):
    def header(self):
        self.set_font("helvetica", style="", size=48)
        self.cell(w=0, h=50, txt="CS50 Shirtificate", align="C")
        self.ln(10)

    def image(self):
        self.image("./shirtificate.png", 0, 60)

    def footer(self, name):
        self.set_font(family="helvetica", style="",size=20)
        self.set_text_color(255,255,255)
        self.cell(w=0, h=220, txt=f"{name} took CS50", align="C")

pdf = Shirtificate()
pdf.add_page()
pdf.image()
pdf.shirt_text(input("Name: "))
pdf.outpud("shirtificate.pdf")

