from tkinter import *

# Importação da biblioteca para edeição de imagens
from PIL import Image, ImageTk
clientes = Tk()
import subprocess

# Configurações da tela
clientes.title("Pesquisa Cliente Dogin's")

clientes.resizable(False, False)

width_screen = clientes.winfo_screenwidth()
height_screen = clientes.winfo_screenheight()

width = 1100
height = 700


posx = (width_screen / 2) - (width / 2)
posy = (height_screen / 2) - (height / 2)

clientes.maxsize(width, height)
clientes.minsize(width, height)

clientes.geometry("%dx%d+%d+%d" % (width, height, posx, posy))
clientes.configure(bg='#fff')

#text "Cadastro do Cliente"
lbl_agradecimentos = Label(clientes, text="Cadastro do Cliente", bg="#FFF", font=("Helvetica 14 bold")).place(x=430, y=100)

#foto "logo"
fotoOriginal = Image.open("imgs/logo.png")
fotoResize = fotoOriginal.resize((150, 30))
fotoLogo = ImageTk.PhotoImage(fotoResize)
test = Label(clientes, bg="#FFFFFF", image=fotoLogo).place(x=100, y=40)

#foto "perfil"
fotoOriginal = Image.open("imgs/perfil.png")
fotoResize = fotoOriginal.resize((130, 130))
fotoPerfil = ImageTk.PhotoImage(fotoResize)
Perfil = Label(clientes, bg="#FFFFFF", image=fotoPerfil).place(x=100, y=150)

# botao voltar ao menu
def abrir_tela_menu():
    subprocess.run(["python", "menu.py"])
btn_menu = Button(clientes, text="Voltar ao menu", bd=0, bg="#FFF", fg="#777777", font="Helvetica 10 underline", activebackground="#FFFFFF", activeforeground="#777", command=abrir_tela_menu)
btn_menu.place(x=900, y=40)

# text "Código do Cliente "
lbl_codigoCliente = Label(clientes, bg="#FFF", text="Código do Cliente",font="Helvetica 10").place(x=310, y=150)
text_nome = Entry(clientes, width=30).place(x=310, y=180)

#text "CPF "
lbl_cpf = Label(clientes, bg="#FFF", text="CPF",font="Helvetica 10").place(x=310, y=220)

text_nome = Entry(clientes, width=25).place(x=310, y=250)

#text "Celular "
lbl_celular = Label(clientes, bg="#FFF", text="Celular",font="Helvetica 10").place(x=310, y=290)
text_nome = Entry(clientes, width=21).place(x=310, y=320)

#text "CEP "
lbl_cep = Label(clientes, bg="#FFF", text="CEP",font="Helvetica 10").place(x=310, y=360)
text_nome = Entry(clientes, width=25).place(x=310, y=390)

#text "Bairro"
lbl_bairro = Label(clientes, bg="#FFF", text="Bairro",font="Helvetica 10").place(x=310, y=430)
text_nome = Entry(clientes, width=40).place(x=310, y=460)

#text "Nome"
lbl_nome = Label(clientes, bg="#FFF", text="Nome",font="Helvetica 10").place(x=530, y=150)
text_nome = Entry(clientes, width=30).place(x=530, y=180)

#text "Data de Nascimento "
lbl_dataNascimento = Label(clientes, bg="#FFF", text="Data de nascimento",font="Helvetica 10").place(x=500, y=220)
text_dataNascimento = Entry(clientes, width=25).place(x=500, y=250)

#text "Idade "
lbl_idade = Label(clientes, bg="#FFF", text="Idade",font="Helvetica 10").place(x=670, y=220)
text_idade = Entry(clientes, width=10).place(x=670, y=250)

#text "Telefone "
lbl_telefonev= Label(clientes, bg="#FFF", text="Celular",font="Helvetica 10").place(x=495, y=290)
text_telefone = Entry(clientes, width=21).place(x=495, y=320)

#text "Endereço "
lbl_endereco = Label(clientes, bg="#FFF", text="Endereço",font="Helvetica 10").place(x=500, y=360)
text_endereco = Entry(clientes, width=40).place(x=500, y=390)

#text "Numero "
lbl_numero = Label(clientes, bg="#FFF", text="N°",font="Helvetica 10").place(x=760, y=360)
text_numero = Entry(clientes, width=10).place(x=760, y=390)

#text "Cidade"
lbl_cidade = Label(clientes, bg="#FFF", text="Cidade",font="Helvetica 10").place(x=570, y=430)
text_cidade = Entry(clientes, width=30).place(x=570, y=460)

#text "UF "
lbl_uf = Label(clientes, bg="#FFF", text="UF",font="Helvetica 10").place(x=765, y=430)
text_uf = Entry(clientes, width=10).place(x=765, y=460)

#botao "Salvar", "Alterar", "Excluir"
btn_salvar = Button(clientes, width=15, text="Salvar", activebackground="#76bce3", bd=0, bg="#85D3FF",compound=TOP).place(x=430, y=530)
btn_alterar = Button(clientes, width=15, text="Alterar Cliente", bg="#fff", bd=1,compound=TOP).place(x=550, y=530)
btn_excluir = Button(clientes, width=15, text="Excluir Cliente", bg="#fff", bd=1,compound=TOP).place(x=680, y=530)


clientes.mainloop()