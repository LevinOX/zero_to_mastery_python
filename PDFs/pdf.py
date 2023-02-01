import sys
import PyPDF2

inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('PDFs/super.pdf')


pdf_combiner(inputs)
# with open('PDFs/twopage.pdf', 'rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     page = reader.getPage(0)
#     #page = reader.getNumPages
#     page.rotateCounterClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open('PDFs/tilt.pdf', 'wb') as new_file:
#         writer.write(new_file)
