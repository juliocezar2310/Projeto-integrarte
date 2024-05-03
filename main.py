from tkinter import * 
import pandas as pd
import tela_entrada
import tela_saida
import tela_planilha_mensal

window = Tk()
window.geometry("700x500")

def home():
    global window
    window.destroy()
    window = Tk()
    window.geometry("700x500")
    
    btn_pagina_entrada = Button(window, text='Mudar para Página 1', command=tela_registro_entrada)
    btn_pagina_entrada.place(x=15, y=15)
    btn_pagina_saida = Button(window, text='Mudar para Página 2', command=tela_registro_saida)
    btn_pagina_saida.place(x=15, y=45)
    btn_pagina_planilha = Button(window, text='Mudar para Página 3', command=tela_relatorio_mensal)
    btn_pagina_planilha.place(x=15, y=75)


def tela_registro_entrada():
    global window
    window.destroy()
    window = Tk()
    window.geometry("700x500")

    tela_entrada.pagina(window)

    btn_pagina_inicial = Button(window, text='voltar', command=home)
    btn_pagina_inicial.place(x=15, y=10)

def tela_registro_saida():
    global window
    window.destroy()
    window = Tk()
    window.geometry("700x500")

    tela_saida.pagina(window)

    btn_pagina_inicial = Button(window, text='voltar', command=home)
    btn_pagina_inicial.place(x=15, y=10)

def tela_relatorio_mensal():
    global window
    window.destroy()
    window = Tk()
    window.geometry("700x500")

    tela_planilha_mensal.pagina(window)

    btn_pagina_inicial = Button(window, text='voltar', command=home)
    btn_pagina_inicial.place(x=15, y=10)

# pagina(window)

home()
window.mainloop()