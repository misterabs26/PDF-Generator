from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm",format="letter")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

def add_footer(topic):
    # footer
    pdf.set_y(-15)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 8, f"Page {pdf.page_no()}: {topic}", align='R')

for i, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(0,0,250)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L",ln=1)
    pdf.line(10,24,206,24)
    add_footer(row["Topic"])

    for page in range(row["Pages"]-1):
        pdf.add_page()
        add_footer(row["Topic"])


pdf.output("output.pdf")