import pandas as pd
from datetime import date
import os

class Registro:
    def __init__(self):
        self.fluxo = None
        self.tipo_transacao = None
        self.titulo = None
        self.nome_beneficiario = None
        self.tipo_transacao = None
        self.valor = None
        self.nome_arquivo = None
        self.diretorio_mensal = None
        self.cria_diretorios()


    def cria_diretorios(self):
        mes_numerico = date.today().month
        meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
        mes = meses[mes_numerico - 1]
        if not os.path.exists('Registros Mensais/2024'):
            os.mkdir('Registros Mensais/2024')
        if not os.path.exists(f'Registros Mensais/2024/{mes}'):
            os.mkdir(f'Registros Mensais/2024/{mes}')
        self.diretorio_mensal = f'Registros Mensais/2024/{mes}'
    
    def validar_dados(self, fluxo, tipo_transacao, titulo, nome_beneficiario, valor):
        self.fluxo = fluxo
        self.tipo_transacao = tipo_transacao
        self.titulo = titulo
        self.nome_beneficiario = nome_beneficiario
        self.tipo_transacao = tipo_transacao
        if isinstance(valor, int) or isinstance(valor, float):
            self.valor = valor

    def verificar_registros_do_dia(self):
        dia_atual = date.today().day
        nome_arquivo = f'{self.diretorio_mensal}/registro_integrarte_dia_{dia_atual}.csv'
        self.nome_arquivo = nome_arquivo
        if date.today().day < 10:
            dia_atual = "0" + str(dia_atual) 
        
        if not os.path.exists(nome_arquivo):
            registro_limpo = pd.DataFrame(columns=["fluxo", "tipo_transacao", "titulo", "nome_beneficiario", "valor"])
            registro_limpo.to_csv(nome_arquivo, index=False)
        registro = pd.read_csv(nome_arquivo, )
        return registro

    def salvar_registro(self, df):
        arquivofinal = self.verificar_registros_do_dia()
        dados = pd.concat([arquivofinal, df], ignore_index=True)
        dados.to_csv(self.nome_arquivo, index=False)

    # def relatorio_mensal(self):

    
    def novo_registro(self, fluxo, tipo_transacao, titulo, nome_beneficiario, valor):
        self.validar_dados(fluxo, tipo_transacao, titulo, nome_beneficiario, valor)

        if(self.fluxo != "Entrada"):
            print("nome_beneficiario", self.nome_beneficiario)
            print("titulo", self.titulo)
            if self.titulo != "" and self.nome_beneficiario == "":
                print("tudo, menos adicional")
                self.nome_beneficiario = 'Integrarte'
            else: 
                self.titulo = self.nome_beneficiario
                self.nome_beneficiario = 'Integrarte'

        dados_dict = {"fluxo": self.fluxo, "tipo_transacao": self.tipo_transacao, "titulo": self.titulo, "nome_beneficiario": self.nome_beneficiario, "valor": self.valor}
        dados_df = pd.DataFrame([dados_dict])

        self.salvar_registro(dados_df)

        arquivofinal = pd.read_csv('registro_integrarte.csv')

        dados = pd.concat([arquivofinal, dados_df], ignore_index=True)

        dados.to_csv('registro_integrarte.csv', index=False)
        
        
