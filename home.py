import streamlit as st
import sqlite3
import pandas as pd
import os
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR /'databases' / DB_NAME

#Criar connecção

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()
#criar tabela alunos

def tabela_alunos():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        ID_ALUNO INTEGER PRIMARY KEY,
        NOME VARCHAR(100) NOT NULL,
        ID_CONTRATO INTEGER,
        FOREIGN KEY (ID_CONTRATO) REFERENCES contratos_aulas(ID_CONTRATO_AULA)
    );
""")

    conn.commit()
    conn.close()

tabela_alunos()
query = 'Select * from alunos'
df = pd.read_sql_query(query, conn)

st.title('Cadastro de Alunos')
st.data_editor(df,use_container_width= True, hide_index= True)





