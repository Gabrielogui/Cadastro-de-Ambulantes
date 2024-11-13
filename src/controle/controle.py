import tkinter as tk
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
    # ======= MÉTODO DE CADASTRAR O AMBULANTE =======
    def cadastrarAmbulante(self):
        pass

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


