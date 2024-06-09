import pandas as pd
from datetime import date 

class Aluno:
    def __init__(self):
        pass

    def criar_aluno(self, nome_aluno, nome_familiar, cpf, data_nascimento):
        self.nome_aluno = nome_aluno
        self.nome_familiar = nome_familiar
        self.cpf = cpf
        self.data_nascimento = data_nascimento

    def consultar_aluno_existente(self, documento):
        alunos = pd.read_csv('alunos.csv')
        print(documento)
        if str(documento) in (alunos['cpf'].values.astype(str)):
            print('existe')
            return True
        else:
            print('nexiste')
            return False
        
    def consultar_aluno(self, documento):
        alunos = pd.read_csv('alunos.csv')
        aluno = alunos[alunos['cpf'] == float(documento)]
        return aluno
    
    def consultar_pagamentos_aluno(self, documento):
        alunos = pd.read_csv('Registros/Registro Pagamento do Alunos.csv')
        aluno = alunos[alunos['documento'] == float(documento)]
        print('tamnho é ', len(aluno))
        if len(aluno) == 0:
            print(aluno)
            aluno 
            return aluno
        return aluno

        # if str(documento) in (alunos['cpf'].values.astype(str)):

    def salvar_aluno(self):
        registro_alunos = pd.read_csv('alunos.csv')

        if self.cpf not in (registro_alunos['cpf'].values.astype(str)):
            aluno = {'nome aluno': self.nome_aluno, 'nome familiar': self.nome_familiar, 'cpf': self.cpf, 'data nascimento': self.data_nascimento}
            df_aluno = pd.DataFrame([aluno])
            dados = pd.concat([registro_alunos, df_aluno], ignore_index=True)

            dados.to_csv('alunos.csv', index=False)
            print('Aluno adicionado!')
        else:
            print('Aluno já existe!')
    
    def remover_aluno(self, cpf):
        registro_alunos = pd.read_csv('alunos.csv')
        
        registro_alunos = registro_alunos[registro_alunos['cpf'] != float(cpf)] 
        registro_alunos.to_csv('alunos.csv', index=False)

        # planilha = pd.read_excel('Registros/Registro Pagamento do Alunos.xlsx', skiprows=2)
        # df = planilha.fillna(method='ffill')
        # print(df)

        # print('asdfas')
        # print(planilha)
        # print(planilha['MESES'])
        # print(planilha.columns)
        # # Obtém as células mescladas do DataFrame 'df'