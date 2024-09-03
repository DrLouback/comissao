import streamlit as st
import sqlite3
from pathlib import Path
import pandas as pd
from datetime import datetime


ROOT_DIR = Path(__file__).parent
DB_FILE = ROOT_DIR/'..'/'databases'/'db.sqlite3'
st.page_link('home.py',label='Home')
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

def tabela_turmas():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
                   create table if not exists turmas (
                   id_turma integer PRIMARY KEY,
                   modalidade varchar (20),
                   dia_semana varchar (20),
                   horario varchar(5), 
                   id_professor int,
                   vagas int,
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
modalidade = ['Pilates','Funcional','HIIT Pilates']

query_prof = 'select * from professores'
df_prof = pd.read_sql_query(query, conn)
print(df_prof)
df = pd.read_sql_query(query,conn)


st.title('Turmas')
cadastro = st.empty()

col1, col2, col3, col4 = st.columns(4)
with col1:
    modalidade = st.selectbox('Modalidade',modalidade)
with col2:
    dia = st.selectbox('Dia', dias)
with col3:
    hora = st.selectbox('Hora', horários)
with col4:
    professor = st.selectbox('Professor', professores)

criar = st.button('Criar')
if criar:
    tabela_turmas()
    
    cursor.execute("""insert into turmas(id_turma, modalidade, dia_semana, horario, id_professor, vagas) values (?,?,?,?,?,?)"""
                   , (None, modalidade, dia, hora, professor, 1))
    conn.commit()
#st.dataframe(df, hide_index=True, use_container_width=True)