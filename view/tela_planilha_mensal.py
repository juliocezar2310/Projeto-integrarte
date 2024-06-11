import os
import pandas as pd
from tkinter import * 
from Componentes import textos_predefinidos, radio_buttons


def pagina(window):

    # Variáveis de Receita, funcionam Inputs de texto
    ano = Entry(window)
    ano.place(x=50 + 230,y=114.5)
    mes = Entry(window)
    mes.place(x=50 + 230,y=174.5)
    
    label_ano = Label(window, text="Ano:", font="times 12")
    label_ano.place(x=20 + 230, y=95)
    
    label_mes = Label(window, text="Mês:", font="times 12")
    label_mes.place(x=20 + 230, y=155)
       
    def gerar_relatorio(ano, mes):
        print(mes, type(mes))
        meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
        mes_selecionado = meses[int(mes) - 1]
        print(mes_selecionado)
        arquivo_anterior = pd.read_csv(f'Registros/{ano}/{meses[int(mes) - 2]}/Relatório Mensal {meses[int(mes) - 2]}.csv')
        arquivos = os.listdir(f'Registros/{ano}/{mes_selecionado}')
        arquivos = [ fname for fname in arquivos if fname.endswith('.csv')]
        print(arquivos)
        df = pd.DataFrame()
        if len(arquivos) > 1:
            df_primario = pd.read_csv(f'Registros/{ano}/{mes_selecionado}/{arquivos[0]}')
            for i in range(len(arquivos)):
                df_secundario = pd.read_csv(f'Registros/{ano}/{mes_selecionado}/{arquivos[i]}')
                df = pd.concat([df, df_secundario], ignore_index=True) 
        else:
                df = pd.read_csv(f'Registros/{ano}/{mes_selecionado}/{arquivos[0]}')

        dados_entrada =  df.query('fluxo == "Receita"')
        dados_saida =  df.query('fluxo == "Despesa"')
        
        entrada_entrato_bancario = dados_entrada.query('tipo_transacao == "Conta Bancária/pix"')['valor'].sum()
        saida_entrato_bancario = dados_saida.query('tipo_transacao == "Conta Bancária/pix"')['valor'].sum()

        entrada_saldo = dados_entrada.query('tipo_transacao == "Dinheiro"')['valor'].sum()
        saida_saldo = dados_saida.query('tipo_transacao == "Dinheiro"')['valor'].sum()

        extrato_bancario_anterior = arquivo_anterior['Extrato Bancario'].iloc[0]
        saldo_anterior = arquivo_anterior['Saldo Total'].iloc[0]

        extrato_bancario_total = extrato_bancario_anterior + (entrada_entrato_bancario - saida_entrato_bancario)
        saldo_total = saldo_anterior + (entrada_saldo - saida_saldo)

        df['Extrato Bancario'] = ''
        df['Saldo Total'] = ''
        df['Extrato Bancario'][0] = extrato_bancario_total
        df['Saldo Total'][0] = saldo_total

        df = df.rename(columns={'fluxo': 'Fluxo','tipo_transacao': 'Tipo da Transação','titulo': 'Titulo','nome_beneficiario': 'Nome do Beneficiario','valor': 'Valor'})

        df.to_excel(f'Registros/{ano}/{mes_selecionado}/Relatório Mensal {mes_selecionado}.xlsx', index=False)
        df.to_csv(f'Registros/{ano}/{mes_selecionado}/Relatório Mensal {mes_selecionado}.csv', index=False, encoding='utf-8')



    botao_registro = Button(window, text='Registrar', command = lambda : gerar_relatorio(ano.get(), mes.get()))
    botao_registro.place(x=425,y=435)
