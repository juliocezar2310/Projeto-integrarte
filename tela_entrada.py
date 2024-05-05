from tkinter import * 
from Componentes import textos_predefinidos, radio_buttons_entrada, radio_buttons_tipo_transacao
from Registro import Registro 

registro = Registro()

def pagina(window):
    # Variaveis cujos valores serão definidos por RadioButtons 
    titulo_value = StringVar(window, "0")
    tipo_transacao = StringVar(window, "0")
    fluxo = StringVar(window, "0")

    # Variãveis de Entrada, funcionam Inputs de texto
    entrada_titulo = Entry(window)
    entrada_titulo.place(x=72,y=227.5 + 80)
    valor = Entry(window)
    valor.place(x=72,y=257 + 80)
    entrada_opcional = Entry(window)


    # Posiciona os textos em suas devidas posições
    textos_predefinidos(window, "Entrada")

    # Posiciona os RadioButtons em suas devidas posições
    radio_buttons_entrada(window, titulo_value)
    radio_buttons_tipo_transacao(window, tipo_transacao)
    # radio_buttons(window, titulo_value, tipo_transacao, fluxo, entrada_opcional)




    # Após registrar os dados em um csv, ele vai limpar os campos, para que o usuário possa realizar seu próximo registro
    def limpa_campos():
        fluxo.set(None)
        tipo_transacao.set(None)
        titulo_value.set(None)
        entrada_titulo.delete(0, 'end')
        entrada_opcional.delete(0, 'end')
        valor.delete(0, 'end')


                
    botao_registro = Button(window, text='Registrar', command = lambda: (registro.novo_registro("Entrada", tipo_transacao.get(), titulo_value.get(), entrada_titulo.get(), float(valor.get())), limpa_campos()))
    botao_registro.place(x=425,y=435)
