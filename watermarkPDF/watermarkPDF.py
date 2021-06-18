import img2pdf
import PyPDF2
from PIL import Image
import os
import sys
  

pdf_file = sys.argv[1]

merged_file = "merged.pdf"

# storing image path
img_path = sys.argv[2]


img = Image.open(img_path)
img = img.convert("RGBA")
datas = img.getdata()

newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

img.putdata(newData)
img.save("img2.png", "PNG")





os.system("convert img2.png -background white -alpha remove -alpha off output.png")

  
# storing pdf path
pdf_path = "file.pdf"
  
# opening image
image = Image.open("output.png")
  
# converting into chunks using img2pdf
pdf_bytes = img2pdf.convert(image.filename)
  
# opening or creating pdf file
file = open(pdf_path, "wb")
  
# writing pdf files with chunks
file.write(pdf_bytes)
  
# closing image file
image.close()
  
# closing pdf file
file.close()
watermark = "file.pdf"


input_file = open(pdf_file,'rb')
input_pdf = PyPDF2.PdfFileReader(pdf_file)
watermark_file = open(watermark,'rb')
watermark_pdf = PyPDF2.PdfFileReader(watermark_file)


pdf_page = input_pdf.getPage(0)
watermark_page = watermark_pdf.getPage(0)

pdf_page.mergePage(watermark_page)

output = PyPDF2.PdfFileWriter()
output.addPage(pdf_page)
merged_file = open(merged_file,'wb')
output.write(merged_file)
merged_file.close()
watermark_file.close()
input_file.close()

os.remove("file.pdf")