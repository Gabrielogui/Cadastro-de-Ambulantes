import tkinter as tk

from Ambulante import *

# |=======| CONTROLE |=======|
class Controle():
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
        