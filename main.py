import sqlite3
from pathlib import Path

ROOT_DIR = Path('__file__').parent
DB_NAME = 'db.sqlite3'
DB_FILE = f'{ROOT_DIR}\\databases\\{DB_NAME}'
TABLE_NAME = 'contratos_aulas'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()


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

def insert_values (nome_contrato,valor,qntd_semana):
    sql = (f'INSERT INTO {TABLE_NAME} (NOME_CONTRATO_AULA, VALOR, QNTD_SEMANA) VALUES (?,?,?)')
    cursor.execute(sql,[nome_contrato,valor,qntd_semana])
    connection.commit()
    
    print(sql)

def delete_contrato (id_contrato_aula, nome_contrato_aula):
    cursor = connection.cursor()
    sql = (f' Delete from {TABLE_NAME} where ID_CONTRATO_AULA = ? OR NOME_CONTRATO_AULA = ?')
    cursor.execute(sql,[id_contrato_aula, nome_contrato_aula])
    connection.commit()

def update_contrato(informação, mudança, id):
    sql = f'UPDATE {TABLE_NAME} SET {informação} = ? WHERE ID_CONTRATO_AULA = ?'
    cursor.execute(sql,[mudança, id])
    connection.commit()

if __name__ == '__main__':
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    criar_tabela()
    insert_values('Mensal 2 aulas por semana',425,2)
    delete_contrato('3','Mensal 2 aulas por semana')
    update_contrato('Valor',240,1)

