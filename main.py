from tkinter import * 
import pandas as pd
import tela_entrada
import tela_saida
import tela_planilha_mensal
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

    #CRIAÇÃO DO FRAME
    frame_inicio = Frame(window)
    img = Image.open("images/integrarte.jpg")
    img = img.resize((600, 400))
    photo = ImageTk.PhotoImage(img)
    label_imagem = Label(frame_inicio, image=photo)
    label_imagem.image = photo 
    label_imagem.pack()

    img = Image.open('images/logo.JPG')
    img = img.resize((278, 128))
    img = ImageTk.PhotoImage(img)
    panel = Label(frame_inicio, image=img, borderwidth=0)
    label_imagem.img = img
    label_imagem.place(x=-3, y=-3)
    panel.image = img
    panel.pack()

    btn_pagina_entrada = Button(frame_inicio, text='Mudar para Página 1',font=("Arial",13), bg="#FFA500", fg="white", command=tela_registro_entrada)
    btn_pagina_entrada.place(x=214, y=175)
    btn_pagina_saida = Button(frame_inicio, text='Mudar para Página 2',font=("Arial",13), bg="#FFA500", fg="white", command=tela_registro_saida)
    btn_pagina_saida.place(x=214, y=235)
    btn_pagina_planilha = Button(frame_inicio, text='Mudar para Página 3',font=("Arial",13), bg="#FFA500", fg="white", command=tela_relatorio_mensal)
    btn_pagina_planilha.place(x=214, y=295)

    frame_inicio.place(relx=0.076,rely=0.1,relwidth=0.85,relheight=0.8)



def tela_registro_entrada():
    global window
    window.destroy()
    window = Tk()
    window.title('Registro de Entrada')
    window.geometry("700x500")

    tela_entrada.pagina(window)

    btn_pagina_inicial = Button(window, text='voltar', command=home)
    btn_pagina_inicial.place(x=15, y=10)

def tela_registro_saida():
    global window
    window.destroy()
    window = Tk()
    window.title('Registrar Dados Saída')
    window.geometry("700x500")
    

    tela_saida.pagina(window)

    btn_pagina_inicial = Button(window, text='voltar', command=home)
    btn_pagina_inicial.place(x=15, y=10)

def tela_relatorio_mensal():
    global window
    window.destroy()
    window = Tk()
    window.title('Gerador do Relatório Mensal')
    window.geometry("700x500")
    

    tela_planilha_mensal.pagina(window)

    btn_pagina_inicial = Button(window, text='voltar', command=home)
    btn_pagina_inicial.place(x=15, y=10)

home()
window.mainloop()