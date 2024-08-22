import tkinter as tk
from Ambulante import Ambulante
from tkinter import messagebox

def salvar_dados():
    ambulante = Ambulante()

    ambulante.nome = nome_entrada.get()
    ambulante.cpf  = cpf_entrada.get()
    ambulante.rg   = rg_entrada.get()

    if((not ambulante.nome) or (not ambulante.cpf) or (not ambulante.rg)):
        messagebox.showwarning('Aviso!', 'Todos os campos devem ser preenchidos')
        return
    
    print(f'''
            Nome: {ambulante.nome}
            CPF : {ambulante.cpf}
            RG  : {ambulante.rg}
                ''')

    messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")

    nome_entrada.delete(0, tk.END)
    cpf_entrada.delete(0, tk.END)
    rg_entrada.delete(0, tk.END)

# ======= CRIAÇÃO DA JANELA =======
janela = tk.Tk()
janela.title('Cadastro de Ambulantes')

# ======= CRIAÇÃO DOS CAMPOS =======

# NOME:
tk.Label(janela, text='Nome Completo:').grid(row=0, column=0, padx=30, pady=30)
nome_entrada = tk.Entry(janela, width=30)
nome_entrada.grid(row=0, column=1, padx=10, pady=10)

# CPF:
tk.Label(janela, text='CPF:').grid(row=1, column=0, padx=30, pady=30)
cpf_entrada = tk.Entry(janela, width=30)
cpf_entrada.grid(row=1, column=1, padx=10, pady=10)

# RG:
tk.Label(janela, text='RG:').grid(row=2, column=0, padx=30, pady=30)
rg_entrada = tk.Entry(janela, width=30)
rg_entrada.grid(row=2, column=1, padx=10, pady=10)

# ======= BOTÃO =======
botao_salvar = tk.Button(janela, text='Salvar', command=salvar_dados)
botao_salvar.grid(row=3, column=1, padx=10, pady=10)


# ======= MAINLOOP =======
janela.mainloop()
