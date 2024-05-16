import pandas as pd

class Aluno:
    def __init__(self, nome_aluno, nome_familiar, cpf, data_nascimento):
        self.nome_aluno = nome_aluno
        self.nome_familiar = nome_familiar
        self.cpf = cpf
        self.data_nascimento = data_nascimento

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