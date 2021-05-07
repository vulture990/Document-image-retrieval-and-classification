from fpdf import FPDF
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img=cv2.imread('test.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
file=open('data.txt','w')
file.write(pytesseract.image_to_string(img))
file.close()
file = open('data.txt', 'r')
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=15)

for x in file:
  # cuz it needs to encode to latin-1 otherwise it l give an execption just the way this lib was made x'(
    x2 = x.encode('latin-1', 'replace').decode('latin-1')
    pdf.cell(100, 10, txt=x2, ln=1, align='C')

pdf.output("text.pdf")

file.close()

