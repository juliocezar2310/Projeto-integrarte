from tkinter import * 
from Componentes import textos_predefinidos, radio_buttons_saida, radio_buttons_tipo_transacao
from Registro import Registro
# from Pagina import Pagina
import pandas as pd

registro = Registro()

def pagina(window):

    # botao_home = Button(window, text='Registrar', command = lambda: main.pagina(window))
    # botao_home.place(x=15,y=30)
    # Variaveis cujos valores serão definidos por RadioButtons 

    titulo_value = StringVar(window, "0")
    tipo_transacao = StringVar(window, "0")

    # Variáveis de Entrada, funcionam Inputs de texto
    entrada_titulo = Entry(window)
    entrada_titulo.place(x=190,y=180)
    valor = Entry(window)
    valor.place(x=390,y=180)
    entrada_opcional = Entry(window)


    # Posiciona os textos em suas devidas posições
    textos_predefinidos(window, 'Saída')

    # Posiciona os RadioButtons em suas devidas posições
    radio_buttons_saida(window, titulo_value, entrada_opcional )
    radio_buttons_tipo_transacao(window, tipo_transacao)



    # Após registrar os dados em um csv, ele vai limpar os campos, para que o usuário possa realizar seu próximo registro
    def limpa_campos():
        tipo_transacao.set(None)
        titulo_value.set(None)
        entrada_titulo.delete(0, 'end')
        entrada_opcional.delete(0, 'end')
        valor.delete(0, 'end')
        
       

                
    botao_registro = Button(window, text='Registrar', command = lambda: (registro.novo_registro("Saída", tipo_transacao.get(), titulo_value.get(), entrada_opcional.get(), float(valor.get())), limpa_campos()))
    botao_registro.place(x=425,y=435)


