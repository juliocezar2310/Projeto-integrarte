from tkinter import * 
import pandas as pd
import tela_entrada
import tela_saida
import tela_planilha_mensal


# Tela do Tkinter
window = Tk()
window.geometry("700x500")
def home(window):
    window.destroy()
    window = Tk()
    window.geometry("700x500")

    btn_pagina_inicial = Button(window, text='Mudar para Página 1', command=lambda: tela_entrada.pagina(window))
    btn_pagina_inicial.place(x=15, y=15)
    btn_pagina_inicial = Button(window, text='Mudar para Página 2', command=lambda: tela_saida.pagina(window))
    btn_pagina_inicial.place(x=15, y=45)
    btn_pagina_inicial = Button(window, text='Mudar para Página 3', command=lambda: tela_planilha_mensal.pagina(window))
    btn_pagina_inicial.place(x=15, y=75)

# pagina(window)

home(window)
window.mainloop()