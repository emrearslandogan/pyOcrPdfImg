import PySimpleGUI as sg
from pdf_convert import *

layout = [
        [sg.Text("Taranacak dosya"), sg.Input(key="-INFILE-"), sg.FileBrowse("Dosya seç"), sg.Text("Taranacak Klasör"), sg.Input(key="-INFOLDER-"), sg.FolderBrowse("Klasör seç")],
        [sg.Text("Çıktı klasörü:"), sg.Input(key="-OUT-"), sg.FolderBrowse()],
        [sg.Exit("Çıkış"), sg.Button("TARA")],
]

window = sg.Window("PDF ve Fotoğraf Tarayıcı", layout, resizable=True)

while True:
  event, values = window.read()
  print(event, values) # bug -varsa- yakalamak için

  if event in (sg.WINDOW_CLOSED, "Çıkış"):
    break
  
  if event == "TARA":
    if values["-INFOLDER-"] and values["-INFILE-"]: sg.popup_error("Lütfen sadece klasör ya da dosya girişi yapınız")
    elif not values["-OUT-"]: sg.popup_error("Lütfen taranmış pdf'ler için bir klasör seçiniz")
    elif values["-INFILE-"] and values["-INFILE-"][-4:] == ".pdf": # yani girilen dosya bir pdf dosyası ise
      pdf_convert(
        file_path=values["-INFILE-"],
        output_folder=values["-OUT-"],
        text_lang="tur",
        image_format="png"
      )
      sg.popup_no_titlebar("Tarama başarıyla tamamlandı!!\nİşlemlerinize devam edebilirsiniz")
    
    elif values["-INFILE-"] and values["-INFILE-"][values["-INFILE-"].rfind(".") +1:] in ["jpg", "jpeg", "png", "tiff", "gif", "bmp"]: # yani girilen dosya bir resim ise
      img_convert(
        file_path=values["-INFILE-"],
        output_folder=values["-OUT-"],
        text_lang="tur"
      )
      sg.popup_no_titlebar("Tarama başarıyla tamamlandı!!\nİşlemlerinize devam edebilirsiniz")

    elif values["-INFOLDER-"]:  # klasör gelince direkt ana fonksiyona bırakıyor ayırt etme işini, burada yapılmıyor
      folder_convert(
        folder_path=values["-INFOLDER-"],
        output_folder=values["-OUT-"],
        text_lang="tur",
        image_format="png"
      )
      sg.popup_no_titlebar("Tarama başarıyla tamamlandı!!\nİşlemlerinize devam edebilirsiniz")

    else:
      sg.popup_error("Lütfen taratacak dosyalar'ler için kaynak seçiniz")


window.close()