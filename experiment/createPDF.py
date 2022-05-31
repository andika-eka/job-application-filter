from fpdf import FPDF
import random

lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus placerat in eros et ultricies. Cras ornare lorem sit amet leo ultrices aliquam. Fusce eu nunc leo. Nunc sed erat tellus. Phasellus quis nulla nunc. Donec aliquet augue in enim accumsan, at pellentesque elit mattis. Suspendisse vulputate, purus eu dictum imperdiet, lectus felis semper eros, vel accumsan lectus urna sit amet mi. Nullam tristique est id magna feugiat, nec accumsan tellus porta."

pdf = FPDF()
pdf.add_page()

#image
top_left_x, top_left_y = 0, 0
with pdf.round_clip(x=top_left_x + 12, y=top_left_y + 2, r=38):
    pdf.image(   "https://source.unsplash.com/random", 10, 0, 70)

#name and title
pdf.set_draw_color(r=0, g=0, b=0)
pdf.set_line_width(1.5)
pdf.set_font("helvetica", "B", 20)
pdf.cell(50)
pdf.line(x1=55, y1=30, x2=200, y2=30)
pdf.cell(0, 0, "Putu andika Eka putra", border=0,)
pdf.set_font("helvetica", size =15)
pdf.ln(10)
pdf.cell(50)
pdf.cell(0, 0, "software engineer", border=0,)
pdf.ln(20)

#contact
pdf.set_font("helvetica", "B", size=15)
pdf.set_y(50)
pdf.cell(0, 5, "Contact:", new_x="LMARGIN", new_y="NEXT")
pdf.set_line_width(0.5)
pdf.line(x1=10, y1=55, x2=50, y2=55)
for i in range(1,6):
    pdf.ln(2)
    pdf.set_font("helvetica", "B", size=12)
    pdf.cell(2)
    pdf.cell(0, 5, f"contact {i}", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("helvetica", size=12)
    pdf.cell(5)
    pdf.cell(0, 5, f"content {i}", new_x="LMARGIN", new_y="NEXT")

# list 1 , 2 , 3
pdf.set_font("helvetica", "B", size=12)
pdf.ln(10)
pdf.cell(0, 5, "List 1 :", new_x="LMARGIN", new_y="NEXT")
pdf.line(x1=10, y1=pdf.get_y(), x2=50, y2=pdf.get_y())
pdf.set_font("helvetica", size=12)
pdf.ln(2)
for i in range(1,6):
    pdf.cell(2)
    pdf.cell(0, 5, f"Printing line number {i}", new_x="LMARGIN", new_y="NEXT")

pdf.set_font("helvetica", "B", size=12)
pdf.ln(10)
pdf.cell(0, 5, "List 2 :", new_x="LMARGIN", new_y="NEXT")
pdf.line(x1=10, y1=pdf.get_y(), x2=50, y2=pdf.get_y())
pdf.set_font("helvetica", size=12)
pdf.ln(2)
for i in range(1,4):
    pdf.cell(2)
    pdf.cell(0, 5, f"Printing line number {i}", new_x="LMARGIN", new_y="NEXT")



pdf.set_font("helvetica", "B", size=12)
pdf.ln(10)
pdf.cell(0, 5, "List 3 :", new_x="LMARGIN", new_y="NEXT")
pdf.line(x1=10, y1=pdf.get_y(), x2=50, y2=pdf.get_y())
pdf.set_font("helvetica", size=12)
pdf.ln(2)
for i in range(1,5):
    pdf.cell(2)
    pdf.cell(0, 5, f"Printing line number {i}", new_x="LMARGIN", new_y="NEXT")

pdf.set_y(40)
pdf.set_left_margin(60)

pdf.set_font("helvetica", "B", size=15)
pdf.cell(10, 10, "Summary: ", new_x="LMARGIN", new_y="NEXT")
pdf.line(x1=60, y1=pdf.get_y(), x2=200, y2=pdf.get_y())
pdf.ln(3)
pdf.set_font("helvetica", size=12)
pdf.write( txt = lorem[:200])
pdf.ln(10)

pdf.set_font("helvetica", "B", size=15)
pdf.cell(10, 10, "Education: ", new_x="LMARGIN", new_y="NEXT")
pdf.line(x1=60, y1=pdf.get_y(), x2=200, y2=pdf.get_y())
pdf.ln(3)
pdf.set_font("helvetica", size=12)
pdf.set_left_margin(65)
for i in range(1,3):
    pdf.write( txt = lorem[:50])
    pdf.ln(5)
pdf.ln(5)

pdf.set_left_margin(60)
pdf.set_font("helvetica", "B", size=15)
pdf.cell(10, 10, "Experience: ", new_x="LMARGIN", new_y="NEXT")
pdf.line(x1=60, y1=pdf.get_y(), x2=200, y2=pdf.get_y())
pdf.ln(3)
pdf.set_font("helvetica", size=12)
pdf.set_left_margin(65)
for i in range(1,7):
    pdf.write( txt = lorem[:random.randint(50, 200)])
    pdf.ln(8)
pdf.ln(5)

pdf.set_left_margin(60)
pdf.set_font("helvetica", "B", size=15)
pdf.cell(10, 10, "Text: ", new_x="LMARGIN", new_y="NEXT")
pdf.line(x1=60, y1=pdf.get_y(), x2=200, y2=pdf.get_y())
pdf.ln(3)
pdf.set_font("helvetica", size=12)
pdf.write( txt = lorem[:200])
pdf.ln(10)

pdf.output("generated.pdf")
