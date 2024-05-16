from tkinter import * 
from Componentes import textos_predefinidos, radio_buttons_entrada, radio_buttons_tipo_transacao
from Registro import Registro 
from Aluno import Aluno 

registro = Registro()

def pagina(window):

    label_titulo_aluno = Label(window, text="Nome Aluno", font="times 13 ")
    label_titulo_aluno.place(x=12, y=50)

    # Variãveis de Entrada, funcionam Inputs de texto
    entrada_titulo_aluno = Entry(window)
    entrada_titulo_aluno.place(x=14,y=80)

    label_titulo_familiar = Label(window, text="Nome do Familiar", font="times 13")
    label_titulo_familiar.place(x=12, y=110)

    entrada_titulo_familiar = Entry(window)
    entrada_titulo_familiar.place(x=14,y=140)
    
    label_titulo_documento = Label(window, text="Documento (CPF)", font="times 13")
    label_titulo_documento.place(x=12, y=170)

    entrada_titulo_documento = Entry(window)
    entrada_titulo_documento.place(x=14,y=200)

    label_titulo_nascimento = Label(window, text="Data de Nascimento", font="times 13")
    label_titulo_nascimento.place(x=12, y=230)

    entrada_titulo_nascimento = Entry(window)
    entrada_titulo_nascimento.place(x=14,y=260)

    def limpa_campos():
        entrada_titulo_aluno.get().delete(0, 'end')
        entrada_titulo_familiar.get().delete(0, 'end')
        entrada_titulo_documento.get().delete(0, 'end')
        entrada_titulo_nascimento.get().delete(0, 'end')
    
    def criar_aluno(nome_aluno, nome_familiar, documento, data_nascimento):
        aluno = Aluno(nome_aluno, nome_familiar, documento, data_nascimento)
        aluno.salvar_aluno()

        
                
    botao_registro = Button(window, text='criar aluno', command=lambda: criar_aluno(entrada_titulo_aluno.get(), entrada_titulo_familiar.get(), entrada_titulo_documento.get(), entrada_titulo_nascimento.get()))
    botao_registro.place(x=580,y=450)




#nome aluno,nome familiar,cpf,data nascimento