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
        
    def conecta_bd(self):
        self.conn = sqlite3.connect('cadastro_ambulante.bd')
        self.cursor = self.conn.cursor()
        print('conectando ao banco de dados !')

    def desconecta_bd(self):
        self.conn.close()
        print('desconectando do banco de dados!')

    def montar_tabelas(self):
        self.conecta_bd()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS ambulante(
                id INTEGER PRIMARY KEY,
                nome char(50) NOT NULL,
                
                )
        ''')