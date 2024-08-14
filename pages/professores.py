import sqlite3
import pandas as pd
import streamlit as st
from pathlib import Path
import os
import time
# Definições de caminho
ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR /'..'/ 'databases' / DB_NAME

def tabela_professores():
    try:
        
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute(f' Create table IF NOT EXISTS professores '
                    '('
                            'id_professor INTEGER PRIMARY KEY AUTOINCREMENT,'
                            'id_aluno int,'
                            'id_contrato int,'
                            'quantidade_aula_semana int,'
                            'valor DECIMAL (10,2),'
                            'desconto DECIMAL (10,2),'
                            'FOREIGN KEY (id_aluno) REFERENCES alunos(id_aluno),'
                            'FOREIGN KEY (id_contrato) REFERENCES contratos_aulas(id_contrato)'
                        
                        ');'
        )

        print(f'Tabela criada com sucesso')
        connection.commit()
        
    except Exception as e:
        raise ValueError(f'Erro ao criar a tabela: {e}')


tabela_professores()
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()
query = """
    SELECT
        p.id_professor,
        a.nome AS nome_aluno,
        c.NOME_CONTRATO_AULA AS nome_contrato,
        p.quantidade_aula_semana,
        p.valor,
        p.desconto
    FROM professores p
    LEFT JOIN alunos a ON p.id_aluno = a.id_aluno
    LEFT JOIN contratos_aulas c ON p.id_contrato = c.ID_CONTRATO_AULA;
"""
 


df = pd.read_sql_query(query,conn)
df = df.dropna()

st.dataframe(df)




