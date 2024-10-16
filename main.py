import tkinter as tk
from tkinter import messagebox

from Ambulante import Ambulante

# |=======| JANELAS PRINCIPAIS |=======|
janela = tk.Tk()

# |=======| View |=======|
class View():
    # ======= Construtor =======
    def __init__(self):
        self.janela = janela
        self.tela()
        self.menu()
        self.frames_da_tela()
        self.frame01()
        self.frame02()
        self.frame03()
        self.janela.mainloop()

    # ======= PRINCIPAIS CONFIGURAÇÕES DA TELA =======
    def tela(self):
        # CONFIGURAÇÃO DA TELA
        self.janela.title('Cadastro de Ambulantes')
        self.janela.configure(background= '#736e8f')
        self.janela.attributes('-fullscreen', True)
        self.janela.resizable(False, False)
        
    
    # ======= FRAMES DA TELA PRINCIPAL =======
    def frames_da_tela(self):
        # FRAME 01 - FRAME LATERAL (MENU DO USUÁRIO)
        self.frame_01 = tk.Frame(self.janela, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=1.5)
        self.frame_01.place(relx=0.005,rely=0.005,relheight=0.98,relwidth=0.1)

        # FRAME 02 - FRAME SUPERIOR (INSERIR OS DADOS)
        self.frame_02 = tk.Frame(self.janela, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=1.5)
        self.frame_02.place(relx=0.108, rely=0.005, relheight=0.485, relwidth=0.888)

        # FRAME 03 - FRAME INFERIOR (TREEVIEWS DOS CADASTRADOS)
        self.frame_03 = tk.Frame(self.janela, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=1.5)
        self.frame_03.place(relx=0.108, rely=0.5, relheight=0.485, relwidth=0.888)

    # ======= FRAME 01 (MENU DO USUÁRIO) =======
    def frame01(self):
        pass
    
    # ======= FRAME 02 (WIDGETS DO CADASTRO) =======
    def frame02(self):
        # ======= BOTÕES =======
        # BOTÃO LIMPAR:
        self.bt_limpar  = tk.Button(self.frame_02, text='Limpar', bd=2, bg='#3e557a', fg='white', font=('verdano', 0, 'bold'))
        self.bt_limpar.place(relx=0.12, rely=0.02, relwidth=0.05, relheight=0.1)

        # BOTÃO BUSCAR
        self.bt_buscar  = tk.Button(self.frame_02, text='Buscar', bd=2, bg='#3e557a', fg='white', font=('verdano', 0, 'bold'))
        self.bt_buscar.place(relx=0.171, rely=0.02, relwidth=0.05, relheight=0.1)

        # BOTÃO SALVAR
        self.bt_salvar  = tk.Button(self.frame_02, text='Salvar', bd=2, bg='#3e557a', fg='white', font=('verdano', 0, 'bold'))
        self.bt_salvar.place(relx=0.93, rely=0.88, relwidth=0.05, relheight=0.1)

        # BOTÃO ALTERAR
        self.bt_alterar = tk.Button(self.frame_02, text='Alterar', bd=2, bg='#3e557a', fg='white', font=('verdano', 0, 'bold'))
        self.bt_alterar.place(relx=0.3, rely=0.02, relwidth=0.05, relheight=0.1)

        # BOTÃO APAGAR
        self.bt_apagar  = tk.Button(self.frame_02, text='Apagar', bd=2, bg='#ab2e4b', fg='white', font=('verdano', 0, 'bold'))
        self.bt_apagar.place(relx=0.351, rely=0.02, relwidth=0.05, relheight=0.1)

        # ======= LABELS, ENTRY E LISTA DE OPÇÕES DOS AMBULANTES =======
        # LABEL E ENTRY DO ID: (TORNAR NÃO EDITAVEL)
        self.lb_id = tk.Label(self.frame_02, text='Código', bg='#dfe3ee')
        self.lb_id.place(relx=0.01, rely=0.02)

        self.id_entry = tk.Entry(self.frame_02) # IDEIA: COLOCAR COMO LABEL E UM BG WHITE, PARA FICAR NÃO EDITAVEL
        self.id_entry.place(relx=0.01, rely=0.08, relwidth=0.035) 

        # LABEL E ENTRY DO NOME:
        self.lb_nome = tk.Label(self.frame_02, text='Nome', bg='#dfe3ee')
        self.lb_nome.place(relx=0.01, rely=0.15)

        self.nome_entry = tk.Entry(self.frame_02)
        self.nome_entry.place(relx=0.01, rely=0.2, relwidth=0.2)

        # LABEL E ENTRY DO CPF: (VERIFICAÇÃO) - FORMATAR
        self.lb_cpf = tk.Label(self.frame_02, text='CPF', bg='#dfe3ee')
        self.lb_cpf.place(relx=0.22, rely=0.15)

        self.cpf_entry = tk.Entry(self.frame_02)
        self.cpf_entry.place(relx=0.22, rely=0.2, relwidth=0.09)

        # LABEL E ENTRY DO RG: - FORMATAR
        self.lb_rg = tk.Label(self.frame_02, text='RG', bg='#dfe3ee')
        self.lb_rg.place(relx=0.32, rely=0.15)

        self.rg_entry = tk.Entry(self.frame_02)
        self.rg_entry.place(relx=0.32, rely=0.2, relwidth=0.09)

        # LABEL E ENTRY DO TELEFONE:
        self.lb_telefone = tk.Label(self.frame_02, text='Telefone', bg='#dfe3ee')
        self.lb_telefone.place(relx=0.42, rely=0.15)

        self.telefone_entry = tk.Entry(self.frame_02)
        self.telefone_entry.place(relx=0.42, rely=0.2, relwidth=0.09)

        # LABEL E ENTRY DO EMAIL:
        self.lb_email = tk.Label(self.frame_02, text='Email', bg='#dfe3ee')
        self.lb_email.place(relx=0.52, rely=0.15)

        self.email_entry = tk.Entry(self.frame_02)
        self.email_entry.place(relx=0.52, rely=0.2, relwidth=0.12)

        # LABEL E ENTRY DO ENDEREÇO: (CEP, CIDADE, BAIRRO, RUA)
        # CEP - FORMATAR + VERIFICAÇÃO
        self.lb_cep = tk.Label(self.frame_02, text='CEP', bg='#dfe3ee')
        self.lb_cep.place(relx=0.65, rely=0.15)

        self.cep_entry = tk.Entry(self.frame_02)
        self.cep_entry.place(relx=0.65, rely=0.2, relwidth=0.08)

        # CIDADE - TRANSFORMAR ENTRY EM LABEL APÓS VERIFICAÇÃO DO CEP
        self.lb_cidade = tk.Label(self.frame_02, text='Cidade', bg='#dfe3ee')
        self.lb_cidade.place(relx=0.74, rely=0.15)

        self.cidade_entry = tk.Entry(self.frame_02)
        self.cidade_entry.place(relx=0.74, rely=0.2, relwidth=0.08)

        # BAIRRO
        self.lb_bairro = tk.Label(self.frame_02, text='Bairro', bg='#dfe3ee')
        self.lb_bairro.place(relx=0.83, rely=0.15)

        self.bairro_entry = tk.Entry(self.frame_02)
        self.bairro_entry.place(relx=0.83, rely=0.2, relwidth=0.08)

        # RUA
        self.lb_rua = tk.Label(self.frame_02, text='Rua', bg='#dfe3ee')
        self.lb_rua.place(relx=0.92, rely=0.15)

        self.rua_entry = tk.Entry(self.frame_02)
        self.rua_entry.place(relx=0.92, rely=0.2, relwidth=0.08)

        # LABEL E ENTRY DO NOME DA MÃE 
        self.lb_nomeMae = tk.Label(self.frame_02, text='Nome da Mãe', bg='#dfe3ee')
        self.lb_nomeMae.place(relx=0.01, rely=0.25)

        self.nomeMae_entry = tk.Entry(self.frame_02)
        self.nomeMae_entry.place(relx=0.01, rely=0.3, relwidth=0.2)

        # LABEL E ENTRY DA DATA DE NASCIMENTO: (SÓ ACEITO SE FOR MAIOR DE IDADE)
        self.lb_dataNascimento = tk.Label(self.frame_02, text='Data de Nascimento', bg='#dfe3ee')
        self.lb_dataNascimento.place(relx=0.22, rely=0.25)

        self.dataNascimento_entry = tk.Entry(self.frame_02)
        self.dataNascimento_entry.place(relx=0.22, rely=0.3, relwidth=0.09)

        # LABEL E LISTA DE OPÇÕES DA ATIVIDADE: (AMBULANTE, BARRAQUEIRO, CARRINHO DE ALIMENTAÇÃO, BAIANAS DE ACARAJÉ E BALEIROS)  
        # OPÇÕES - 
        self.opcoes_atividades = ['Ambulante', 'Barraqueiro', 'Carrinho de Alimentação', 'Baiana de Acarajé', 'Baleiro']
        self.atividade_selecao = tk.StringVar(self.frame_02)
        self.atividade_selecao.set('Escolha') # Pode colocar também a primeira opção 'self.opcoes_atividades[0]'

        self.lb_atividades = tk.Label(self.frame_02, text='Atividades', bg='#dfe3ee')
        self.lb_atividades.place(relx=0.32, rely=0.25)

        self.atividade_optionMenu = tk.OptionMenu(self.frame_02, self.atividade_selecao, *self.opcoes_atividades)
        self.atividade_optionMenu.place(relx=0.32, rely=0.3)

        # LABEL E LISTA DE OPÇÕES DA RAÇA (BRANCA, PRETA, PARDA, INDÍGENA E AMARELA)
        self.opcoes_racas = ['Branca', 'Preta', 'Parda', 'Indígena', 'Amarela']
        self.raca_selecao = tk.StringVar(self.frame_02)
        self.raca_selecao.set('Escolha a raca') # Pode colocar também a primeira opção 'self.opcoes_racas[0]'

        self.lb_racas = tk.Label(self.frame_02, text='Raça', bg='#dfe3ee')
        self.lb_racas.place(relx=0.42, rely=0.25)

        self.raca_optionMenu = tk.OptionMenu(self.frame_02, self.raca_selecao, *self.opcoes_racas)
        self.raca_optionMenu.place(relx=0.42, rely=0.3)

        # LABEL E LISTA DE OPÇÕES DO GÊNERO (HOMEM, MULHER, PREFERE NÃO IDENTIFICAR)
        self.opcoes_generos = ['Homem', 'Mulher', 'Prefiro não identificar']
        self.genero_selecao = tk.StringVar(self.frame_02)
        self.genero_selecao.set('Escolha o gênero') # Pode colocar também a primeira opção 'self.opcoes_generos[0]'

        self.lb_generos = tk.Label(self.frame_02, text='Gênero', bg='#dfe3ee')
        self.lb_generos.place(relx=0.52, rely=0.25)

        self.genero_optionMenu = tk.OptionMenu(self.frame_02, self.genero_selecao, *self.opcoes_generos)
        self.genero_optionMenu.place(relx=0.52, rely=0.3)

        # LABEL E LISTA DE OPÇÕES SE POSSUI DEFICIÊNCIA (SIM OU NÃO)
        self.opcoes_possuiDeficiencia = ['Não', 'Sim']
        self.possuiDeficiencia_selecao = tk.StringVar(self.frame_02)
        self.possuiDeficiencia_selecao.set(self.opcoes_possuiDeficiencia[0]) # Pode colocar também a primeira opção 'self.opcoes_possuiDeficiencia[0]'

        self.lb_possuiDeficiencia = tk.Label(self.frame_02, text='Possui deficiência?', bg='#dfe3ee')
        self.lb_possuiDeficiencia.place(relx=0.65, rely=0.25)

        self.possuiDeficiencia_optionMenu = tk.OptionMenu(self.frame_02, self.possuiDeficiencia_selecao, *self.opcoes_possuiDeficiencia)
        self.possuiDeficiencia_optionMenu.place(relx=0.65, rely=0.3)

        # LABEL E LISTA DE OPÇÕES ESCOLARIDADE (EDUCAÇÃO INFANTIL, FUNDAMENTAL I, FUNDAMENTAL II, ENSINO MÉDIO, SUPERIOR, PÓS-GRADUAÇÃO)
        self.opcoes_escolaridades = ['Homem', 'Mulher', 'Prefiro não identificar']
        self.escolaridade_selecao = tk.StringVar(self.frame_02)
        self.escolaridade_selecao.set('Escolha a escolaridade') # Pode colocar também a primeira opção 'self.opcoes_escolaridades[0]'

        self.lb_escolaridades = tk.Label(self.frame_02, text='Escolaridade', bg='#dfe3ee')
        self.lb_escolaridades.place(relx=0.74, rely=0.25)

        self.escolaridade_optionMenu = tk.OptionMenu(self.frame_02, self.escolaridade_selecao, *self.opcoes_escolaridades)
        self.escolaridade_optionMenu.place(relx=0.74, rely=0.3)

        # LABEL E LISTA DE OPÇÕES SE TRABALHA (SIM OU NÃO)

        # LABEL E LISTA DE OPÇÕES DA FAIXA SALARIAL (MENOS DE 1000, ENTRE 1000 E 2000, ENTRE 2000 E 3000, ETC...)

        # ======= LABEL, ENTRY E LISTA DE OPÇÕES DOS AJUDAENTES (INFOMAÇÕES DO AJUDANTE PERANTE A ATIVIDADE ESCOLHIDA) =======


    # ======= FRAME 03 (TREEVIEW DOS CADASTRADOS) =======
    def frame03(self):
        pass

    # ======= MENU SUPERIOR =======
    def menu(self):
        # CRIANDO A FUNCIONALIDADE DO MENU
        menubar = tk.Menu(self.janela)
        self.janela.config(menu=menubar)

        # CRIANDO ABAS DO MENU
        filemenu01 = tk.Menu(menubar)
        filemenu02 = tk.Menu(menubar)
        filemenu03 = tk.Menu(menubar)

        # COLOCANDO TÍTULOS
        menubar.add_cascade(label='Opções', menu=filemenu01)
        menubar.add_cascade(label='Sobre', menu=filemenu02)
        menubar.add_cascade(label='Relatórios', menu=filemenu03)

        def Quit(): self.janela.destroy() # colocar globalmente depois

        # MENU 01 - OPÇÕES
        filemenu01.add_command(label='Sair', command=Quit)

        # MENU 02 - SOBRE

        # MENU 03 - RELATÓRIOS


View()