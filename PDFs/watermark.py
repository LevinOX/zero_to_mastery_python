import os
import PyPDF2 as pdf

# Read the watermark
watermark = pdf.PdfFileReader("PDFs/wtr.pdf")

# Read the page without watermark
ORIG = "twopage.pdf"
template = pdf.PdfFileReader(f"PDFs/{ORIG}")
page = template.pages[0]
print(template.pages)

# Add the page to the writer
output = pdf.PdfFileWriter()
output.addPage(page)

# Add the watermark to the page
# page.mergePage(watermark.pages[0])
for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

# finally, write the new document with a watermark
name_orig = os.path.splitext(ORIG)[0]
with open(f"PDFs/{name_orig}_water.pdf", "wb") as fp:
    output.write(fp)
