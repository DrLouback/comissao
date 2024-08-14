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

def criar_tabela():
    try:
        
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute(f' Create table IF NOT EXISTS contratos_aulas '
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


criar_tabela()
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()
query = "Select * from contratos_aulas"
 


df = pd.read_sql_query(query,conn)
df = df.dropna()
df_coluna = df.iloc[:,1:4]

def validar_campos(contrato, valor, qntd):
    if not contrato:
        return "O nome do contrato precisa ser preenchido"
    if valor <= 0:
        return "O valor não pode ser menor ou igual a 0"
    if qntd <= 0:
        return "A quantidade não pode ser menor ou igual a 0"
    return None


column_configuration = {
    "ID_CONTRATO_AULA": st.column_config.TextColumn(
        "ID", help="ID do Contrato", max_chars=100, width="small"
    ),
    "NOME_CONTRATO_AULA": st.column_config.TextColumn(
        "Contrato",
        help="Nome do contrato",
        width="medium",
        
    ),
    "VALOR": st.column_config.NumberColumn(
        "Valor",
        help="Valor do contrato",
        width="small",
       
    ),
    "QNTD_SEMANA": st.column_config.NumberColumn(
        "Vezes na semana",
        help= "Vezes na semana",
        width='small'
    )
}


st.title('Contratos')
col1, col2, col3, col4 = st.columns([2,1,1,1], vertical_alignment= 'bottom')
event = st.dataframe(df_coluna, use_container_width=True, hide_index=True, column_config= column_configuration, on_select='rerun' , selection_mode='multi-row') 
with col1:
    contrato = st.text_input('Nome do contrato')
with col2:
    valor = st.number_input('Valor do contrato', format="%.2f")
with col3:
    qntd = st.number_input('Vezes na semana', format= "%d", value= 0, step= 1)
with col4:
    success_placeholder = st.empty()
    submit_button = st.button("Cadastrar")
    if submit_button:
        mensagem_error = validar_campos(contrato, valor, qntd)
        if mensagem_error:
            st.error(mensagem_error)
        else:
            cursor.execute("""
                            insert into contratos_aulas (ID_CONTRATO_AULA, NOME_CONTRATO_AULA, VALOR, QNTD_SEMANA) 
                            VALUES (?,?,?,?)
                        """, (None,contrato, valor, qntd))
            conn.commit()
            
            
            success_placeholder.success("Contrato cadastrado com sucesso")
            time.sleep(2)
            st.rerun()
         




if event:
    st.header('Contratos selecionados')
    contratos_select = event.selection.rows # type: ignore
    contratos_filtrados = df.iloc[contratos_select]

    ids_deletar = contratos_filtrados['ID_CONTRATO_AULA'].tolist()
    if st.button('Deletar contratos'):
            conn.execute('Delete from contratos_aulas where ID_CONTRATO_AULA in ({})'.format(','.join('?' * len(ids_deletar))),ids_deletar)
            conn.commit()
            df = pd.read_sql_query(query,conn)
            st.success('Contrato Deletado')
            time.sleep(2)
            st.rerun
    
st.dataframe(contratos_filtrados.iloc[:,0:4], column_config= column_configuration, use_container_width= True, hide_index=True)
conn.close()




