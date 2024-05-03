import pandas as pd

class Registro:
    def __init__(self):
        self.fluxo = None
        self.tipo_transacao = None
        self.titulo = None
        self.nome_beneficiario = None
        self.tipo_transacao = None
        self.valor = None

    def limpa_campos(self):
        self.fluxo.set(None)
        self.tipo_transacao.set(None)
        self.titulo.set(None)
        self.entrada_titulo.delete(0, 'end')
        self.entrada_opcional.delete(0, 'end')
        self.valor.delete(0, 'end')
    
    def validar_dados(self, fluxo, tipo_transacao, titulo, nome_beneficiario, valor):
        self.fluxo = fluxo
        self.tipo_transacao = tipo_transacao
        self.titulo = titulo
        self.nome_beneficiario = nome_beneficiario
        self.tipo_transacao = tipo_transacao
        if isinstance(valor, int) or isinstance(valor, float):
            self.valor = valor

    
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

        arquivofinal = pd.read_csv('registro_integrarte.csv')

        dados_dict = {"fluxo": self.fluxo, "tipo_transacao": self.tipo_transacao, "titulo": self.titulo, "nome_beneficiario": self.nome_beneficiario, "valor": self.valor}
        dados_df = pd.DataFrame([dados_dict])
        dados = pd.concat([arquivofinal, dados_df], ignore_index=True)

        dados.to_csv('registro_integrarte.csv', index=False)
        

