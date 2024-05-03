from tkinter import * 
from Componentes import textos_predefinidos, radio_buttons


def pagina(window):

    titulo_value = StringVar(window, "0")
    tipo_transacao = StringVar(window, "0")
    fluxo = StringVar(window, "0")

    # Variáveis de Entrada, funcionam Inputs de texto
    entrada_titulo = Entry(window)
    entrada_titulo.place(x=72,y=227.5 + 80)
    valor = Entry(window)
    valor.place(x=72,y=257 + 80)
    entrada_opcional = Entry(window)

       
    #
    def gerar_relatorio():
        print()

                
    botao_registro = Button(window, text='Registrar', command = gerar_relatorio)
    botao_registro.place(x=425,y=435)
