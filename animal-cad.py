from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from PIL import Image, ImageTk
import subprocess
import cv2
import numpy as np
from tkinter import filedialog


animal = Tk()

# Configurações da tela
animal.title("Dogin's")

animal.resizable(False, False)

width_screen = animal.winfo_screenwidth()
height_screen = animal.winfo_screenheight()

width = 900
height = 600


posx = (width_screen / 2) - (width / 2)
posy = (height_screen / 2) - (height / 2)

animal.maxsize(width, height)
animal.minsize(width, height)

animal.geometry("%dx%d+%d+%d" % (width, height, posx, posy))
animal.configure(bg='#fff')

#text "Cadastro do Cliente"
lbl_agradecimentos = Label(animal, text="Cadastro do Animal", bg="#F0E68C", font=("Helvetica 14 bold")).place(x=430, y=100)

# foto "logo"
fotoOriginal = Image.open("imgs/logo.png")
fotoResize = fotoOriginal.resize((150, 30))
fotoLogo = ImageTk.PhotoImage(fotoResize)
test = Label(animal, bg="#FFFFFF", image=fotoLogo).place(x=100, y=40)

#foto "perfil"
fotoOriginal = Image.open("imgs/perfil.png")
fotoResize = fotoOriginal.resize((130, 130))
fotoPerfil = ImageTk.PhotoImage(fotoResize)
Perfil = Label(animal, bg="#FFFFFF", image=fotoPerfil).place(x=100, y=150)

#text "Código de cadastro "
lbl_codigo = Label(animal, bg="#FFF", text="Código de cadastro",font="Helvetica 10").place(x=310, y=150)
txt_codigo = Entry(animal, width=30)
txt_codigo.place(x=310, y=180)

#text "Peso"
lbl_Peso = Label(animal, bg="#FFF", text="Peso",font="Helvetica 10").place(x=530, y=150)
txt_Peso = Entry(animal, width=30)
txt_Peso.place(x=530, y=180)

#text "Data de nascimento "
lbl_nasc = Label(animal, bg="#FFF", text="Data de nascimento",font="Helvetica 10").place(x=310, y=220)
txt_nasc = Entry(animal, width=25)
txt_nasc.place(x=310, y=250)

#text "Idade "
lbl_idade = Label(animal, bg="#FFF", text="Idade",font="Helvetica 10").place(x=310, y=290) 
txt_idade = Entry(animal, width=21)
txt_idade.place(x=310, y=320)

# text " Esecie  "
lbl_dataNascimento = Label(animal, bg="#FFF", text="Especie",font="Helvetica 10").place(x=530, y=220)
txt_dataNascimento = Entry(animal, width=25)
txt_dataNascimento.place(x=530, y=240)

#text "Raça "
lbl_especie = Label(animal, bg="#FFF", text="Raça ",font="Helvetica 10").place(x=530, y=280)
txt_especie = Entry(animal, width=25)
txt_especie.place(x=530, y=310)


def salvar():
    variavel_codigo= txt_codigo.get()
    variavel_peso = txt_Peso.get()
    variavel_data = txt_dataNascimento.get()
    variavel_idade = txt_idade.get()
    variavel_especie = txt_especie.get()

    if(variavel_codigo == "" or variavel_peso == "" or variavel_data=="" or variavel_idade=="" or variavel_especie==""):
        MessageBox.showinfo("Erro","Há campos em branco")
    else:

        conectar = mysql.connect(host="localhost",user="root",password="", database="cadastro")
        cursor = conectar.cursor()
        cursor.execute("insert into cadastrar values('"+ variavel_codigo + "','"+ variavel_peso + "','"+ variavel_data + "', '"+ variavel_idade + "','"+ variavel_data + "')")
        cursor.execute("commit")
        MessageBox.showinfo("Mensagem","Cadastro realizado com sucesso")
        conectar.close()


def alterar():
    variavel_codigo = txt_codigo.get()
    variavel_peso = txt_Peso.get()
    variavel_data = txt_dataNascimento.get()
    variavel_idade = txt_idade.get()
    variavel_especie = txt_especie.get()

    if (variavel_codigo == "" or variavel_peso == "" or variavel_data == "" or variavel_idade == "" or variavel_especie == ""):
        MessageBox.showinfo("Erro", "Há campos em branco")
    else:
        conectar = mysql.connect(host="localhost", user="root", password="", database="cadastro")
        cursor = conectar.cursor()
        cursor.execute("UPDATE cadastrar SET peso=%s, data=%s, idade=%s, especie=%s WHERE código=%s",
                       (variavel_peso, variavel_data, variavel_idade, variavel_especie, variavel_codigo))
        conectar.commit()
        MessageBox.showinfo("Mensagem", "Cadastro alterado com sucesso")
        conectar.close()

def excluir():
    variavel_codigo = txt_codigo.get()

    if (variavel_codigo == ""):
        MessageBox.showinfo("Erro", "O campo código está em branco")
    else:
        conectar = mysql.connect(host="localhost", user="root", password="", database="cadastro")
        cursor = conectar.cursor()
        cursor.execute("DELETE FROM cadastrar WHERE código=%s", (variavel_codigo,))
        conectar.commit()
        MessageBox.showinfo("Mensagem", "Cadastro excluído com sucesso")
        conectar.close()

def consultar():
    conectar = mysql.connect(host="localhost", user="root", password="", database="cadastro")
    cursor = conectar.cursor()
    cursor.execute("SELECT * FROM cadastrar")
    registros = cursor.fetchall()
    conectar.close()

    for registro in registros:
        print(registro)

# buttons
btn_salvar = Button(animal, width=15, text="Salvar", activebackground="#FFFF00", bd=0, bg="#FFFF00",compound=TOP, command=salvar).place(x=230, y=490)
btn_alterar = Button(animal, width=15, text="Alterar", bg="#fff", bd=1,compound=TOP, command=alterar).place(x=350, y=490)
btn_excluir = Button(animal, width=15, text="Excluir", bg="#fff", bd=1,compound=TOP, command=excluir).place(x=480, y=490)
btn_consultar = Button(animal, width=15, text="Consultar", bg="#fff", bd=1,compound=TOP, command=consultar).place(x=610, y=490)


def abrir_tela_tk():
    subprocess.run(["python", "rotacao.py"])
btn_imagem = Button(animal, width=15, text="Carregar Imagem", bg="#fff", bd=1,compound=TOP, command=abrir_tela_tk).place(x=110, y=300)



animal.mainloop()