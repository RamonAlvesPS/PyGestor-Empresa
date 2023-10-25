#!/usr/bin/env python
# -*- coding: utf-8 -*-

# importando dependencias do Tkinter
from tkinter.ttk import *
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
# tk calendar
from tkcalendar import Calendar, DateEntry
from datetime import date

# importando pillow
from PIL import ImageTk, Image

#importando CRUD
import crud

#importando o screeninfo # para saber o tamanho da tela
from screeninfo import get_monitors

# Obtém as dimensões do monitor principal
monitor = get_monitors()[0]

# Calcula as coordenadas para o centro da tela
largura_janela = 850  # Largura da sua janela
altura_janela = 620   # Altura da sua janela
pos_x = (monitor.width - largura_janela) // 2
pos_y = (monitor.height - altura_janela) // 2


# cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca   
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"   # letra
co6 = "#003452"   # azul
co7 = "#ef5350"   # vermelha

co6 = "#038cfc"   # azul
co8 = "#263238"   # + preta
co9 = "#e9edf5"   # + grey

co10 = "#1b1464"   # azul escuro
co11 = "#0ff2c5"   # + verde
co12 = "#eb008c"   # pink

# Criando janela
janela = Tk()
janela.iconbitmap('./img/icon.ico')
janela.title("By Ramon Alves")

# Define a posição da janela
janela.geometry(f'{largura_janela}x{altura_janela}+{pos_x}+{pos_y}')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
#style.theme_use("alt")
#style.theme_use("default")
style.theme_use("clam")

# Criando Frames
#frame_logo = Frame(janela, width=850, height=52, bg=co6)
frame_logo = Frame(janela, width=850, height=52, bg=co10)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)

frame_dados = Frame(janela, width=850, height=65, bg=co1)
frame_dados.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680)

frame_detalhes = Frame(janela, width=850, height=200, bg=co1)
frame_detalhes.grid(row=4, column=0, pady=0, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=850, height=200, bg=co1)
frame_tabela.grid(row=5, column=0, pady=0, padx=10, sticky=NSEW)

# ========== Frame Logo =========
app_lg = Image.open('./img/Logo.png')
app_lg = app_lg.resize((50, 50))
app_lg = ImageTk.PhotoImage(app_lg)

app_logo = Label(frame_logo, image=app_lg, text=" PyGestor - Empresa", width=850, compound=LEFT, relief=RAISED, anchor=NW, font=('Ivy 20 bold'), bg=co10, fg=co1)
app_logo.place(x=200, y=0)

