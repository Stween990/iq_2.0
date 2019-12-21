from tkinter import *
from tkinter import filedialog
import os
from PyPDF2 import PdfFileWriter, PdfFileReader
from datetime import datetime

root = Tk()
root.title("Manipulación Masiva de Documentos - DISCOLMEDICA SAS")
root.iconbitmap()
root.geometry("600x400")


def find_folder():
    file_name = filedialog.askdirectory(initialdir="/", title="Seleccione un archivo")
    input_busqueda = Label(root, text=file_name, font="Lexend 14").place(x=70, y=150)

    if len(file_name) > 0:
        get_file_name(file_name)
    else:
        return "Error al intentar cargar la carpeta"


label_busqueda = Label(root, text="Ruta ", font="Lexend 16 bold").place(x=50, y=150)
button_busqueda = Button(
    root, text="Cargar", font="Lexend 16 bold", command=find_folder
).place(x=500, y=140)


def get_file_name(file_name):
    replaced_str = file_name.replace("\n", "/")
    clean_str = replaced_str.replace("C:", "")
    os.chdir(clean_str)
    # PROCESO
    if len(clean_str) > 1:
        for pdf in os.listdir():
            path_file = clean_str + "/" + pdf
            array_filename = list(pdf)
            if path_file.find("ANEX") == 52:
                rename = os.rename(
                    path_file,
                    clean_str
                    + "/"
                    + "0_828002423_"
                    + array_filename[11]
                    + array_filename[12]
                    + array_filename[13]
                    + array_filename[14]
                    + array_filename[15]
                    + array_filename[16]
                    + array_filename[17]
                    + array_filename[18]
                    + array_filename[19]
                    + "_7_0.pdf",
                )
            elif path_file.find("AUTO") == 52:
                rename = os.rename(
                    path_file,
                    clean_str
                    + "/"
                    + "0_828002423_"
                    + array_filename[11]
                    + array_filename[12]
                    + array_filename[13]
                    + array_filename[14]
                    + array_filename[15]
                    + array_filename[16]
                    + array_filename[17]
                    + array_filename[18]
                    + array_filename[19]
                    + "_11_0.pdf",
                )
            elif path_file.find("ORDM") == 52:
                rename = os.rename(
                    path_file,
                    clean_str
                    + "/"
                    + "0_828002423_"
                    + array_filename[11]
                    + array_filename[12]
                    + array_filename[13]
                    + array_filename[14]
                    + array_filename[15]
                    + array_filename[16]
                    + array_filename[17]
                    + array_filename[18]
                    + array_filename[19]
                    + "_5_0.pdf",
                )
            elif path_file.find("FACT") == 52:
                rename = os.rename(
                    path_file,
                    clean_str
                    + "/"
                    + "0_828002423_"
                    + array_filename[11]
                    + array_filename[12]
                    + array_filename[13]
                    + array_filename[14]
                    + array_filename[15]
                    + array_filename[16]
                    + array_filename[17]
                    + array_filename[18]
                    + array_filename[19]
                    + "_4_0.pdf",
                )
            elif path_file.find("HICL") == 52:
                rename = os.rename(
                    path_file,
                    clean_str
                    + "/"
                    + "0_828002423_"
                    + array_filename[11]
                    + array_filename[12]
                    + array_filename[13]
                    + array_filename[14]
                    + array_filename[15]
                    + array_filename[16]
                    + array_filename[17]
                    + array_filename[18]
                    + array_filename[19]
                    + "_16_0.pdf",
                )
            elif path_file.find("FALT") == 52:
                rename = os.rename(
                    path_file,
                    clean_str
                    + "/"
                    + "0_828002423_"
                    + array_filename[11]
                    + array_filename[12]
                    + array_filename[13]
                    + array_filename[14]
                    + array_filename[15]
                    + array_filename[16]
                    + array_filename[17]
                    + array_filename[18]
                    + array_filename[19]
                    + "_2_0.pdf",
                )
            elif path_file.find("COMP") == 52:
                rename = os.rename(
                    path_file,
                    clean_str
                    + "/"
                    + "0_828002423_"
                    + array_filename[11]
                    + array_filename[12]
                    + array_filename[13]
                    + array_filename[14]
                    + array_filename[15]
                    + array_filename[16]
                    + array_filename[17]
                    + array_filename[18]
                    + array_filename[19]
                    + "_18_0.pdf",
                )
        os.startfile(replaced_str)


root.mainloop()

