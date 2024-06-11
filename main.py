from tkinter import * 
import pandas as pd
import view.tela_entrada
import view.tela_saida
import view.tela_planilha_mensal
import view.tela_aluno
import view.tela_cadastro
from PIL import Image, ImageTk

window = Tk()
window.geometry("700x500")


def home():
    global window
    window.destroy()
    window = Tk()
    window.title('Página Principal')
    window.geometry("700x500")

    #coloração do fundo PRINCIPAL
    window.configure(background="#6DC24B")

    #criação da imagem na tela Principal
    img = Image.open('images/fundo.png')
    img = img.resize((350, 500))
    img = ImageTk.PhotoImage(img)
    panel = Label(window, image=img, borderwidth=0)
    panel.image = img
    panel.place(x=350,y=0)

    #CRIAÇÃO DO FRAME
    frame_inicio = Frame(window)

    #coloração do fundo Primário
    frame_inicio.configure(background="white")

    #criação da imagem de logo
    logo = Image.open('images/logo-integrate.JPG')
    logo = logo.resize((278, 128))
    logo = ImageTk.PhotoImage(logo)
    panel1 = Label(frame_inicio, image=logo, borderwidth=0)
    panel1.image = logo
    panel1.place(x=20,y=20)

    btn_pagina_entrada = Button(frame_inicio, text='Registrar Receita',font=("Arial",13), bg="#76ABC8", fg="white", width=16, command=tela_registro_entrada)
    btn_pagina_entrada.place(x=100, y=200)
    btn_pagina_saida = Button(frame_inicio, text='Registrar Despesa',font=("Arial",13), bg="#76ABC8", fg="white", width=16, command=tela_registro_saida)
    btn_pagina_saida.place(x=100, y=260)
    btn_pagina_planilha = Button(frame_inicio, text='Relatório Mensal',font=("Arial",13), bg="#76ABC8", fg="white", width=16, command=tela_relatorio_mensal)
    btn_pagina_planilha.place(x=100, y=320)
    btn_pagina_planilha = Button(frame_inicio, text='Buscar Aluno',font=("Arial",13), bg="#76ABC8", fg="white", width=16, command=tela_buscar_aluno)
    btn_pagina_planilha.place(x=100, y=380)

    frame_inicio.place(relx=0,rely=0,relwidth=0.50,relheight=1)



def tela_registro_entrada():
    global window
    window.destroy()
    window = Tk()
    window.title('Registro de Entrada')
    window.geometry("700x500")

    view.tela_entrada.pagina(window)

    btn_pagina_inicial = Button(window, text='voltar', command=home)
    btn_pagina_inicial.place(x=15, y=10)

def tela_registro_saida():
    global window
    window.destroy()
    window = Tk()
    window.title('Registrar Dados Saída')
    window.geometry("700x500")
    

    view.tela_saida.pagina(window)

    btn_pagina_inicial = Button(window, text='voltar', command=home)
    btn_pagina_inicial.place(x=15, y=10)

def tela_relatorio_mensal():
    global window
    window.destroy()
    window = Tk()
    window.title('Gerador do Relatório Mensal')
    window.geometry("700x500")
    

    view.tela_planilha_mensal.pagina(window)

    btn_pagina_inicial = Button(window, text='voltar', command=home)
    btn_pagina_inicial.place(x=15, y=10)

def tela_buscar_aluno():
    global window
    window.destroy()
    window = Tk()
    window.title('Cadastro aluno')
    window.geometry("700x500")
  
    view.tela_aluno.pagina(window)

    btn_pagina_inicial = Button(window, text='voltar', command=home)
    btn_pagina_inicial.place(x=15, y=10)

    botao_adicionar = Button(window, text='adicionar aluno', command= tela_cadastro_aluno)
    botao_adicionar.place(x=580,y=450)

def tela_cadastro_aluno():
    global window
    window.destroy()
    window = Tk()
    window.title('Cadastro aluno')
    window.geometry("700x500")
  
    view.tela_cadastro.pagina(window)

    btn_pagina_inicial = Button(window, text='voltar', command=tela_buscar_aluno)
    btn_pagina_inicial.place(x=15, y=10)


home()
window.mainloop()