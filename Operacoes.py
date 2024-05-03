class Operacoes:
    def __init__(self):
        self.fluxo = None
        self.tipo_entrada = None
        self.titulo = None
        self.nome_beneficiario = None
        self.valor = None

        def realiza_novo_registro(fluxo, tipo_entrada, titulo, nome_beneficiario, valor):

        if(fluxo != "Entrada"):
            print("nome_beneficiario", nome_beneficiario)
            print("titulo", titulo)
            if titulo != "" and nome_beneficiario == "":
                print("tudo, menos adicional")
                nome_beneficiario = 'Integrarte'
            else: 
                titulo = nome_beneficiario
                nome_beneficiario = 'Integrarte'

        arquivofinal = pd.read_csv('registro_integrarte.csv')

        dados_dict = {"fluxo": fluxo, "tipo_entrada": tipo_entrada, "titulo": titulo, "nome_beneficiario": nome_beneficiario, "valor": valor}
        dados_df = pd.DataFrame([dados_dict])
        dados = pd.concat([arquivofinal, dados_df], ignore_index=True)

        dados.to_csv('registro_integrarte.csv', index=False)
        limpa_campos()
        

