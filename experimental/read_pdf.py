import pdfplumber

with pdfplumber.open("test.pdf") as pdf:
    page = pdf.pages[0]
    text = page.extract_text()
    print(type(text))
