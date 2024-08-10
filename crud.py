import sqlite3
from pathlib import Path

ROOT_DIR = Path('__file__').parent
DB_NAME = 'db.sqlite3'
DB_FILE = f'{ROOT_DIR}\\databases\\{DB_NAME}'
TABLE_NAME = 'contratos_aulas'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

#Criando tabela, se existir ignora
def criar_tabela():
    try:
        

        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute(f' Create table IF NOT EXISTS {TABLE_NAME} '
                    '('
                            'ID_CONTRATO_AULA INTEGER PRIMARY KEY AUTOINCREMENT,'
                            'NOME_CONTRATO_AULA VARCHAR (30),'
                            'VALOR INT NOT NULL,'
                            'QNTD_SEMANA INT NOT NULL'
                        
                        ');'
        )

        print(f'Tabela criada com sucesso')
        connection.commit()
        
    except Exception as e:
        raise ValueError(f'Erro ao criar a tabela: {e}')


def select_contrato():
        try:
            id_contrato = input('Digite o Id: ')
            list_id = []
            if id_contrato:
                sql = (f'Select * from {TABLE_NAME} where ID_CONTRATO_AULA == ?')
                cursor.execute(sql,(id_contrato,))
                resultados = cursor.fetchall()
                list_id.append(id_contrato)
                return list_id
            else: 
                nome_contrato = input('Digite o nome do contrato: ')
                sql = (f'Select * from {TABLE_NAME} where NOME_CONTRATO_AULA = ?')
                cursor.execute(sql,(nome_contrato,))
                resultados = cursor.fetchall()
                for rows in resultados:
                       id_contrato = rows[0]
                       nome_contrato = rows[1]
                       print(id_contrato, nome_contrato)
                       list_id.append(id_contrato)
                return list_id

        except Exception as e:
            raise ValueError(f'Erro para visualizar dados: {e}')
        
#Cadastrando contratos:
def insert_values (nome_contrato,valor,qntd_semana):
    try:
        

        sql = (f'INSERT INTO {TABLE_NAME} (NOME_CONTRATO_AULA, VALOR, QNTD_SEMANA) VALUES (?,?,?)')
        cursor.execute(sql,[nome_contrato,valor,qntd_semana])
        connection.commit()
    except Exception as e:
        raise ValueError(f'Erro ao cadastrar contrato: {e}')


def delete_contrato (id_contrato_aula):
    cursor = connection.cursor()
    sql = (f' Delete from {TABLE_NAME} where ID_CONTRATO_AULA = ?')
    cursor.execute(sql,[id_contrato_aula])
    connection.commit()

def update_contrato(informação, mudança, id):
    sql = f'UPDATE {TABLE_NAME} SET {informação} = ? WHERE ID_CONTRATO_AULA = ?'
    cursor.execute(sql,[mudança, id])
    connection.commit()

def tabela_contratos_aulas():
    while True:
        answer = input('Cadastrar contrato [C]   Deletar Contrato [D]   Mudar Contrato [M]').upper()
        
        if answer == 'C':

            
            cursor.execute(f'Select NOME_CONTRATO_AULA from {TABLE_NAME}')
            resultado = cursor.fetchall()
            lista_contratos = [resultado[0] for resultado in resultado]
        
           
            nome_contrato = input('Digite o nome do contrato: ')
            if nome_contrato in lista_contratos:
                print('Esse contrato já está cadastrado.')
            else:
                valor = input('Digite o valor do contrato: ')
                qntd_semana = input('Digite quantidade de aulas permitidas: ')
                return insert_values(nome_contrato, valor, qntd_semana)

        
        if answer == 'D':
            cursor.execute(f'Select ID_CONTRATO_AULA, NOME_CONTRATO_AULA from {TABLE_NAME}')
            resultado = cursor.fetchall()
            for i in resultado:
                print(*i)
            id_contrato_aula = select_contrato()
            answer = input('Confirma exclusão? [Y] [N]: ').upper()
            if answer == 'Y':
                for id in id_contrato_aula: 
                        delete_contrato(id)
                return print('Deletado com sucesso')
        

        if answer == 'M':

            id = input('Qual ID do contrato que deseja mudar: ')
            informação = input('Qual informação deseja mudar: ')
            mudança = input('Para qual valor deseja mudar: ')
            return update_contrato(informação,mudança,id)
        else: 
            print('Não é um comando válido')
          
            
    


if __name__ == '__main__':
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    criar_tabela()
    tabela_contratos_aulas()