# ========== Função para cadastrar Produtos ==========
def PRODUTO():
    #função novo produto
    def new_produto():
        codigo = e_codigo_produto.get()
        nome = e_nome_produto.get()
        descricao = e_descricao_produto.get("1.0", "end")
        valor = e_valor_produto.get()
        quantidade = e_quantidade_produto.get()
        data_fabricacao = e_data_fabricacao.get()
        fabricante_nome = e_fabricante_produto.get()
        unidade = c_unidade_produto.get()

        lista = [codigo, nome, descricao, valor, quantidade, data_fabricacao, fabricante_nome, unidade]
        
        try:
            crud.criar_produto(lista)
        except ImportError:
            messagebox.showerror('Erro:', ImportError)

        #Limpando campos
        e_codigo_produto.delete(0,END)
        e_nome_produto.delete(0,END)
        e_descricao_produto.delete("1.0", "end")
        e_valor_produto.delete(0,END)
        e_quantidade_produto.delete(0,END)
        e_data_fabricacao.delete(0,END)
        e_fabricante_produto.delete(0,END)
        c_unidade_produto.delete(0,END)

        controle("Produto")
        mostrar_produtos()
    
    #função atualizar produto
    def update_produto():
        try:
            tree_itens = tree_produto.focus()
            tree_dicionario = tree_produto.item(tree_itens)
            tree_lista = tree_dicionario['values']

            e_codigo_produto.delete(0, END)
            e_codigo_produto.insert(0, tree_lista[0])
            
            e_nome_produto.delete(0,END)
            e_nome_produto.insert(0, tree_lista[1])

            e_descricao_produto.delete("1.0", END)
            e_descricao_produto.insert("1.0", tree_lista[2])

            e_valor_produto.delete(0,END)
            e_valor_produto.insert(0, tree_lista[3])

            e_quantidade_produto.delete(0,END)
            e_quantidade_produto.insert(0, tree_lista[4])

            e_data_fabricacao.delete(0,END)
            e_data_fabricacao.insert(0, tree_lista[5])

            e_fabricante_produto.delete(0,END)
            e_fabricante_produto.insert(0, tree_lista[6])

            c_unidade_produto.delete(0,END)
            c_unidade_produto.insert(0, tree_lista[7])

            def update():
                codigo = e_codigo_produto.get()
                nome = e_nome_produto.get()
                descricao = e_descricao_produto.get("1.0", END)
                valor = e_valor_produto.get()
                quantidade = e_quantidade_produto.get()
                data_fabricacao = e_data_fabricacao.get()
                fabricante_nome = e_fabricante_produto.get()
                unidade = c_unidade_produto.get()

                lista = [codigo, nome, descricao, valor, quantidade, data_fabricacao, fabricante_nome, unidade]
                
                try:
                    crud.atualizar_produto(lista)
                except ImportError:
                    messagebox.showerror('Erro:', ImportError)
                
                #Limpando campos
                e_codigo_produto.delete(0,END)
                e_nome_produto.delete(0,END)
                e_descricao_produto.delete("1.0", END)
                e_valor_produto.delete(0,END)
                e_quantidade_produto.delete(0,END)
                e_data_fabricacao.delete(0,END)
                e_fabricante_produto.delete(0,END)
                c_unidade_produto.delete(0,END)

                mostrar_produtos()

                botao_confirmar_atualizacao.destroy()

            botao_confirmar_atualizacao = Button(frame_detalhes, width=10, command=update, anchor=CENTER, text='Confirmar', overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
            botao_confirmar_atualizacao.place(x=727, y=130)

        except ImportError:
            messagebox.showerror('Erro', 'Selecione um dos produtos na tabela!')
    
    #funcão Deletar produto
    def delete_produto():
        try:
            tree_itens = tree_produto.focus()
            tree_dicionario = tree_produto.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]

            crud.deletar_produto([valor_id])

            mostrar_produtos()
        except ImportError:
            messagebox.showerror('Erro', 'Selecione um produto na tabela!')

    #funcão pesquisar produto
    def select_produto():
        try:
            produto_procurado = e_procurar_produto.get()
            produtos = crud.consultar_produtos()

            for produto in produtos:
                if int(produto[0]) == int(produto_procurado):                 
                    e_codigo_produto.delete(0, END)
                    e_codigo_produto.insert(0, produto[0])
                    
                    e_nome_produto.delete(0,END)
                    e_nome_produto.insert(0, produto[1])

                    e_descricao_produto.delete("1.0",END)
                    e_descricao_produto.insert("1.0", produto[2])

                    e_valor_produto.delete(0,END)
                    e_valor_produto.insert(0, produto[3])

                    e_quantidade_produto.delete(0,END)
                    e_quantidade_produto.insert(0, produto[4])

                    e_data_fabricacao.delete(0,END)
                    e_data_fabricacao.insert(0, produto[5])

                    e_fabricante_produto.delete(0,END)
                    e_fabricante_produto.insert(0, produto[6])

                    c_unidade_produto.delete(0,END)
                    c_unidade_produto.insert(0, produto[7])

                    return
        except ImportError:
            messagebox.showerror('Erro', 'Produto não encontrado!')
        
        mostrar_produtos()
    
    #funcão visualizar produto
    def view_produto():
        try:
            tree_itens = tree_produto.focus()
            tree_dicionario = tree_produto.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]

            e_codigo_produto.delete(0, END)
            e_codigo_produto.insert(0, valor_id)
            
            e_nome_produto.delete(0,END)
            e_nome_produto.insert(0, tree_lista[1])

            e_descricao_produto.delete("1.0",END)
            e_descricao_produto.insert("1.0", tree_lista[2])

            e_valor_produto.delete(0,END)
            e_valor_produto.insert(0, tree_lista[3])

            e_quantidade_produto.delete(0,END)
            e_quantidade_produto.insert(0, tree_lista[4])

            e_data_fabricacao.delete(0,END)
            e_data_fabricacao.insert(0, tree_lista[5])

            e_fabricante_produto.delete(0,END)
            e_fabricante_produto.insert(0, tree_lista[6])

            c_unidade_produto.delete(0,END)
            c_unidade_produto.insert(0, tree_lista[7])

        except ImportError:
            messagebox.showerror('Erro', 'Selecione um dos produtos na tabela!')

    # Criando campos de entrada
    #Nome Produto
    l_nome_produto = Label(frame_detalhes, text="Produto: *", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    l_nome_produto.place(x=3, y=10)
    e_nome_produto = Entry(frame_detalhes, width=28, justify='left', relief='solid')
    e_nome_produto.place(x=6, y=35)
    
    #Descrição
    l_descricao_produto = Label(frame_detalhes, text="Descrição: *", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    l_descricao_produto.place(x=3, y=70)
    e_descricao_produto = Text(frame_detalhes, width=22, height=4, relief='solid')
    e_descricao_produto.place(x=6, y=95)
    #e_descricao_produto = Entry(frame_detalhes, width=25, justify='left', relief='solid')
    #e_descricao_produto.place(x=6, y=95)

    #Código
    l_codigo_produto = Label(frame_detalhes, text="Código: *", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    l_codigo_produto.place(x=236, y=10)
    e_codigo_produto = Entry(frame_detalhes, width=23, justify='left', relief='solid')
    e_codigo_produto.place(x=239, y=35)

    #Valor
    l_valor_produto = Label(frame_detalhes, text="Valor: *", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    l_valor_produto.place(x=236, y=70)
    e_valor_produto = Entry(frame_detalhes, width=23, justify='left', relief='solid')
    e_valor_produto.place(x=239, y=95)

    #Quantidade
    l_quantidade_produto = Label(frame_detalhes, text="Quantidade: *", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    l_quantidade_produto.place(x=236, y=130)
    e_quantidade_produto = Entry(frame_detalhes, width=23, justify='left', relief='solid')
    e_quantidade_produto.place(x=239, y=155)

    #data de Fabricação
    l_data_fabricacao = Label(frame_detalhes, text="Data de Fabricação *", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    l_data_fabricacao.place(x=433, y=10)
    e_data_fabricacao = Entry(frame_detalhes, width=18, justify='left', relief='solid')
    #e_data_fabricacao = DateEntry(frame_detalhes, width=16, backgroud='darkblue', foreground='white', bordewidth=1, year=2023)
    e_data_fabricacao.place(x=436, y=35)

    #Fabricante do Produto
    #pegando os Fabricantes
    #fabricantes = ["Isis", "Nestlé", "Ambev", "BRF", "JBS", "3 Corações", "Yoki"]

    lista_fabricantes = crud.consultar_fabricantes()
    fabricantes = []

    for fabricante in lista_fabricantes:
        fabricantes.append(fabricante[1])
    
    fabricante = []
    for i in fabricantes:
        fabricante.append(i)

    l_fabricante_produto = Label(frame_detalhes, text="Fabricante: *", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    l_fabricante_produto.place(x=433, y=70)
    e_fabricante_produto = ttk.Combobox(frame_detalhes, width=16, font=('Ivy 9 bold'))
    e_fabricante_produto['values'] = (fabricante)
    e_fabricante_produto.place(x=436, y=95)

    #Unidade
    #pegando os tipo
    unidades = ["Uni", "Kg", "g", "m", "m²", "l", "ml"]
    unidade = []
    for i in unidades:
        unidade.append(i)

    l_unidade_produto = Label(frame_detalhes, text="Unidade: *", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    l_unidade_produto.place(x=433, y=130)
    c_unidade_produto = ttk.Combobox(frame_detalhes, width=16, font=('Ivy 9 bold'))
    c_unidade_produto['values'] = (unidade)
    c_unidade_produto.place(x=436, y=155)

    # Linha separatória
    l_linha = Label(frame_detalhes, relief=GROOVE, text='I', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co0, fg=co0)
    l_linha.place(x=602, y=10)
    l_linha = Label(frame_detalhes, relief=GROOVE, text='I', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co1, fg=co0)
    l_linha.place(x=600, y=10)

    #Procurar Produto
    l_procurar_produto = Label(frame_detalhes, text="Procurar Produto: [Cód.]", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    l_procurar_produto.place(x=613, y=10)
    e_procurar_produto = Entry(frame_detalhes, width=16, justify='center', relief='solid')
    e_procurar_produto.place(x=616, y=35)

    img_botao_procurar_produto = Image.open("./img/search.png")
    img_botao_procurar_produto = img_botao_procurar_produto.resize((20, 20))
    img_botao_procurar_produto = ImageTk.PhotoImage(img_botao_procurar_produto)

    botao_procurar_produto = Button(frame_detalhes, anchor=CENTER, command=select_produto, text='Procurar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0)
    botao_procurar_produto.place(x=753, y=33)

    #Botões
    botao_salvar = Button(frame_detalhes, anchor=CENTER, command=new_produto, text='Salvar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
    botao_salvar.place(x=627, y=100)

    botao_atualizar = Button(frame_detalhes, anchor=CENTER, command=update_produto, text='Atualizar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co6, fg=co1)
    botao_atualizar.place(x=627, y=130)

    botao_deletar = Button(frame_detalhes, anchor=CENTER, command=delete_produto, text='Deletar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co7, fg=co1)
    botao_deletar.place(x=627, y=160)

    botao_ver = Button(frame_detalhes, anchor=CENTER, command=view_produto, text='Ver'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0)
    botao_ver.place(x=727, y=160)

    # Tabela Produtos
    def mostrar_produtos():
        app_nome = Label(frame_tabela, text="Lista de Produtos", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 12 bold'), bg=co1, fg=co10)
        app_nome.grid(row=0, column=0, padx=9, pady=3, sticky=NSEW)

        # creating a treeview with dual scrollbars
        list_header = ['Cód', 'Nome', 'Descricao', 'Valor', 'Quant', 'Data de fabricacao', 'Fabricante', 'Unidade']

        df_list = crud.consultar_produtos()

        global tree_produto

        tree_produto = ttk.Treeview(frame_tabela, selectmode="extended",columns=list_header, show="headings")

        # vertical scrollbar
        vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_produto.yview)
        # horizontal scrollbar
        hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_produto.xview)

        tree_produto.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_produto.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tabela.grid_rowconfigure(0, weight=12)

        hd=["nw","center","center","center","center","center","center","center"]
        h=[60,130,160,70,50,140,130,70]
        n=0

        for col in list_header:
            tree_produto.heading(col, text=col.title(), anchor=NW)
            # adjust the column's width to the header string
            tree_produto.column(col, width=h[n],anchor=hd[n])

            n+=1

        for item in df_list:
            tree_produto.insert('', 'end', values=item)

    mostrar_produtos()

# =========== Função para adicionar cursos e turmas ==========
def FABRICANTE():
    #função novo fabricante
    def new_fabricante():
        cnpj = e_cnpj_fabricante.get()
        nome = e_nome_fabricante.get()
        endereco = e_endereco_fabricante.get()
        cidade = e_cidade_fabricante.get()
        uf = e_uf_fabricante.get()
        telefone = e_telefone_fabricante.get()
        representante = e_representante_fabricante.get()
        data_cadastro = e_data_cadastro_fabricante.get()
        categoria = e_categoria_fabricante.get()
        email = e_email_representante_fabricante.get()

        lista = [cnpj, nome, endereco, cidade, uf, telefone, representante, data_cadastro, categoria, email]
        
        try:
            crud.criar_fabricante(lista)
        except ImportError:
            messagebox.showerror('Erro:', ImportError)

        #Limpando campos
        e_cnpj_fabricante.delete(0,END)
        e_nome_fabricante.delete(0,END)
        e_endereco_fabricante.delete(0,END)
        e_cidade_fabricante.delete(0,END)
        e_uf_fabricante.delete(0,END)
        e_telefone_fabricante.delete(0,END)
        e_representante_fabricante.delete(0,END)
        e_data_cadastro_fabricante.delete(0,END)
        e_categoria_fabricante.delete(0,END)
        e_email_representante_fabricante.delete(0,END)

        controle("Fabricante")
        mostrar_fabricantes()
    
    #função atualizar fabricante
    def update_fabricante():
        try:
            tree_itens = tree_fabricante.focus()
            tree_dicionario = tree_fabricante.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]

            e_cnpj_fabricante.delete(0,END)
            e_cnpj_fabricante.insert(0, valor_id)

            e_nome_fabricante.delete(0,END)
            e_nome_fabricante.insert(0, tree_lista[1])

            e_endereco_fabricante.delete(0,END)
            e_endereco_fabricante.insert(0, tree_lista[2])

            e_cidade_fabricante.delete(0,END)
            e_cidade_fabricante.insert(0, tree_lista[3])

            e_uf_fabricante.delete(0,END)
            e_uf_fabricante.insert(0, tree_lista[4])

            e_telefone_fabricante.delete(0,END)
            e_telefone_fabricante.insert(0, tree_lista[5])

            e_representante_fabricante.delete(0,END)
            e_representante_fabricante.insert(0, tree_lista[6])

            e_data_cadastro_fabricante.delete(0,END)
            e_data_cadastro_fabricante.insert(0, tree_lista[7])

            e_categoria_fabricante.delete(0,END)
            e_categoria_fabricante.insert(0, tree_lista[8])

            e_email_representante_fabricante.delete(0,END)
            e_email_representante_fabricante.insert(0, tree_lista[9])


            def update():
                cnpj = e_cnpj_fabricante.get()
                nome = e_nome_fabricante.get()
                endereco = e_endereco_fabricante.get()
                cidade = e_cidade_fabricante.get()
                uf = e_uf_fabricante.get()
                telefone = e_telefone_fabricante.get()
                representante = e_representante_fabricante.get()
                data_cadastro = e_data_cadastro_fabricante.get()
                categoria = e_categoria_fabricante.get()
                email = e_email_representante_fabricante.get()

                lista = [cnpj, nome, endereco, cidade, uf, telefone, representante, data_cadastro, categoria, email]
                
                try:
                    crud.atualizar_fabricante(lista)
                except ImportError:
                    messagebox.showerror('Erro:', ImportError)
                
                #Limpando campos
                e_cnpj_fabricante.delete(0,END)
                e_nome_fabricante.delete(0,END)
                e_endereco_fabricante.delete(0,END)
                e_cidade_fabricante.delete(0,END)
                e_uf_fabricante.delete(0,END)
                e_telefone_fabricante.delete(0,END)
                e_representante_fabricante.delete(0,END)
                e_data_cadastro_fabricante.delete(0,END)
                e_categoria_fabricante.delete(0,END)
                e_email_representante_fabricante.delete(0,END)

                mostrar_fabricantes()

                botao_confirmar_atualizacao.destroy()

            botao_confirmar_atualizacao = Button(frame_detalhes, width=10, command=update, anchor=CENTER, text='Confirmar', overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
            botao_confirmar_atualizacao.place(x=727, y=130)

        except ImportError:
            messagebox.showerror('Erro', 'Selecione um dos Fabricantes na tabela!')
            
        mostrar_fabricantes()
    
    #funcão Deletar fabricante
    def delete_fabricante():
        try:
            tree_itens = tree_fabricante.focus()
            tree_dicionario = tree_fabricante.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]

            crud.deletar_fabricante([valor_id])

            mostrar_fabricantes()
        except ImportError:
            messagebox.showerror('Erro', 'Selecione um Fabricante na tabela!')

    #funcão pesquisar fabricante
    def select_fabricante():
        try:
            fabricante_procurado = e_procurar_fabricante.get()
            fabricantes = crud.consultar_produtos()

            for fabricante in fabricantes:
                if int(fabricante[0]) == int(fabricante_procurado):                 
                    e_cnpj_fabricante.delete(0,END)
                    e_cnpj_fabricante.insert(0, fabricante[0])

                    e_nome_fabricante.delete(0,END)
                    e_nome_fabricante.insert(0, fabricante[1])

                    e_endereco_fabricante.delete(0,END)
                    e_endereco_fabricante.insert(0, fabricante[2])

                    e_cidade_fabricante.delete(0,END)
                    e_cidade_fabricante.insert(0, fabricante[3])

                    e_uf_fabricante.delete(0,END)
                    e_uf_fabricante.insert(0, fabricante[4])

                    e_telefone_fabricante.delete(0,END)
                    e_telefone_fabricante.insert(0, fabricante[5])

                    e_representante_fabricante.delete(0,END)
                    e_representante_fabricante.insert(0, fabricante[6])

                    e_data_cadastro_fabricante.delete(0,END)
                    e_data_cadastro_fabricante.insert(0, fabricante[7])

                    e_categoria_fabricante.delete(0,END)
                    e_categoria_fabricante.insert(0, fabricante[8])

                    e_email_representante_fabricante.delete(0,END)
                    e_email_representante_fabricante.insert(0, fabricante[9])

                    return
        except ImportError:
            messagebox.showerror('Erro', 'Fabricante não encontrado!')
        
        mostrar_fabricantes()
    
    #funcão visualizar fabricante
    def view_fabricante():
        try:
            tree_itens = tree_fabricante.focus()
            tree_dicionario = tree_fabricante.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]

            e_cnpj_fabricante.delete(0,END)
            e_cnpj_fabricante.insert(0, valor_id)

            e_nome_fabricante.delete(0,END)
            e_nome_fabricante.insert(0, tree_lista[1])

            e_endereco_fabricante.delete(0,END)
            e_endereco_fabricante.insert(0, tree_lista[2])

            e_cidade_fabricante.delete(0,END)
            e_cidade_fabricante.insert(0, tree_lista[3])

            e_uf_fabricante.delete(0,END)
            e_uf_fabricante.insert(0, tree_lista[4])

            e_telefone_fabricante.delete(0,END)
            e_telefone_fabricante.insert(0, tree_lista[5])

            e_representante_fabricante.delete(0,END)
            e_representante_fabricante.insert(0, tree_lista[6])

            e_data_cadastro_fabricante.delete(0,END)
            e_data_cadastro_fabricante.insert(0, tree_lista[7])

            e_categoria_fabricante.delete(0,END)
            e_categoria_fabricante.insert(0, tree_lista[8])

            e_email_representante_fabricante.delete(0,END)
            e_email_representante_fabricante.insert(0, tree_lista[9])

        except ImportError:
            messagebox.showerror('Erro', 'Selecione um dos Fabricantes na tabela!')

    # Criando campos de entrada
    #Nome Fabricante
    l_nome_fabricante = Label(frame_detalhes, text="Fabricante: *", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    l_nome_fabricante.place(x=3, y=10)
    e_nome_fabricante = Entry(frame_detalhes, width=28, justify='left', relief='solid')
    e_nome_fabricante.place(x=6, y=35)
    
    #Endereço
    l_endereco_fabricante = Label(frame_detalhes, text="Endereço: *", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    l_endereco_fabricante.place(x=3, y=70)
    e_endereco_fabricante = Entry(frame_detalhes, width=28, justify='left', relief='solid')
    e_endereco_fabricante.place(x=6, y=95)

    #Cidade
    l_cidade_fabricante = Label(frame_detalhes, text="Cidade: *", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    l_cidade_fabricante.place(x=3, y=130)
    e_cidade_fabricante = Entry(frame_detalhes, width=18, justify='left', relief='solid')
    e_cidade_fabricante.place(x=6, y=155)

    #UF
    l_uf_fabricante = Label(frame_detalhes, text="UF: *", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    l_uf_fabricante.place(x=163, y=130)
    e_uf_fabricante = Entry(frame_detalhes, width=8, justify='left', relief='solid')
    e_uf_fabricante.place(x=166, y=155)

    #CNPJ
    l_cnpj_fabricante = Label(frame_detalhes, text="CNPJ: *".upper(), height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    l_cnpj_fabricante.place(x=236, y=10)
    e_cnpj_fabricante = Entry(frame_detalhes, width=23, justify='left', relief='solid')
    e_cnpj_fabricante.place(x=239, y=35)

    #Telefone
    l_telefone_fabricante = Label(frame_detalhes, text="Telefone: *", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    l_telefone_fabricante.place(x=236, y=70)
    e_telefone_fabricante = Entry(frame_detalhes, width=23, justify='left', relief='solid')
    e_telefone_fabricante.place(x=239, y=95)

    #Representante
    l_representante_fabricante = Label(frame_detalhes, text="Representante: *", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    l_representante_fabricante.place(x=236, y=130)
    e_representante_fabricante = Entry(frame_detalhes, width=23, justify='left', relief='solid')
    e_representante_fabricante.place(x=239, y=155)

    #data do Cadastro
    l_data_cadastro_fabricante = Label(frame_detalhes, text="Data do Cadastro: *", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    l_data_cadastro_fabricante.place(x=433, y=10)
    e_data_cadastro_fabricante = Entry(frame_detalhes, width=18, justify='left', relief='solid')
    #e_data_cadastro_fabricante = DateEntry(frame_detalhes, width=16, backgroud='darkblue', foreground='white', bordewidth=1, year=2023)
    e_data_cadastro_fabricante.place(x=436, y=35)

    #Categoria do Fabricante
    #pegando as Categorias
    categorias = ["Alimentos", "Eletrônicos", "Automóveis"]
    categoria = []
    for i in categorias:
        categoria.append(i)

    l_categoria_fabricante = Label(frame_detalhes, text="Categoria: *", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    l_categoria_fabricante.place(x=433, y=70)
    e_categoria_fabricante = ttk.Combobox(frame_detalhes, width=16, font=('Ivy 9 bold'))
    e_categoria_fabricante['values'] = (categoria)
    e_categoria_fabricante.place(x=436, y=95)

    #Email
    l_email_representante_fabricante = Label(frame_detalhes, text="Email: *", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    l_email_representante_fabricante.place(x=433, y=130)
    e_email_representante_fabricante = Entry(frame_detalhes, width=16, justify='left', relief='solid')
    e_email_representante_fabricante.place(x=436, y=155)

    # Linha separatória
    l_linha = Label(frame_detalhes, relief=GROOVE, text='I', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co0, fg=co0)
    l_linha.place(x=602, y=10)
    l_linha = Label(frame_detalhes, relief=GROOVE, text='I', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co1, fg=co0)
    l_linha.place(x=600, y=10)

    #Procurar Fabricante
    l_procurar_fabricante = Label(frame_detalhes, text="Procurar Fabricante:", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    l_procurar_fabricante.place(x=613, y=10)
    e_procurar_fabricante = Entry(frame_detalhes, width=16, justify='center', relief='solid')
    e_procurar_fabricante.place(x=616, y=35)

    img_botao_procurar_fabricante = Image.open("./img/search.png")
    img_botao_procurar_fabricante = img_botao_procurar_fabricante.resize((20, 20))
    img_botao_procurar_fabricante = ImageTk.PhotoImage(img_botao_procurar_fabricante)

    botao_procurar_fabricante = Button(frame_detalhes, anchor=CENTER, command=select_fabricante, text='Procurar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0)
    botao_procurar_fabricante.place(x=753, y=33)

    #Botões
    botao_salvar = Button(frame_detalhes, anchor=CENTER, command=new_fabricante, text='Salvar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
    botao_salvar.place(x=627, y=100)

    botao_atualizar = Button(frame_detalhes, anchor=CENTER, command=update_fabricante, text='Atualizar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co6, fg=co1)
    botao_atualizar.place(x=627, y=130)

    botao_deletar = Button(frame_detalhes, anchor=CENTER, command=delete_fabricante, text='Deletar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co7, fg=co1)
    botao_deletar.place(x=627, y=160)

    botao_ver = Button(frame_detalhes, anchor=CENTER, command=view_fabricante, text='Ver'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0)
    botao_ver.place(x=727, y=160)

    # Tabela Produtos
    def mostrar_fabricantes():
        app_nome = Label(frame_tabela, text="Lista de Fabricantes", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 12 bold'), bg=co1, fg=co10)
        app_nome.grid(row=0, column=0, padx=9, pady=3, sticky=NSEW)

        # creating a treeview with dual scrollbars
        list_header = ['CNPJ', 'Nome', 'Endereco', 'Cidade', 'UF', 'Telefone', 'Representante', 'Cadastro', 'Categoria', 'Email']

        df_list = crud.consultar_fabricantes()

        global tree_fabricante

        tree_fabricante = ttk.Treeview(frame_tabela, selectmode="extended",columns=list_header, show="headings")

        # vertical scrollbar
        vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_fabricante.yview)
        # horizontal scrollbar
        hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_fabricante.xview)

        tree_fabricante.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_fabricante.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tabela.grid_rowconfigure(0, weight=12)

        hd=["nw","nw","nw","center","center","center","center","center","center", "center"]
        h=[40,160,80,80,35,70,110,100,75,60]
        n=0

        for col in list_header:
            tree_fabricante.heading(col, text=col.title(), anchor=NW)
            # adjust the column's width to the header string
            tree_fabricante.column(col, width=h[n],anchor=hd[n])

            n+=1

        for item in df_list:
            tree_fabricante.insert('', 'end', values=item)

    mostrar_fabricantes()

# =========== Função para salvar ==========
def SALVAR():
    print("Salvo!")

# ========== Função de controle ==========
def controle(i):
    if i == "Produto":
        for widget in frame_detalhes.winfo_children():
            widget.destroy()
        for widget in frame_tabela.winfo_children():
            widget.destroy()
        
        app_produto.config(relief=SUNKEN)
        app_fabricante.config(relief=RAISED)
        PRODUTO() # Chamando a função cadastrar

    if i == "Fabricante":
        for widget in frame_detalhes.winfo_children():
            widget.destroy()
        for widget in frame_tabela.winfo_children():
            widget.destroy()
        
        app_fabricante.config(relief=SUNKEN)
        app_produto.config(relief=RAISED)
        FABRICANTE() # Chamando a função adicionar

    if i == "Salvar":
        for widget in frame_detalhes.winfo_children():
            widget.destroy()
        for widget in frame_tabela.winfo_children():
            widget.destroy()
        salvar() # Chamando a função alunos

# ========== Criando Botões ==========
#Botão produto
app_img_produto = Image.open('./img/product.png')
app_img_produto = app_img_produto.resize((25, 25))
app_img_produto = ImageTk.PhotoImage(app_img_produto)
app_produto = Button(frame_dados, command=lambda:controle('Produto'), image=app_img_produto, text="  Produto".upper(), width=150, compound=LEFT, relief=RIDGE, font=('Ivy 11 '), bg=co1, fg=co0)
app_produto.place(x=10, y=15)

app_produto.bind("<Enter>", app_produto.config(relief=SUNKEN))
app_produto.bind("<Leave>", app_produto.config(relief=RAISED))

#Botão fabricante
app_img_fabricante = Image.open('./img/factory.png')
app_img_fabricante = app_img_fabricante.resize((25, 25))
app_img_fabricante = ImageTk.PhotoImage(app_img_fabricante)
app_fabricante = Button(frame_dados, command=lambda:controle('Fabricante'), image=app_img_fabricante, text="  Fabricante".upper(), width=150, compound=LEFT, relief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_fabricante.place(x=185, y=15)

app_fabricante.bind("<Enter>", app_fabricante.config(relief=SUNKEN))
app_fabricante.bind("<Leave>", app_fabricante.config(relief=RAISED))


# Abrindo
app_produto.config(relief=SUNKEN)
app_fabricante.config(relief=RAISED)
PRODUTO()

# Executando a janela
janela.mainloop()