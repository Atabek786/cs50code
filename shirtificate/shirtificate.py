from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Rendering logo:
        self.image("/workspaces/134886326/shirtificate/shirtificate.png", 10, 8, 33)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 15)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "CS50 Shirtificate", border=1, align="C")
        # Performing a line break:
        self.ln(20)

    def footer(self, name):  # Accept the 'name' parameter here
        # Position cursor at 1.5 cm from the bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "I", 8)
        # Printing page number:
        self.cell(0, 10, f"{name} took CS50", align="C")

name = input("Name: ")
pdf = PDF()
pdf.add_page()

# Call the header method
pdf.header()

# Call the footer method and pass the 'name' variable
pdf.footer(name)

pdf.output("certificate.png")