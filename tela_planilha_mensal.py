from tkinter import * 
from Componentes import textos_predefinidos, radio_buttons


def pagina(window):

    # Variáveis de Entrada, funcionam Inputs de texto
    ano = Entry(window)
    ano.place(x=100 + 50,y=234.5 + 80 - 180)

    mes = Entry(window)
    mes.place(x=100 + 280,y=234.5 + 80 - 180)
    
    label_ano = Label(window, text="Ano:", font="times 12")
    label_ano.place(x=100 + 20, y=235 + 60 - 180)
    
    label_mes = Label(window, text="Mês:", font="times 12")
    label_mes.place(x=100 + 250, y=235 + 60 - 180)
       
    #
    def gerar_relatorio(ano, mes):
        import os
        import pandas as pd
        meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
        mes_selecionado = meses[int(mes) - 1]
        arquivos = os.listdir(f'Registros Mensais/{ano}/{mes_selecionado}')
        df = pd.DataFrame()

        if len(arquivos) > 1:
            df_primario = pd.read_csv(f'Registros Mensais/{ano}/{mes_selecionado}/{arquivos[0]}')
            for i in range(len(arquivos)):
                df_secundario = pd.read_csv(f'Registros Mensais/{ano}/{mes_selecionado}/{arquivos[i]}')
                df = pd.concat([df, df_secundario], ignore_index=True) 
        else:
                df = pd.read_csv(f'Registros Mensais/{ano}/{mes_selecionado}/{arquivos[0]}')
        soma_entrada = df.query('fluxo == "Entrada"')['valor'].sum()
        soma_saida = df.query('fluxo == "Saída"')['valor'].sum()
        # print(df)
        df['Valor Total de Entrada'] = soma_entrada
        df['Valor Total de Saída'] = soma_saida
        if soma_saida > soma_entrada:
            df['Total Prejuizo'] = soma_saida - soma_entrada
        else: 
            df['Total Lucro'] = soma_entrada - soma_saida
            
        df.to_csv(f'Registros Mensais/{ano}/{mes_selecionado}/Relatório Mensal {mes_selecionado}.csv', index=False)


                
    botao_registro = Button(window, text='Registrar', command = lambda : gerar_relatorio(ano.get(), mes.get()))
    botao_registro.place(x=425,y=435)
