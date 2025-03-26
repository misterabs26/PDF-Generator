from fpdf import FPDF
import pandas as pd
import math

pdf = FPDF(orientation="P", unit="mm",format="letter")
pdf.set_auto_page_break(auto=False, margin=0)

page_width = pdf.w
page_height = math.floor(pdf.h)

df = pd.read_csv("topics.csv")
# note lines
def note_lines(start_y, pg_height, line_spacing):
    for line in range(start_y + line_spacing, pg_height-15, line_spacing):
        pdf.line(10,line,206,line)

# footer
def add_footer(topic):
    # footer
    pdf.set_y(-15)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 8, f"Page {pdf.page_no()}: {topic}", align='R')

# Page customization
for i, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(0,0,250)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L",ln=1)
    pdf.line(10,pdf.get_y(),page_width-10,pdf.get_y())

    #note lines
    note_lines(math.floor(pdf.get_y()), page_height,10)
    #footer
    add_footer(row["Topic"])

    for page in range(row["Pages"]-1):
        pdf.add_page()
        note_lines(math.floor(pdf.get_y()), page_height, 10)
        add_footer(row["Topic"])

pdf.output("output.pdf")