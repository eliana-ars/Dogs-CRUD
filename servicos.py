from tkinter import *

# Importação da biblioteca para edeição de imagens
from PIL import Image, ImageTk
servicos = Tk()
import subprocess

#Configurações da tela
servicos.title("Dogin's")

servicos.resizable(False, False)

width_screen = servicos.winfo_screenwidth()
height_screen = servicos.winfo_screenheight()

width = 870
height = 570

posx = (width_screen / 2) - (width / 2)
posy = (height_screen / 2) - (height / 2)

servicos.maxsize(width, height)
servicos.minsize(width, height)

servicos.geometry("%dx%d+%d+%d" % (width, height, posx, posy))
servicos.configure(bg='#fff')

# foto "logo" e Label para guardar a imagem Logo
fotoOriginal = Image.open("imgs/logo.png")
fotoResize = fotoOriginal.resize((150, 30))
fotoLogo = ImageTk.PhotoImage(fotoResize)
test = Label(servicos, bg="#FFFFFF", image=fotoLogo).place(x=80, y=30)

# escrita "servicos"
lbl_servicos = Label(servicos, text="Cadastro de Serviços", bg="#FFF", font=(
    "Helvetica 14 bold")).place(relx=.45, rely=.200, anchor="center")
fotoOriginal = Image.open("imgs/coracao.png")
fotoResize = fotoOriginal.resize((15, 13))
fotoCoracao = ImageTk.PhotoImage(fotoResize)
coracao = Label(servicos, bg="#FFF", image=fotoCoracao).place(relx=.60, rely=.200, anchor="e")

# botao voltar ao menu
def abrir_tela_menu():
    subprocess.run(["python", "menu.py"])
btn_menu = Button(servicos, text="Voltar ao menu", bd=0, bg="#FFF", fg="#777777", font="Helvetica 10 underline", activebackground="#FFFFFF", activeforeground="#777", command=abrir_tela_menu)
btn_menu.place(x=700, y=40)

#text "Nome do Dono " e caixa de texto "Nome do dono"
lbl_nome = Label(servicos, bg="#FFF", text="Nome do dono",font="Helvetica 10").place(x=200, y=150)
text_nome = Entry(servicos, width=30).place(x=200, y=180)

#text "Escolha o pet" e text "Escolha o pet" e 
lbl_pet = Label(servicos, bg="#FFF", text="Escolha o pet",font="Helvetica 10").place(x=200, y=220)
text_pet = Entry(servicos, width=30).place(x=200, y=250)

# text "Data" e vcaixa de texto "Data"
lbl_data = Label(servicos, bg="#FFF", text="Data",font="Helvetica 10").place(x=200, y=300)
text_data = Entry(servicos, width=15).place(x=200, y=330)

# text "Hora" e caixa de texto "UF"
lbl_hora = Label(servicos, bg="#FFF", text="Hora",font="Helvetica 10").place(x=370, y=300)
text_hora = Entry(servicos, width=10).place(x=370, y=330)

#Checkbutton's
def vacinacaoClicado():
    esp = str(vvacinacao.get())
    print("Vacimação:"+esp)

def banhoClicado():
    esp = str(vbanho.get())
    print("Banho:"+esp)

def tosaClicado():
    esp = str(vtosa.get())
    print("Tosa:"+esp)

def limpezaClicado():
    esp = str(vlimpeza.get())
    print("Tosa:"+esp)


#text "Escolha Serviços"
lbl_pet = Label(servicos, bg="#FFF", text="Escolha os serviços",font="Helvetica 10").place(x=480, y=200)

vvacinacao = IntVar()
vbanho = IntVar()
vtosa = IntVar()
vlimpeza = IntVar()

fr_quadrado1 = Frame(servicos, borderwidth=1, relief="groove",bg="#FFFFFF")
fr_quadrado1.place(x=470, y=230, width=200, height=100)

cb_vacinacao = Checkbutton(fr_quadrado1, text="Vacicao",variable=vacinacaoClicado,onvalue=0, offvalue="n",command=vacinacaoClicado)
cb_vacinacao.pack(side=TOP)

cb_vbanho = Checkbutton(fr_quadrado1, text="Banho",bg="#FFFFFF",variable=banhoClicado,onvalue=0, offvalue="n",command=vacinacaoClicado)
cb_vbanho.pack(side=TOP)

cb_vtosa = Checkbutton(fr_quadrado1, text="Tosa",bg="#FFFFFF",variable=tosaClicado,onvalue=0, offvalue="n",command=vacinacaoClicado)
cb_vtosa.pack(side=TOP)

cb_limpeza = Checkbutton(fr_quadrado1, bg="#FFFFFF",text="Limpeza Dentária",variable=limpezaClicado,onvalue=0, offvalue="n",command=vacinacaoClicado)
cb_limpeza.pack(side=TOP)

#botao "Salvar", "Alterar", "Excluir"
btn_salvar = Button(servicos, width=15, text="Salvar", activebackground="#76bce3", bd=0, bg="#85D3FF",compound=TOP).place(x=250, y=450)
btn_alterar = Button(servicos, width=15, text="Alterar Cliente", bg="#fff", bd=1,compound=TOP).place(x=380, y=450)
btn_excluir = Button(servicos, width=15, text="Excluir Cliente", bg="#fff", bd=1,compound=TOP).place(x=510, y=450)



servicos.mainloop()
