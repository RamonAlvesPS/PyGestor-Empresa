#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importações
#import os
import sqlite3
from datetime import datetime, timedelta, date

# Conectando ao BD
try:
    con = sqlite3.connect('cadastros.db')
    print('Conexao com banco de dados realizado com sucesso!!')
except sqlite3.Error as e:
    print("Erro ao conectar com o Banco de Dados!!", e)

cursor = con.cursor()

# Criando tabela de fabricantes
try:
    with con:
        cursor = con.cursor()
        cursor.execute(""" CREATE TABLE IF NOT EXISTS fabricantes(
                       cnpj TEXT PRIMARY KEY, 
                       nome TEXT,
                       endereco TEXT,
                       cidade TEXT,
                       uf TEXT,
                       telefone TEXT,
                       representante TEXT,
                       data_cadastro DATA,
                       categoria TEXT,
                       email TEXT
        )""")
        print("Tabela 'fabricantes' criada com sucesso!")
except sqlite3.Error as e:
    print("Erro ao criar a tabela 'fabricantes':", e)

# Criando tabela de produtos
try:
    with con:
        cursor = con.cursor()
        cursor.execute(""" CREATE TABLE IF NOT EXISTS produtos(
                       codigo INTEGER PRIMARY KEY, 
                       nome TEXT,
                       descricao TEXT,
                       valor TEXT, 
                       quantidade TEXT,
                       data_fabricacao DATE,
                       fabricante_nome TEXT,
                       unidade TEXT,
                       FOREIGN KEY (fabricante_nome) REFERENCES fabricantes (nome) ON UPDATE CASCADE ON DELETE CASCADE
        )""")
        print("Tabela 'produtos' criada com sucesso!")
except sqlite3.Error as e:
    print("Erro ao criar a tabela 'produtos':", e)