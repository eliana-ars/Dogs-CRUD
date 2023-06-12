from tkinter import *
from tkinter import ttk
import mysql.connector as mysql


def exibir_registros():
    conectar = mysql.connect(host="localhost", user="root", password="", database="cadastro")
    cursor = conectar.cursor()
    cursor.execute("SELECT * FROM cadastrar")
    registros = cursor.fetchall()
    conectar.close()

    # Limpar tabela existente
    for row in tabela.get_children():
        tabela.delete(row)

    # Preencher tabela com os registros
    for registro in registros:
        tabela.insert("", "end", values=registro)

# Criação da janela e tabela
janela = Tk()
tabela = ttk.Treeview(janela, columns=("codigo", "peso", "data", "idade", "especie"), show="headings")
tabela.heading("codigo", text="Código")
tabela.heading("peso", text="Peso")
tabela.heading("data", text="Data de Nascimento")
tabela.heading("idade", text="Idade")
tabela.heading("especie", text="Espécie")
tabela.pack()

# Botão para exibir registros
btn_exibir = Button(janela, text="Exibir Registros", command=exibir_registros)
btn_exibir.pack()

janela.mainloop()