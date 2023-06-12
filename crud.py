from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import cv2
import numpy as np
import tkinter as tk


crud=Tk()

#Configurações da tela
taskBarHeight = 40
crud.title("Acesso ao Petshop Dogin's")
crud.resizable(False, False)

width_screen = crud.winfo_screenwidth()
height_screen = crud.winfo_screenheight() - taskBarHeight

width = 1240
height = 700

posx = (width_screen / 2) - (width / 2)
posy = (height_screen / 2) - (height / 2)

crud.maxsize(width, height)
crud.minsize(width, height)

crud.geometry("%dx%d+%d+%d" % (width, height, posx, posy))
crud.configure(bg='#fff')

logodoginsorigin = Image.open("imgs/logo.png")
logoresize = logodoginsorigin.resize((140, 50))
logoDogins = ImageTk.PhotoImage(logoresize)
logodog = Label(crud, image = logoDogins , bg="#fff")
logodog.place(relx = .150, rely = .10, anchor = "n")

lbl_nome = Label(crud, text="Nome", font=("Arial 12"))
lbl_nome.place(relx=0.37,rely=0.3)
txt_nome= Entry(crud, font=("Aial 12"),backgroud="#FFF")
txt_nome.place(relx=0.43 , rely=0.3)


lbl_cpf=Label(crud,text="CPF:", font=("Arial 12"))
lbl_cpf.place(relx=0.37,rely=0.4)
txt_cpf=Entry(crud, font=("Arial 12") , backgroud="#FFF")
txt_cpf.place(relx=0.43, rely=0.4)


lbl_email=Label(crud,text="E-mail:", font=("Arial 12"))
lbl_email.place(relx=0.37,rely=0.5)
txt_email = Entry(crud, font=("Arial 12"), backgroud="#FFF")
txt_email.place(relx=0.43,rely=0.5)


def salvar():
    variavel_nome= txt_nome.get()
    variavel_cpf = txt_cpf.get()
    variavel_email = txt_email.get()

    if(variavel_nome == "" or variavel_cpf == "" or variavel_email==""):
        MessageBox.showinfo("Erro","Há campos em branco")
    else:

        conectar = mysql.connect(host="localhost",user="root",password="", database="crud")
        cursor = conectar.cursor()
        cursor.execute("insert into promocao values('"+ variavel_nome + "','"+ variavel_email + "','"+ variavel_cpf + "')")
        cursor.execute("commit")
        MessageBox.showinfo("Mensagem","Cadastro realizado com sucesso")
        conectar.close()

def excluir():
    if(txt_nome.get() == ""):
        MessageBox.showinfo("ALERT" , "Digite o código para deletar")
    else:
        conectar= mysql.connect(host="localhost", user="root",password="", database="crud")
        cursor = conectar.cursor()
        cursor.execute("delete from promocao where cpf='"+txt_cpf.get() + "'")
        cursor.execute("commit")
        MessageBox.showinfo("Mensagem", "Informação excluída com sucesso")
        crud.close()

def atualizar():
    id = txt_nome.get()
    name = txt_nome.get()
    cpf = txt_cpf.get()
    if(name == "" or cpf == ""):
        MessageBox.showinfo("ALERT" , "Digite todos os campos para realizar alteração")
    else:
        conectar = mysql.connect(host="localhost", user="root",password="", database="crud")
        cursor = conectar.cursor()
        cursor.execute("Update promocao set nome = '"+ txt_nome.get() +"', email='"+ txt_email.get() + "'where cpf = '"+ txt_cpf.get()+"'")
        cursor.execute("commit");
        MessageBox.showinfo("status","Successfully Update")
        conectar.close()

def Select():
    if(txt_cpf.get() == ""):
        MessageBox.showinfo("ALERT","Por favor digite o código")
    else:
        conectar = mysql.connect(host="localhost",user="root", password="",database="crud")
        cursor = conectar.cursor()
        cursor.execute("select * from promocao where cpf= '" + txt_cpf.get()+"'")
        rows = cursor.fetchall()
        for row in rows:
            txt_nome.insert(0, row[0])
            txt_email.insert(0, row[1])
        conectar.close()
txt_mensagem = Text(crud, text="Faça seu cadastro para receber promoções exclusivas",font=("Arial 18")).place(relx=0.5,rely=0.2)

btn_salvar = Button(crud, text="Salvar", command=salvar, font=("Arial 12")).place(relx=0.3,rely=0.65)
btn_excluir = Button(crud, text="Apagar", command=excluir, font=("Arial 12")).place(relx=0.4, rely=0.65)
btn_update = Button(crud, text="Update", command=atualizar, font=("Arial 12")).place(relx=0.5, rely=0.65)
btn_consultar = Button(crud, text="Consultar", command=Select, font=("Arial 12")).place(relx=0.6, rely=0.65)


#Rotação imagem
def Simples(rotacao_image, angulo):
    altura, largura = rotacao_image.shape[0], rotacao_image.shape[1]
    y, x = altura / 2, largura / 2
    rotacao_matriz = cv2.getRotationMatrix2D((x, y), angulo, 1.0)
    rotacionando_image = cv2.warpAffine(rotacao_image, rotacao_matriz, (largura, altura))
    return rotacionando_image

def complexo(rotacao_image, angulo):
    altura, largura = rotacao_image.shape[0], rotacao_image.shape[1]
    x, y = altura / 2, largura / 2
    rotacao_matriz = cv2.getRotationMatrix2D((y, x), angulo, 1.0)
    coseno = np.abs(rotacao_matriz[0][0])
    seno = np.abs(rotacao_matriz[0][1])
    nova_altura = int((altura * seno) + largura * coseno)
    nova_largura = int((altura * coseno) + largura * seno)

    rotacao_matriz[0][2] += (nova_largura / 2) - x
    rotacao_matriz[1][2] += (nova_altura / 2) - y

    rotacionando_image = cv2.warpAffine(rotacao_image, rotacao_matriz, (nova_largura, nova_altura))
    return rotacionando_image

# Carregar a imagem
imagem_usuario = cv2.imread("usuario.png", 1)

# Realizar as rotações
Normal = Simples(imagem_usuario, 40)
Rotacao_Detalhada = complexo(imagem_usuario, 40)


# Converter as imagens para o formato suportado pelo Tkinter
imagem_normal = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(imagem_usuario, cv2.COLOR_BGR2RGB)))
imagem_rotacao_simples = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(Normal, cv2.COLOR_BGR2RGB)))
imagem_rotacao_detalhada = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(Rotacao_Detalhada, cv2.COLOR_BGR2RGB)))

# Exibir as imagens em labels
lbl_imagem_normal = tk.Label(crud, image=imagem_normal)
lbl_imagem_normal.pack()

lbl_imagem_rotacao_simples = tk.Label(crud, image=imagem_rotacao_simples)
lbl_imagem_rotacao_simples.pack()
