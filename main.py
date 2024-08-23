import tkinter as tk
from Ambulante import Ambulante
from tkinter import messagebox

# |=======| FUNÇÕES |=======|

# ======= SALVAR OS DADOS ========
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

# ======= FUNÇÃO DE CHECK-LIST =======
def mostrar_selecionados():
    selecionados = []
    for item, var in checklist.items():
        if var.get():
            selecionados.append(item)

    equipamento_selecao.get()

    print("Itens selecionados:", ", ".join(selecionados), equipamento_selecao.get())


# ======= CRIAÇÃO DA JANELA =======
janela = tk.Tk()
janela.title('Cadastro de Ambulantes')

# |=======| ITENS GLOBAIS |=======|
checklist = {
    "Baleiro":tk.BooleanVar(),
    "Ambulante":tk.BooleanVar(),
    "Varejista":tk.BooleanVar()
}

# ======= CRIAÇÃO DOS CAMPOS =======

# NOME:
tk.Label(janela, text='Nome Completo:').grid(row=0, column=0, sticky=tk.W, padx=30, pady=30)
nome_entrada = tk.Entry(janela, width=30)
nome_entrada.grid(row=0, column=1, padx=10, pady=10)

# CPF:
tk.Label(janela, text='CPF:').grid(row=0, column=2, padx=30, pady=30)
cpf_entrada = tk.Entry(janela, width=30)
cpf_entrada.grid(row=0, column=3, padx=10, pady=10)

# RG:
tk.Label(janela, text='RG:').grid(row=0, column=4, padx=30, pady=30)
rg_entrada = tk.Entry(janela, width=30)
rg_entrada.grid(row=0, column=5, padx=10, pady=10)

# Municipio:
tk.Label(janela, text='Município:').grid(row=2, column=0, padx=30, pady=30)
municipio_entrada = tk.Entry(janela, width=30)
municipio_entrada.grid(row=2, column=1, padx=30, pady=30)

# Bairro:
tk.Label(janela, text='Bairro:').grid(row=2, column=2, padx=30, pady=30)
bairro_entrada = tk.Entry(janela, width=30)
bairro_entrada.grid(row=2, column=3, padx=30, pady=30)

# Rua:
tk.Label(janela, text='Rua:').grid(row=2, column=4, padx=30, pady=30)
rua_entrada = tk.Entry(janela, width=30)
rua_entrada.grid(row=2, column=5, padx=30, pady=30)

# Número do Celular:
tk.Label(janela, text='Celular:').grid(row=3, column=0, padx=30, pady=30)
celular_entrada = tk.Entry(janela, width=30)
celular_entrada.grid(row=3, column=2, padx=30, pady=30)

# Número do Whatsapp
tk.Label(janela, text='Whatsapp').grid(row=3, column=3)
whatsapp_entrada = tk.Entry(janela, width=30)
whatsapp_entrada.grid(row=3, column=5, padx=30, pady=30)

# |=======| LISTA DE OPÇÕES |=======|

# ======= ATIVIDADE/EQUIPAMENTO =======
# Lista de opções
opcoes_equipamento = ["Varejista", "Ambulante", "Baleiro"]

# Variável associada ao OptionMenu
equipamento_selecao = tk.StringVar(janela)
equipamento_selecao.set(opcoes_equipamento[0])  # Define a opção inicial

# Criação do OptionMenu
menu_opcoes_equipamento = tk.OptionMenu(janela, equipamento_selecao, *opcoes_equipamento)
menu_opcoes_equipamento.grid(row=4, column=2, padx=10, pady=10)

# ======= RAÇA =======

opcoes_raca = ["Negro", "Pardo", "Branco"]

raca_selecao = tk.StringVar(janela)
raca_selecao.set(opcoes_raca[0])

menu_opcoes_raca = tk.OptionMenu(janela, raca_selecao, *opcoes_raca)
menu_opcoes_raca.grid(row=4, column=0, padx=30, pady=30)

# ======= DDD CELULAR =======

opcoes_dddCelular = ["71", "75", "73", "74", "77"]

dddCelular_selecao = tk.StringVar(janela)
dddCelular_selecao.set(opcoes_dddCelular[0])

menu_opcoes_dddCelular = tk.OptionMenu(janela, dddCelular_selecao, *opcoes_dddCelular)
menu_opcoes_dddCelular.grid(row=3, column=1, padx=10, pady=10)

# ======= DDD WHATSAPP =======

opcoes_dddWhatsapp = ["71", "75", "73", "74", "77"]

dddWhatsapp_selecao = tk.StringVar(janela)
dddWhatsapp_selecao.set(opcoes_dddCelular[0])

menu_opcoes_dddWhatsapp = tk.OptionMenu(janela, dddCelular_selecao, *opcoes_dddCelular)
menu_opcoes_dddWhatsapp.grid(row=3, column=4, padx=10, pady=10)

# ======= ESCOLARIDADE =======

opcoes_Escolaridade = ["Ensino Fundamental II Incompleto", 
                       "Ensino Fundamental II Completo", 
                       "Ensino Médio Incompleto", 
                       "Ensino Médio Completo",
                       "Graduação Incompleta",
                       "Graduação Completa"]

escolaridade_selecao = tk.StringVar(janela)
escolaridade_selecao.set(opcoes_Escolaridade[0])

menu_opcoes_escolaridade = tk.OptionMenu(janela, escolaridade_selecao, *opcoes_Escolaridade)
menu_opcoes_escolaridade.grid(row=4, column=1, padx=30, pady=30)

# ======= CHECK-LIST =======
'''row_checkbox = 3
for item, var in checklist.items():
    tk.Checkbutton(janela, text=item, variable=var).grid(row=row_checkbox, column=0, padx=10, pady=10)
    row_checkbox += 1
'''

'''botao_check = tk.Button(janela, text='Selecionar', command=mostrar_selecionados)
botao_check.grid(row=row_checkbox, column=0, padx=10, pady=10)'''

# ======= BOTÃO =======
botao_salvar = tk.Button(janela, text='Salvar', command=salvar_dados)
botao_salvar.grid(row=5, column=0, padx=10, pady=10)


# ======= MAINLOOP =======
janela.mainloop()
