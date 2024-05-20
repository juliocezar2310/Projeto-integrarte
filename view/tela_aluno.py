from tkinter import * 
from Componentes import textos_predefinidos, radio_buttons_entrada, radio_buttons_tipo_transacao
from Registro import Registro 
from Aluno import Aluno 


registro = Registro()
alunos = Aluno()

def pagina(window):

    label_titulo = Label(window, text="Consultar Aluno", font="times 13")
    label_titulo.place(x=228, y=62)

    # Variãveis de Entrada, funcionam Inputs de texto
    entrada_titulo = Entry(window)
    entrada_titulo.place(x=230,y=90)

    def registro_aluno(documento):
        def pagina_registro_aluno(aluno):
            janela_aluno = Tk()
            janela_aluno.title(f'Dados {aluno["nome aluno"].values[0]}')
            janela_aluno.geometry("1200x600")

            canvas = Canvas(janela_aluno)
            canvas.create_line(10, 85, 1000, 85)
            canvas.create_line(10, 130, 1000, 130)


            canvas.create_line(300, 85, 300, 300)
            canvas.create_line(345, 85, 345, 300)
            canvas.create_line(300, 85, 300, 300)
            # canvas.create_line(10, 85, 1000, 85)
            # canvas.create_line(10, 115, 1000, 115)
            canvas.pack(fill=BOTH, expand=1)

            label_titulo = Label(janela_aluno, text="INTEGRARTE - Centro Pró-Integração, Cidadania e Arte", font="times 13")
            label_titulo.place(x=10, y=15)
            cnpj = Label(janela_aluno, text="CNPJ: 04.638.448/0001-96", font="times 13")
            cnpj.place(x=10, y=45)
            
            nome_l = Label(janela_aluno, text="Nome", font="times 13")
            nome_l.place(x=15, y=108)


            nome_l = Label(janela_aluno, text="Ano", font="times 13")
            nome_l.place(x=305, y=108)
            
            nome = Label(janela_aluno, text='Lucas Matheus de Oliveira Ramos Oliveira', font="times 12")
            # nome = Label(janela_aluno, text=aluno["nome aluno"].values[0], font="times 13")
            nome.place(x=15, y=135)
            




        if alunos.consultar_aluno_existente(documento):
            dados_aluno = alunos.consultar_aluno(documento)
            pagina_registro_aluno(dados_aluno)
            

                
    botao_registro = Button(window, text='consultar', command=lambda: registro_aluno(entrada_titulo.get()) )
    botao_registro.place(x=360,y=85)