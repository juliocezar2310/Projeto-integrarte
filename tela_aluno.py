from tkinter import * 
from Componentes import textos_predefinidos, radio_buttons_entrada, radio_buttons_tipo_transacao
from Registro import Registro 


registro = Registro()

def pagina(window):

    label_titulo = Label(window, text="Consultar Aluno", font="times 13")
    label_titulo.place(x=228, y=62)

    # Variãveis de Entrada, funcionam Inputs de texto
    entrada_titulo = Entry(window)
    entrada_titulo.place(x=230,y=90 )
                
    botao_registro = Button(window, text='consultar')
    botao_registro.place(x=360,y=85)

    

