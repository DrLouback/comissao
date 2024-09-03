import streamlit as st
import sqlite3
import pandas as pd
import os
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR /'databases' / DB_NAME

col1, col2, col3 = st.columns(3)

st.page_link('pages/contratos.py',label='Contratos')
st.page_link('pages/professores.py',label='Professores')
st.page_link('pages/Turmas.py',label='Turmas')