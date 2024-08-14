import streamlit as st
import sqlite3
from pathlib import Path
import pandas as pd
from datetime import datetime

ROOT_DIR = Path(__file__).parent
DB_FILE = ROOT_DIR/'..'/'databases'/'db.sqlite3'

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

def tabela_turmas():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
                   create table if not exists turmas (
                   id_turma integer PRIMARY KEY,
                   horario varchar (5),
                   dia_semana varchar (20),
                   vagas int, 
                   modalidade varchar (15),
                   id_professor int,
                   FOREIGN KEY (id_professor) REFERENCES professores(id_professor)
                   );
                   """)
    conn.commit()
    conn.close()

def tabela_alunos_turmas():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
                   create table if not exists alunos_turmas (
                   id_turma int,
                   id_aluno int,
                   PRIMARY KEY (id_turma, id_aluno),
                   FOREIGN KEY (id_turma) REFERENCES turmas(id_turma),
                   FOREIGN KEY (id_aluno) REFERENCES alunos(id_aluno)
                   );
                   """)
    conn.commit()
    conn.close()


tabela_turmas()
tabela_alunos_turmas()

dias= ['Segunda-feira','Terça-feira','Quarta-feira','Quinta-feira','Sexta-feira']
horários= ['06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00']
query = 'Select * from turmas'
df = pd.read_sql_query(query,conn)


st.title('Turmas')
cadastro = st.empty()
with cadastro:
    col1, col2, col3, col4 = st.columns(4)
   
with col1:
        horario = st.selectbox('Horário', horários,)
with col2:
        dia = st.selectbox('Dia', dias)
with col3:
        vagas = st.number_input('Vagas')
with col4:
        dia = st.selectbox('Dia', dias)
with col4:
        dia = st.selectbox('Dia', dias)
#st.dataframe(df, hide_index=True, use_container_width=True)