from PyPDF2 import PdfFileWriter, PdfFileReader
import img2pdf
from PIL import Image, ImageEnhance
import sys
import os


input_pdf=sys.argv[1], 
output='watermarkedPDF.pdf',
watermark=sys.argv[2]

im = Image.open(watermark, "r")

if im.mode != 'RGBA':
        im = im.convert('RGBA')
else:
    im = im.copy()
alpha = im.split()[3]
alpha = ImageEnhance.Brightness(alpha).enhance(0.1)
im.putalpha(alpha)

watermark = im
watermark.save("input.png")


# os.system("convert input.png -background white -alpha remove -alpha off saved_image.png")

pdf_path = "file.pdf"
watermark = Image.open("input.png")
# converting into chunks using img2pdf
pdf_bytes = img2pdf.convert(watermark.filename)
  
# opening or creating pdf file
file = open(pdf_path, "wb")
  
# writing pdf files with chunks
file.write(pdf_bytes)
  
# closing image file
image.close()
  
# closing pdf file
file.close()

watermark = 'file.pdf'

watermark_obj = PdfFileReader(watermark)
watermark_page = watermark_obj.getPage(0)

pdf_reader = PdfFileReader(input_pdf)
pdf_writer = PdfFileWriter()


for page in range(pdf_reader.getNumPages()):
    page = pdf_reader.getPage(page)
    page.mergePage(watermark_page)
    pdf_writer.addPage(page)

with open(output, 'wb') as out:
    pdf_writer.write(out)

os.remove('file.pdf')