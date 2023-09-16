# pyOcrPdfImg
This project is a basic program with a simple GUI that takes a file or a folder as an argument, and then converts that file (or folder's content) to searchable pdf. It doesn't require anything to be done by the end-user. It supports *pdf, jpeg, png, gif, tiff* and *bmp* formats. 

To start it as a python file, simply run *python gui.py* in your terminal. Prerequisites are listed as:
*pdf2image, os, pytesseract, PyPDF2, io, PIL, PySimpleGUI*.\
The 9-11st lines and 22nd line in the *pdf_convert.py* should be changed according to your *poppler* and *Tesseract-OCR*'s installation locations. Defaultly, the program expects these external dependencies to be present in the same directory with *pdf_convert.py*. And, default text language is set to Turkish. However, it can be changed by changing the values of *text_lang* variables that are in *gui.py*.

If you don't have any intentions to change anything, you can simply download [.zip file](https://drive.google.com/file/d/1VCr-ehvnmno1UoXDGv3ov0WEWKQMhXur/view?usp=drive_link) and work with it.
