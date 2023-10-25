#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importações
import sqlite3
from datetime import datetime, timedelta, date

# ========== Conectando ao BD ==========
try:
    con = sqlite3.connect('cadastros.db')
    print('Conexao com banco de dados realizado com sucesso!!')
except sqlite3.Error as e:
    print("Erro ao conectar com o Banco de Dados!!", e)


# ========== Tabela de Produtos ==========
# Inserindo Produtos
def criar_produto(i):
    try:
        with con:
            cursor = con.cursor()
            query = "INSERT INTO produtos (codigo, nome, descricao, valor, quantidade, data_fabricacao, fabricante_nome, unidade) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

            cursor.execute(query, i)
        print("Produto criado com sucesso!")
    except sqlite3.Error as e:
        print("Erro ao criar o Produto:", e)
#criar_produto(['12123131', 'nome', 'descricao', 'valor', 'quantidade', date.today(), 'fabricante_nome', 'unidade'])

# Consultar Produtos
def consultar_produtos():
    lista = []
    try:
        with con:
            cursor = con.cursor()
            query = "SELECT * FROM produtos"
            cursor.execute(query)
            linha = cursor.fetchall()

            for i in linha :
                lista.append(i)

        print("Consulta da tabela Produtos realizada com sucesso!")
        return lista
    except sqlite3.Error as e:
        print("Erro ao consultar a tabela Produtos:", e)
#print(consultar_produtos())

# Atualizar Produto
def atualizar_produto(i):
    try:
        with con:
            cursor = con.cursor()
            query = "UPDATE produtos SET nome=?, descricao=?, valor=?, quantidade=?, data_fabricacao=?, fabricante_nome=?, unidade=? WHERE codigo=?"
            cursor.execute(query, i)
        print("Produto atualizado com sucesso!")
    except sqlite3.Error as e:
        print("Erro ao atualizar o Produto:", e)
#atualizar_produto(['1211', 'nome', 'descricao', 'valor', 'quantidade', date.today(), 'fabricante_nome', 'unidade'])

# Deletar Produto
def deletar_produto(i):
    try:
        with con:
            cursor = con.cursor()
            query = "DELETE FROM produtos WHERE codigo=?"
            cursor.execute(query, i)
        print("Produto deletado com sucesso!")
    except sqlite3.Error as e:
        print("Erro ao deletar o Produto:", e)
#deletar_produto([1])

# ========== Tabela de Fabricantes ==========
# Inserindo Fabricante
def criar_fabricante(i):
    try:
        with con:
            cursor = con.cursor()
            query = "INSERT INTO fabricantes (cnpj, nome, endereco, cidade, uf, telefone, representante, data_cadastro, categoria, email) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

            cursor.execute(query, i)
        print("Fabricante criado com sucesso!")
    except sqlite3.Error as e:
        print("Erro ao criar o Fabricante:", e)
#criar_fabricante([])

# Consultar Fabricantes
def consultar_fabricantes():
    lista = []
    try:
        with con:
            cursor = con.cursor()
            query = "SELECT * FROM fabricantes"
            cursor.execute(query)
            linha = cursor.fetchall()

            for i in linha :
                lista.append(i)

        print("Consulta a tabela Fabricantes realizada com sucesso!")
        return lista
    except sqlite3.Error as e:
        print("Erro ao consultar a tabela Fabricantes:", e)
#print(consultar_fabricantes())

# Atualizar Fabricante
def atualizar_fabricante(i):
    try:
        with con:
            cursor = con.cursor()
            query = "UPDATE fabricantes SET nome=?, endereco=?, cidade=?, uf=?, telefone=?, representante=?, data_cadastro=?, categoria=?, email=? WHERE cnpj=?"
            cursor.execute(query, i)
        print("Fabricante atualizado com sucesso!")
    except sqlite3.Error as e:
        print("Erro ao atualizar a Fabricante:", e)
#atualizar_fabricante([])

# Deletar Fabricante
def deletar_fabricante(i):
    try:
        with con:
            cursor = con.cursor()
            query = "DELETE FROM fabricantes WHERE cnpj=?"
            cursor.execute(query, i)
        print("Fabricante deletado com sucesso!")
    except sqlite3.Error as e:
        print("Erro ao deletar o Fabricante:", e)
#deletar_fabricante([])

