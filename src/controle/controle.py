import tkinter as tk
from tkinter import messagebox
import sqlite3

from src.modelo.Ambulante import *

# |=======| CONTROLE |=======|
class Controle():
    # ======= MÉTODO LIMPAR TELA (LIMPA OS ENTRYS DO FRAME 02) =======
    def limpa_tela(self):
        self.id_entry.delete(0, tk.END)
        self.nome_entry.delete(0, tk.END)
        self.cpf_entry.delete(0, tk.END)
        self.rg_entry.delete(0, tk.END)
        self.telefone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.cep_entry.delete(0, tk.END)
        self.cidade_entry.delete(0, tk.END)
        self.bairro_entry.delete(0, tk.END)
        self.rua_entry.delete(0, tk.END)
        self.nomeMae_entry.delete(0, tk.END)
        self.dataNascimento_entry.delete(0, tk.END)
        
    # ======= CONECTANDO COM O BANCO DE DADOS =======
    def conecta_bd(self):
        self.conn = sqlite3.connect('cadastro_ambulante.bd')
        self.cursor = self.conn.cursor()
        print('conectando ao banco de dados !')

    # ======= DESCONECTANDO COM O BANCO DE DADOS =======
    def desconecta_bd(self):
        self.conn.close()
        print('desconectando do banco de dados!')

    # ======= MONTANDO AS TABELAS NECESSÁRIAS PARA O BANCO DE DADOS =======
    def montar_tabelas(self):
        self.conecta_bd()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS ambulante(
                id INTEGER PRIMARY KEY,
                nome char(50) NOT NULL,
                cpf char(11) NOT NULL,
                rg char(10) NOT NULL,
                email char(30) NOT NULL,
                telefone INTEGER(20),
                cep char(8) NOT NULL,
                cidade char(30) NOT NULL,
                bairro char(30) NOT NULL,
                rua char(30) NOT NULL,
                atividade char(30) NOT NULL,
                data_nascimento date NOT NULL,
                nome_mae char(50) NOT NULL,
                raca char(30) NOT NULL,
                genero char(30) NOT NULL,
                deficiencia char(3) NOT NULL,
                escolaridade char(30) NOT NULL,
                trabalha char(3) NOT NULL,
                faixa_salarial char(10),
                hora_atualizacao date
            )
                            
            CREATE TABLE IF NOT EXISTS ajudante(
                id_ajudante INTEGER PRIMARY KEY NOT NULL,
                nome_ajudante char(50) NOT NULL,
                cpf_ajudante char(11) NOT NULL,
                data_nascimento date NOT NULL,
                id_ambulante INTEGER FOREIGN KEY NOT NULL
            )
        ''')

        self.conn.commit()
        print('Banco de dados Criado!')
        self.desconecta_bd()

    # |=======| MÉTODOS 'CRUD' |=======|
    # ======= MÉTODO PARA PEGAR TODOS OS ENTRYS =======
    def pegandoEntrysAmbulante(self):
        # ENTRYS:
        self.id             = self.id_entry.get()
        self.nome           = self.nome_entry.get()
        self.cpf            = self.cpf_entry.get()
        self.rg             = self.rg_entry.get()
        self.email          = self.email_entry.get()
        self.telefone       = self.telefone_entry.get()
        self.cep            = self.cep_entry.get()
        self.cidade         = self.cidade_entry.get()
        self.bairro         = self.bairro_entry.get()
        self.rua            = self.rua_entry.get()
        self.nomeMae        = self.nomeMae_entry.get()
        self.dataNascimento = self.dataNascimento_entry.get()

        # TESTE:
        print(self.id, self.nome, self.cpf, self.rg, self.email, self.telefone, self.cep, self.cidade, self.bairro, self.rua, self.nomeMae, self.dataNascimento)

        # OPTION MENU:
        self.atividadeSelecao         = self.atividade_selecao.get()
        self.racaSelecao              = self.raca_selecao.get()
        self.generoSelecao            = self.genero_selecao.get()
        self.possuiDeficienciaSelecao = self.possuiDeficiencia_selecao.get()
        self.escolaridadeSelecao      = self.escolaridade_selecao.get()
        self.possuiTrabalhoSelecao    = self.possuiTrabalho_selecao.get()
        self.faixaSalarialSelecao     = self.faixaSalarial_selecao.get()

        # TESTE:
        print(self.atividadeSelecao, self.racaSelecao, self.generoSelecao, self.possuiDeficienciaSelecao, self.escolaridadeSelecao, self.possuiTrabalhoSelecao, self.faixaSalarialSelecao)

    # ======= MÉTODO DE CADASTRAR O AMBULANTE =======
    def cadastrarAmbulante(self):
        self.pegandoEntrysAmbulante()

        # ======= TRATAR ENTRADA DE TODOS OS DADOS =======
        # CONFERINDO SE TODOS OS DADOS FORAM PREENCHIDOS E SELECIONADOS:
        if((not self.nome) or (not self.cpf) or (not self.rg)  or (not self.email) or (not self.telefone) or (not self.cep)  or 
        (not self.cidade) or (not self.bairro) or (not self.rua) or (not self.nomeMae) or (not self.dataNascimento)):
            messagebox.showinfo('Aviso!', 'Todos os campos devem ser preenchidos!')
            return
        elif((self.atividadeSelecao == 'Escolha') or (self.racaSelecao == 'Escolha a raca') or (self.generoSelecao == 'Escolha o gênero') or 
        (self.escolaridadeSelecao == 'Escolha') or self.faixaSalarialSelecao == 'Escolha'):
            messagebox.showinfo('Aviso!', 'Deve-se escolher todas as seleções!')
            return
        
        # CRIANDO OS OBJETOS AMBULANTE/AJUDANTE: - (TERMINAR AJUDANTE)
        ambulante = Ambulante(self.nome, self.cpf, self.rg, self.email, self.telefone, self.cep, self.cidade, self.bairro, 
                              self.rua, self.nomeMae, self.dataNascimento, self.atividadeSelecao, self.racaSelecao, 
                              self.generoSelecao, self.possuiDeficienciaSelecao, self.escolaridadeSelecao, 
                              self.possuiTrabalhoSelecao, self.faixaSalarialSelecao)
        
        # CONFERINDO SE O CPF É VÁLIDO:

        if(ambulante.ConferirCpf() == False):
            messagebox.showinfo('Aviso!', f'O CPF do ambulante {ambulante.nome} passado foi inválido!')
            return
        
        # CONFERINDO SE O CPF/RG DO AMBULANTE JÁ FOI CADASTRADO

        # CONFERINDO SE O AMBULANTE É MAIOR DE IDADE:

        if(ambulante.ConferirMaiorIdade() == False):
            messagebox.showinfo('Aviso!', f'O ambulante {self.nome} não é maior de idade')
            return

        # CONFERÊNCIA DOS AJUDATES:
        
    # ======= MÉTODO DE VISUALIZAR O AMBULANTE NA LISTA (FRAME 03) - TREEVIEW =======
    def visualizarListaAmbulante(self):
        pass

    # ======= MÉTODO DE REMOVER O AMBULANTE =======
    def removerAmbulante(self):
        pass

    # ======= METODO PARA ATUALIZAR O AMBULANTE =======
    def atualizarAmbulante(self):
        pass
    
    # ======= MÉTODO PARA PEGAR O AMBULANTE E SUBI-LO AO FRAME 02 QUANDO FOR CLICADO 2X =======
    def onDoubleClick(self):
        pass

    # ======= MÉTODO DE BUSCA DO AMBULANTE(NOME, CPF, ID) =======
    def buscarAmbulante(self):
        pass


