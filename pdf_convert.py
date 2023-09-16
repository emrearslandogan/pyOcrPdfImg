from pdf2image import convert_from_path
from os import listdir
import pytesseract
from PyPDF2 import PdfMerger 
from io import BytesIO 
from PIL import Image

# OCR kısmının ön ayarları
pytesseract.pytesseract.tesseract_cmd = "Tesseract-OCR\\tesseract.exe"
TESSDATA_PREFIX = "Tesseract-OCR\\tessdata"
tessdata_dir_config = '--tessdata-dir "Tesseract-OCR\\tessdata"'


# OCR functions
 
def pdf_convert(file_path, output_folder, text_lang, image_format):
  pdf_name = file_path[(file_path.rfind("/") + 1):]

  print(pdf_name + " dosyası taratılıyor...")    
  
  # Sayfalara parçalama kısmı
  images = convert_from_path(file_path, poppler_path=r"poppler\Library\bin", fmt=image_format) # creates a PIL object of images
  print("Pdf'yi sayfalara parçalama işlemi tamamlandı, taranmaya başlanıyor.")

  # PCR part
  pdfMerger = PdfMerger()

  i = 0
  for image in images:  # and then, we loop around the PIL list, instead of saving each page separately on hard drive
    page_result = pytesseract.image_to_pdf_or_hocr(image, lang=text_lang, config=tessdata_dir_config)
    
    pageIO = BytesIO(page_result) # created ByteIO format of the pdf data (that is currently in bytes format) to be able to use PyPdf2 methods
    pdfMerger.append(pageIO)

    i +=1
    print(str(i) + ". sayfanın taraması tamamlandı")

  print("Dosya kaydediliyor...")
  f = open(output_folder + "/" + pdf_name, "wb")
  pdfMerger.write(f)
  print(pdf_name + " dosyasının taraması tamamlandı")


def img_convert(file_path, output_folder, text_lang):
  img_name = file_path[(file_path.rfind("/") + 1):]
  print(img_name + " dosyası taratılıyor...")
  img_data = Image.open(file_path)  # dosyanın üstünde iş yapabilmek için PIL.Image tipinde bir veriye ihtiyacımız var
  
  img_result = pytesseract.image_to_pdf_or_hocr(img_data, lang=text_lang, config=tessdata_dir_config)

  f = open(output_folder + "/" + img_name[:img_name.rfind(".")] + ".pdf", "wb")
  f.write(bytearray(img_result))
  print(img_name + " dosyasının taraması tamamlandı, kaydedildi")
  f.close()


# pdf -> pdfa, just use pdf_convert function
# img -> pdfa  just use img_convert function

# folder source -> pdfa's
def folder_convert(folder_path, output_folder, text_lang, image_format):
  for file_name in listdir(folder_path): # listdir is an os method
    if (file_name[-4:] == ".pdf"):  # o dosya pdf ise   
      pdf_convert(folder_path + "/" + file_name, output_folder, text_lang, image_format)
    
    elif (file_name[file_name.rfind(".")+1:] in ["jpg", "jpeg", "png", "tiff", "gif", "bmp"]):
      img_convert(folder_path + "/" + file_name, output_folder, text_lang)
      
    else: continue # eğer dosya resim veya pdf değilse
