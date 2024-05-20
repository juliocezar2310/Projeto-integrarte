import os
import pandas as pd
from tkinter import * 
from Componentes import textos_predefinidos, radio_buttons


def pagina(window):

    # Variáveis de Entrada, funcionam Inputs de texto
    ano = Entry(window)
    ano.place(x=50 + 230,y=114.5)
    mes = Entry(window)
    mes.place(x=50 + 230,y=174.5)
    
    label_ano = Label(window, text="Ano:", font="times 12")
    label_ano.place(x=20 + 230, y=95)
    
    label_mes = Label(window, text="Mês:", font="times 12")
    label_mes.place(x=20 + 230, y=155)
       
    #
    def gerar_relatorio(ano, mes):
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
            
        df.to_excel(f'Registros Mensais/{ano}/{mes_selecionado}/Relatório Mensal {mes_selecionado}.xlsx', index=False)


                
    botao_registro = Button(window, text='Registrar', command = lambda : gerar_relatorio(ano.get(), mes.get()))
    botao_registro.place(x=425,y=435)
