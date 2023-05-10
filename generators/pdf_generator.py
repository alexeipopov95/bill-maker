from abc import abstractmethod
from fpdf import FPDF
from fpdf.enums import XPos, YPos
from datetime import date

from constants import FontFamily, FontStyle, Align


class BasePDFGenerator(FPDF):
    """ Class to generate a PDF report """
    DEFAULT_FONT = FontFamily.HELVETICA.value

    def __init__(self, title:str=None) -> None:
        """ Constructor method """
        self.title = title

        super().__init__()

    def custom_cell(self, text:str, align:Align=None) -> None:
        """ Method to generate a custom cell"""
        align = align if align else Align.LEFT
        cell_width = 0 # Width of cells. If 0, the cell extends up to the right margin.
        cell_height = 10 # Height of cells. If 0, they are automatically calculated.
        self.cell(
            w=cell_width,
            h=cell_height,
            txt=text,
            align=align.value,
            new_x=XPos.LMARGIN,
            new_y=YPos.NEXT,
        )

    def header(self):
        """ Method to generate the header of the document """
        title = self.title if self.title else "Flatmates Bill"
        font_size = 25

        self.set_font(self.DEFAULT_FONT, FontStyle.BOLD.value, font_size)
        self.custom_cell(text=title, align=Align.CENTER)
        self.ln(20)

    def footer(self):
        """ Method to generate the footer of the document """
        text = f"Page {self.page_no()}/{self.pages_count}"
        font_size = 15

        self.set_y(-15)
        self.set_font(self.DEFAULT_FONT, FontStyle.ITALIC.value, font_size)
        self.custom_cell(text=text, align=Align.CENTER)

    @abstractmethod
    def generate(self, data: list=None) -> None:
        """ Method to generate a report """
        raise NotImplementedError


class PdfReport(BasePDFGenerator):
    """ Class to generate a PDF report """

    def __init__(self) -> None:
        """ Constructor method """
        super().__init__(title="Flatmates Bill")

    def generate(self, data: list = None) -> None:
        """ Method to generate a report """
        curr_date = date.today().strftime("%d-%m-%Y")
        file_name = f"Flatmates Bill - {curr_date}.pdf"
        self.add_page()
        self.set_font(self.DEFAULT_FONT, size=12)
        for _ in range(1, 41):
            self.custom_cell(
                f"Printing line number {_}"
            )
        self.output(name=file_name)



if __name__ == "__main__":
    pdf = PdfReport()
    pdf.alias_nb_pages()
    pdf.generate()
    
