from tkinter import * 
from Registro import Registro 
from Aluno import Aluno 
from PIL import Image, ImageTk


registro = Registro()
alunos = Aluno()

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

def pagina(window):

    #não está sendo utilizado
    # label_titulo = Label(window, text="Consultar Aluno", font="times 13")
    # label_titulo.place(x=228, y=62)

    #criando a tela de fundo com imagem
    fundo = Image.open('images/buscarAluno.jpg')
    fundo = fundo.resize((700, 500))
    fundo = ImageTk.PhotoImage(fundo)
    panel = Label(window, image=fundo, borderwidth=0)
    panel.image = fundo
    panel.place(x=0,y=0)
    
    entrada_titulo = Entry(window) # Variaveis de Entrada, funcionam Inputs de texto
    entrada_titulo.place(x=230,y=180)

    def registro_aluno(documento):
        def pagina_registro_aluno(aluno):
            print(aluno)
            janela_aluno = Tk()
            janela_aluno.title(f'Dados {aluno["nome"].values[0]}')
            janela_aluno.geometry("1200x600")

            canvas = Canvas(janela_aluno)
            canvas.create_line(10, 83, 904, 83) # Linha Principal 1
            canvas.create_line(10, 132, 904, 132) # Linha Principal 2
            canvas.create_line(10, 310, 904, 310) # Linha Principal 3
            
            canvas.create_line(345, 108, 904, 108) # Linha 1 bloco 1
            canvas.create_line(345, 160, 904, 160) # Linha 2 bloco 1

            canvas.create_line(345, 232, 904, 232) # Linha 1 bloco 2
            canvas.create_line(345, 257, 904, 257) # Linha 2 bloco 2
            canvas.create_line(345, 283, 904, 283) # Linha 3 bloco 2

            canvas.create_line(10, 83, 10, 310) # Coluna Principal 1
            canvas.create_line(300, 83, 300, 310) # Coluna Principal 2
            canvas.create_line(345, 83, 345, 310) # Coluna Principal 3

            for i in range(6):
                canvas.create_line(438 + 93 * i, 83, 438 + 93 * i, 160) # Coluna Mês Bloco 1
                canvas.create_line(395 + 93 * i, 110, 395 + 93 * i, 160) # Coluna "valor | data" Bloco 1
                canvas.create_line(438 + 93 * i, 233, 438 + 93 * i, 310) # Coluna Mês Bloco 2
                canvas.create_line(395 + 93 * i, 260, 395 + 93 * i, 310) # Coluna "valor | data" Bloco 2

            canvas.pack(fill=BOTH, expand=1)

            label_titulo = Label(janela_aluno, text="INTEGRARTE - Centro Pró-Integração, Cidadania e Arte", font="times 13")
            label_titulo.place(x=10, y=15)
            cnpj = Label(janela_aluno, text="CNPJ: 04.638.448/0001-96", font="times 13")
            cnpj.place(x=10, y=45)
            
            nome_l = Label(janela_aluno, text="Nome", font="times 13")
            nome_l.place(x=15, y=110)

            nome = Label(janela_aluno, text=aluno["nome"].values[0], wraplength=280, justify='center', anchor='c', font="times 12")
            nome.place(x=15, y=137)

            data_l = Label(janela_aluno, text="Ano", font="times 13")
            data_l.place(x=304, y=110)
            data_v = Label(janela_aluno, text=aluno["ano"].values[0], font="times 13", justify='center')
            data_v.place(x=304, y=137)

            data_l = Label(janela_aluno, text="Meses", font="times 13")
            data_l.place(x=650, y=60)

            a = 0
            const_y = 0
            for mes in meses:
                data_l = Label(janela_aluno, text=mes, font="times 13", width=9)
                data_l.place(x=350 + 93*a, y=84 + const_y)

                valor_contribuicao = 0.0
                data_contribuicao = ' -'
                filtro_mensal = aluno.query(f'mes == "{mes}"')
                if len(filtro_mensal) != 0: # Caso tenha acontecido uma contribuição naquele mês, o valor será armazenado nas variáveis
                    data_contribuicao = str(filtro_mensal['data'][0]).split('-')[2]
                    valor_contribuicao = (filtro_mensal['valor'][0])
                data_v = Label(janela_aluno, text=valor_contribuicao, font="times 13") # Valor de Contribuição naquele mês
                data_v.place(x=355 + 93*a, y=137 + const_y )

                data_v = Label(janela_aluno, text=data_contribuicao, font="times 13") # Valor da Contribuição naquele mês
                data_v.place(x=405 + 93*a, y=137 + const_y )                

                a += 1
                if a == 6:
                    const_y += 150
                    a = 0
            for i in range(6):
                data_v = Label(janela_aluno, text='Valor', font="times 13")
                data_v.place(x=347 + 93 * i, y=110)
                data_v = Label(janela_aluno, text='Data', font="times 13")
                data_v.place(x=398 + 93 * i, y=110)
                data_v = Label(janela_aluno, text='Data', font="times 13")
                data_v.place(x=398 + 93 * i, y=110 + 150)
                data_v = Label(janela_aluno, text='Valor', font="times 13")
                data_v.place(x=347 + 93 * i, y=110 + 150)

        def pagina_aluno_sem_registro():
            janela_aluno = Tk()
            janela_aluno.title('Aluno sem registro!')
            janela_aluno.geometry("420x100")

            label_titulo = Label(janela_aluno, text="O Aluno selecionado não possui registros de pagamento", font="times 13")
            label_titulo.place(x=10, y=15)

            botao_fechar_guia = Button(janela_aluno, text='consultar', command=lambda: janela_aluno.destroy() )
            botao_fechar_guia.place(x=175,y=50)



        if alunos.consultar_aluno_existente(documento):
            dados_aluno = alunos.consultar_pagamentos_aluno(documento)
            print(len(dados_aluno))
            if len(dados_aluno) == 0:
                pagina_aluno_sem_registro()
            else:
                pagina_registro_aluno(dados_aluno)
            

                
    botao_registro = Button(window, text='consultar', command=lambda: registro_aluno(entrada_titulo.get()) )
    botao_registro.place(x=360,y=180)