from tkinter import *

# Importação da biblioteca para edeição de imagens
from PIL import Image, ImageTk
Login = Tk()


# Configurações da tela
Login.title("Pesquisa Cliente Dogin's")

Login.resizable(False, False)

width_screen = Login.winfo_screenwidth()
height_screen = Login.winfo_screenheight()

width = 700
height = 400


posx = (width_screen / 2) - (width / 2)
posy = (height_screen / 2) - (height / 2)

Login.maxsize(width, height)
Login.minsize(width, height)

Login.geometry("%dx%d+%d+%d" % (width, height, posx, posy))
Login.configure(bg='#fff')

# escrita "Faça seu Login"
lbl_agradecimentos = Label(Login, text="Faça seu Login", bg="#FFF", font=(
    "Helvetica 12 bold")).place(x=100, y=60)
fotoOriginal = Image.open("imgs/coracao.png")
fotoResize = fotoOriginal.resize((15, 13))
fotoCoracao = ImageTk.PhotoImage(fotoResize)
coracao = Label(Login, bg="#FFF", image=fotoCoracao).place(x=223, y=65)

# escrita "Usuário"
lbl_usuario = Label(Login, bg="#FFF", text="Usuário",
                    font="Helvetica 10").place(x=100, y=120)
text_nome = Entry(Login, width=40).place(x=100, y=150)

# escrita "Senha"
lbl_usuario = Label(Login, bg="#FFF", text="Senha",
                    font="Helvetica 10").place(x=100, y=200)
text_nome = Entry(Login, width=40).place(x=100, y=230)

# botao "Entrar" 
btn_entrar = Button(Login, width=20, text="Entrar", activebackground="#76bce3", bd=0, bg="#85D3FF",compound=TOP).place(x=150, y=280)

# botao cadastrar clienete
btn_menu = Button(Login, text="Sair da Plataforma", bd=0, bg="#FFF", fg="#777777",
                  font="Helvetica 10 underline", activebackground="#FFF", activeforeground="#777")
btn_menu.place(x=165, y=305)

# foto "logo"
fotoOriginal = Image.open("imgs/logo.png")
fotoResize = fotoOriginal.resize((250, 200))
fotoLogo = ImageTk.PhotoImage(fotoResize)
test = Label(Login, bg="#FFFFFF", image=fotoLogo).place(x=370, y=50)

Login.mainloop()
