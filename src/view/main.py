import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry

from src.controle.controle import Controle
from src.modelo.Ambulante import Ambulante
from src.view.loginView import LoginView

# |=======| JANELAS PRINCIPAIS |=======|
janela = tk.Tk()

# |=======| VIEW |=======|
class View(Controle):
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
        '''
        - LOGO
        - PESSOA LOGADA(NOME)
        - OPÇÃO PARA DESLOGAR
        - ESCOLHA DAS ATIVIDADES
        - NÚMERO DE CADASTRADOS - TOTAL E POR ATIVIDADE
        '''
        # ======= LOGO =======
        self.logo = tk.Label(self.frame_01, text='LOGO')
        self.logo.place(relx=0.05, rely=0.01, relwidth=0.9, relheight=0.1)

        # ======= USUÁRIO LOGADO =======
        nome = 'nome do usuário'
        self.nome_logado = tk.Label(self.frame_01, text=f'OI, {nome}')
        self.nome_logado.place(relx=0.05, rely=0.13, relwidth=0.9, relheight=0.05)

        # ======= OPÇÃO DE DESLOGAR =======
        self.deslogar = tk.Button(self.frame_01, text='Deslogar', bd=2, bg='#3e557a', fg='white', font=('verdano', 0, 'bold'))
        self.deslogar.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.05)

        # ======= ESCOLHA DAS ATIVIDADES =======
        self.opcoes_atividades = ['Ambulante', 'Barraqueiro', 'Carrinho de Alimentação', 'Baiana de Acarajé', 'Baleiro']
        self.atividade_selecao = tk.StringVar(self.frame_01)
        self.atividade_selecao.set('Escolha') # Pode colocar também a primeira opção 'self.opcoes_atividades[0]'

        self.lb_atividades = tk.Label(self.frame_01, text='Atividades', bg='#dfe3ee')
        self.lb_atividades.place(relx=0.05, rely=0.28)

        self.atividade_optionMenu = tk.OptionMenu(self.frame_01, self.atividade_selecao, *self.opcoes_atividades, command=self.frame02_atualizaAjudante)
        #self.atividade_optionMenu.bind('<1>', lambda e: self.atividade_selecao.set(self.opcoes_atividades[0]))
        self.atividade_optionMenu.place(relx=0.05, rely=0.3)

        # ======= NÚMERO DE CADASTRADOS POR ATIVIDADE/TOTAL =======
        # TOTAL:
        self.totalCadastrados = tk.Label(self.frame_01, text='Nº Total')
        self.totalCadastrados.place(relx=0.05, rely=0.6)

        # AMBULANTE:
        self.totalCadastrados_Ambulante = tk.Label(self.frame_01, text='Nº Ambulante')
        self.totalCadastrados_Ambulante.place(relx=0.05, rely=0.64)

        # BARRAQUEIRO
        self.totalCadastrados_Barraqueiro = tk.Label(self.frame_01, text='Nº Barraqueiro')
        self.totalCadastrados_Barraqueiro.place(relx=0.05, rely=0.68)

        # CARRINHO DE ALIMENTAÇÃO:
        self.totalCadastrados_CarrinhoDeAlimentacao = tk.Label(self.frame_01, text='Nº Carrinho')
        self.totalCadastrados_CarrinhoDeAlimentacao.place(relx=0.05, rely=0.72)

        # BAIANA DE ACARAJÉ:
        self.totalCadastrados_BaianaDeAcaraje = tk.Label(self.frame_01, text='Nº Baiana')
        self.totalCadastrados_BaianaDeAcaraje.place(relx=0.05, rely=0.76)

        # BALEIRO
        self.totalCadastrados_Baleiro = tk.Label(self.frame_01, text='Nº Baleiro')
        self.totalCadastrados_Baleiro.place(relx=0.05, rely=0.8)

    # ======= FRAME 02 (WIDGETS DO CADASTRO) =======
    def frame02(self):
        # ======= BOTÕES =======
        # BOTÃO LIMPAR:
        self.bt_limpar  = tk.Button(self.frame_02, text='Limpar', bd=2, bg='#3e557a', fg='white', font=('verdano', 0, 'bold'), command=self.limpa_tela)
        self.bt_limpar.place(relx=0.12, rely=0.02, relwidth=0.05, relheight=0.1)

        # BOTÃO BUSCAR
        self.bt_buscar  = tk.Button(self.frame_02, text='Buscar', bd=2, bg='#3e557a', fg='white', font=('verdano', 0, 'bold'))
        self.bt_buscar.place(relx=0.171, rely=0.02, relwidth=0.05, relheight=0.1)

        # BOTÃO SALVAR
        self.bt_salvar  = tk.Button(self.frame_02, text='Salvar', bd=2, bg='#3e557a', fg='white', font=('verdano', 0, 'bold'), command=self.cadastrarAmbulante)
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
        self.cpf_entry.bind('<KeyRelease>', self.formatarCPF)
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
        self.telefone_entry.bind('<KeyRelease>', self.formatarTelefone)
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
        self.cep_entry.bind('<KeyRelease>', self.formatarCEP)
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
        self.dataNascimento_entry.bind('<KeyRelease>', self.formatarDataNascimento)
        self.dataNascimento_entry.place(relx=0.22, rely=0.3, relwidth=0.09)

        self.dataNascimento_calendario = DateEntry(self.frame_02, date_pattern="dd/mm/yyyy")
        self.dataNascimento_calendario.place(relx=0.32, rely=0.3)

        # LABEL E LISTA DE OPÇÕES DA ATIVIDADE: (AMBULANTE, BARRAQUEIRO, CARRINHO DE ALIMENTAÇÃO, BAIANAS DE ACARAJÉ E BALEIROS)  
        # OPÇÕES - FOI PARA O FRAME 01
        '''self.opcoes_atividades = ['Ambulante', 'Barraqueiro', 'Carrinho de Alimentação', 'Baiana de Acarajé', 'Baleiro']
        self.atividade_selecao = tk.StringVar(self.frame_02)
        self.atividade_selecao.set('Escolha') # Pode colocar também a primeira opção 'self.opcoes_atividades[0]'

        self.lb_atividades = tk.Label(self.frame_02, text='Atividades', bg='#dfe3ee')
        self.lb_atividades.place(relx=0.32, rely=0.25)

        self.atividade_optionMenu = tk.OptionMenu(self.frame_02, self.atividade_selecao, *self.opcoes_atividades, command=self.frame02_atualizaAjudante)
        #self.atividade_optionMenu.bind('<1>', lambda e: self.atividade_selecao.set(self.opcoes_atividades[0]))
        self.atividade_optionMenu.place(relx=0.32, rely=0.3)'''

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
        self.opcoes_escolaridades = ['Fundamental I incompleto', 'Fundamental I completo', 'Fundamental II incompleto', 'Fundamental I completo',
                                     'Ensino Médio incompleto', 'Ensino Médio completo', 'Ensino Superior incompleto', 'Ensino Superior completo',
                                     'Pós Graduação incompleto', 'Pós Graduação incompleto']
        self.escolaridade_selecao = tk.StringVar(self.frame_02)
        self.escolaridade_selecao.set('Escolha') # Pode colocar também a primeira opção 'self.opcoes_escolaridades[0]'

        self.lb_escolaridades = tk.Label(self.frame_02, text='Escolaridade', bg='#dfe3ee')
        self.lb_escolaridades.place(relx=0.74, rely=0.25)

        self.escolaridade_optionMenu = tk.OptionMenu(self.frame_02, self.escolaridade_selecao, *self.opcoes_escolaridades)
        self.escolaridade_optionMenu.place(relx=0.74, rely=0.3)

        # LABEL E LISTA DE OPÇÕES SE TRABALHA (SIM OU NÃO)
        self.opcoes_possuiTrabalho = ['Não', 'Sim']
        self.possuiTrabalho_selecao = tk.StringVar(self.frame_02)
        self.possuiTrabalho_selecao.set(self.opcoes_possuiTrabalho[0]) # Pode colocar também a primeira opção 'self.opcoes_possuiTrabalho[0]'

        self.lb_possuiTrabalho = tk.Label(self.frame_02, text='Possui trabalho?', bg='#dfe3ee')
        self.lb_possuiTrabalho.place(relx=0.83, rely=0.25)

        self.possuiTrabalho_optionMenu = tk.OptionMenu(self.frame_02, self.possuiTrabalho_selecao, *self.opcoes_possuiTrabalho)
        self.possuiTrabalho_optionMenu.place(relx=0.83, rely=0.3)

        # LABEL E LISTA DE OPÇÕES DA FAIXA SALARIAL (MENOS DE 1000, ENTRE 1000 E 2000, ENTRE 2000 E 3000, ETC...)
        self.opcoes_faixaSalariais = ['-1000', '1000-2000', '2000-3000', '3000-4000', '4000-']
        self.faixaSalarial_selecao = tk.StringVar(self.frame_02)
        self.faixaSalarial_selecao.set('Escolha') # Pode colocar também a primeira opção 'self.opcoes_faixaSalariais[0]'

        self.lb_faixaSalariais = tk.Label(self.frame_02, text='Faixa Salarial', bg='#dfe3ee')
        self.lb_faixaSalariais.place(relx=0.92, rely=0.25)

        self.faixaSalarial_optionMenu = tk.OptionMenu(self.frame_02, self.faixaSalarial_selecao, *self.opcoes_faixaSalariais)
        self.faixaSalarial_optionMenu.place(relx=0.92, rely=0.3)
    
    # ======= LABEL, ENTRY E LISTA DE OPÇÕES DOS AJUDAENTES (INFOMAÇÕES DO AJUDANTE PERANTE A ATIVIDADE ESCOLHIDA) =======
    # CRIAÇÃO DO 'OPTIONMENU' DA QUANTIDADE DE AJUDANTES 
    def frame02_atualizaAjudante(self, atividade_selecao):
        print(f'-> {atividade_selecao}, {self.atividade_selecao.get()} <-')

        # NÚMERO DE AJUDANDTES POSSÍVEIS DE CADA ATIVIDADE
        qtdeAjudante = 0
        if(self.atividade_selecao.get() == 'Ambulante'):
            qtdeAjudante = 1
        elif(self.atividade_selecao.get() == 'Barraqueiro'):
            qtdeAjudante = 3
        elif(self.atividade_selecao.get() == 'Carrinho de Alimentação'):
            qtdeAjudante = 1
        elif(self.atividade_selecao.get() == 'Baiana de Acarajé'):
            qtdeAjudante = 2
        elif(self.atividade_selecao.get() == 'Baleiro'):
            qtdeAjudante = 0
        else:
            return
        
        # LABEL E LISTA DE OPÇÕES DO NÚMERO DE AJUDADNTES
        self.opcoes_ajudantes = []
        for numAjudantes in range(qtdeAjudante + 1):
            self.opcoes_ajudantes.append(numAjudantes)

        self.ajudante_selecao = tk.StringVar(self.frame_02)
        self.ajudante_selecao.set(self.opcoes_ajudantes[0]) # Pode colocar também a primeira opção 'self.opcoes_ajudantes[0]'

        self.lb_ajudantes = tk.Label(self.frame_02, text='ajudantes', bg='#dfe3ee')
        self.lb_ajudantes.place(relx=0.05, rely=0.38)

        self.ajudante_optionMenu = tk.OptionMenu(self.frame_02, self.ajudante_selecao, *self.opcoes_ajudantes, command=self.frame02_criandoCamposAjudantes)
        self.ajudante_optionMenu.place(relx=0.05, rely=0.43)

    # CRIAÇÃO DOS CAMPOS PARA AJUDANTES 
    def frame02_criandoCamposAjudantes(self, ajudante_selecao):
        
        # EXCLUINDO OS CAMPOS DOS AJUDANTES JÁ EXISTENTES
        if(hasattr(self, 'campos_ajudantes')):
            for campos in self.campos_ajudantes:
                campos.destroy()

        self.campos_ajudantes = []

        print(f'<<< {self.ajudante_selecao.get()} >>>')
        # ======= LABELS E ENTRYS DOS AJUDANTES =======
        for i in range(int(self.ajudante_selecao.get())):
            if(int(self.ajudante_selecao.get()) == 0):
                return
            if((int(self.ajudante_selecao.get()) == 1) or (int(self.ajudante_selecao.get()) == 2) or (int(self.ajudante_selecao.get()) == 3)):
                # AJUDANTE 01
                # NOME:
                self.lb_nomeAjudante01 = tk.Label(self.frame_02, text='Nome do ajudante 01', bg='#dfe3ee')
                self.lb_nomeAjudante01.place(relx=0.01, rely=0.55)
                self.campos_ajudantes.append(self.lb_nomeAjudante01)

                self.nomeAjudante01_entry = tk.Entry(self.frame_02)
                self.nomeAjudante01_entry.place(relx=0.01, rely=0.6, relwidth=0.2)  
                self.campos_ajudantes.append(self.nomeAjudante01_entry)

                # CPF:
                self.lb_cpfAjudante01 = tk.Label(self.frame_02, text='CPF do ajudante 01', bg='#dfe3ee')
                self.lb_cpfAjudante01.place(relx=0.01, rely=0.65)
                self.campos_ajudantes.append(self.lb_cpfAjudante01)

                self.cpfAjudante01_entry = tk.Entry(self.frame_02)
                self.cpfAjudante01_entry.place(relx=0.01, rely=0.7, relwidth=0.09) 
                self.campos_ajudantes.append(self.cpfAjudante01_entry) 

                # DATA DE NASCIMENTO:
                self.lb_dataNascimentoAjudante01 = tk.Label(self.frame_02, text='Data de nascimento', bg='#dfe3ee')
                self.lb_dataNascimentoAjudante01.place(relx=0.12, rely=0.65)
                self.campos_ajudantes.append(self.lb_dataNascimentoAjudante01)

                self.dataNascimentoAjudante01_entry = tk.Entry(self.frame_02)
                self.dataNascimentoAjudante01_entry.place(relx=0.12, rely=0.7, relwidth=0.09) 
                self.campos_ajudantes.append(self.dataNascimentoAjudante01_entry)
            if((int(self.ajudante_selecao.get()) == 2) or (int(self.ajudante_selecao.get()) == 3)):
                # AJUDANTE 02
                # NOME:
                self.lb_nomeAjudante02 = tk.Label(self.frame_02, text='Nome do ajudante 02', bg='#dfe3ee')
                self.lb_nomeAjudante02.place(relx=0.31, rely=0.55)
                self.campos_ajudantes.append(self.lb_nomeAjudante02)

                self.nomeAjudante02_entry = tk.Entry(self.frame_02)
                self.nomeAjudante02_entry.place(relx=0.31, rely=0.6, relwidth=0.2)
                self.campos_ajudantes.append(self.nomeAjudante02_entry)

                # CPF:
                self.lb_cpfAjudante02 = tk.Label(self.frame_02, text='CPF do ajudante 02', bg='#dfe3ee')
                self.lb_cpfAjudante02.place(relx=0.31, rely=0.65)
                self.campos_ajudantes.append(self.lb_cpfAjudante02)

                self.cpfAjudante02_entry = tk.Entry(self.frame_02)
                self.cpfAjudante02_entry.place(relx=0.31, rely=0.7, relwidth=0.09)  
                self.campos_ajudantes.append(self.cpfAjudante02_entry)

                # DATA DE NASCIMENTO:
                self.lb_dataNascimentoAjudante02 = tk.Label(self.frame_02, text='Data de nascimento', bg='#dfe3ee')
                self.lb_dataNascimentoAjudante02.place(relx=0.42, rely=0.65)
                self.campos_ajudantes.append(self.lb_dataNascimentoAjudante02)

                self.dataNascimentoAjudante02_entry = tk.Entry(self.frame_02)
                self.dataNascimentoAjudante02_entry.place(relx=0.42, rely=0.7, relwidth=0.09)
                self.campos_ajudantes.append(self.dataNascimentoAjudante02_entry)
            if(int(self.ajudante_selecao.get()) == 3):
                # --- AJUDANTE 03 ---
                # NOME:
                self.lb_nomeAjudante03 = tk.Label(self.frame_02, text='Nome do ajudante 03', bg='#dfe3ee')
                self.lb_nomeAjudante03.place(relx=0.61, rely=0.55)
                self.campos_ajudantes.append(self.lb_nomeAjudante03)

                self.nomeAjudante03_entry = tk.Entry(self.frame_02)
                self.nomeAjudante03_entry.place(relx=0.61, rely=0.6, relwidth=0.2)   
                self.campos_ajudantes.append(self.nomeAjudante03_entry)

                # CPF:
                self.lb_cpfAjudante03 = tk.Label(self.frame_02, text='CPF do ajudante 03', bg='#dfe3ee')
                self.lb_cpfAjudante03.place(relx=0.61, rely=0.65)
                self.campos_ajudantes.append(self.lb_cpfAjudante03)

                self.cpfAjudante03_entry = tk.Entry(self.frame_02)
                self.cpfAjudante03_entry.place(relx=0.61, rely=0.7, relwidth=0.09) 
                self.campos_ajudantes.append(self.cpfAjudante03_entry) 

                # DATA DE NASCIMENTO:
                self.lb_dataNascimentoAjudante03 = tk.Label(self.frame_02, text='Data de nascimento', bg='#dfe3ee')
                self.lb_dataNascimentoAjudante03.place(relx=0.72, rely=0.65)
                self.campos_ajudantes.append(self.lb_dataNascimentoAjudante03)

                self.dataNascimentoAjudante03_entry = tk.Entry(self.frame_02)
                self.dataNascimentoAjudante03_entry.place(relx=0.72, rely=0.7, relwidth=0.09) 
                self.campos_ajudantes.append(self.dataNascimentoAjudante03_entry)
            if((int(self.ajudante_selecao.get()) != 1) and (int(self.ajudante_selecao.get()) != 2) and (int(self.ajudante_selecao.get()) != 3)):
                messagebox.showerror('[ERRO] - Número de ajudantes', 'Não é possível ter mais de três ajudantes!')
                return

    # ======= FRAME 03 (TREEVIEW DOS CADASTRADOS) =======
    def frame03(self):
        # ======= BOTÕES =======

        # ======= LISTA DOS CADASTRADOS - TREEVIEW =======
        self.listaAmbulantes = ttk.Treeview(self.frame_03, height=6, columns=('col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9', 'col10', 'col11', 'col', ''))

        # TÍTULOS DA LISTA - TREEVIEW
        self.listaAmbulantes.heading('#0', text='')
        self.listaAmbulantes.heading('#1', text='Código')
        self.listaAmbulantes.heading('#2', text='Nome')
        self.listaAmbulantes.heading('#3', text='CPF')
        self.listaAmbulantes.heading('#4', text='RG')
        self.listaAmbulantes.heading('#5', text='Telefone')
        self.listaAmbulantes.heading('#6', text='Email')
        self.listaAmbulantes.heading('#7', text='CEP')
        self.listaAmbulantes.heading('#8', text='Cidade')
        self.listaAmbulantes.heading('#9', text='Bairro')
        self.listaAmbulantes.heading('#10', text='Rua')
        self.listaAmbulantes.heading('#11', text='Nome da mãe')
        self.listaAmbulantes.heading('#12', text='Atividade')
        self.listaAmbulantes.heading('#13', text='Raça')

        # TAMANHO DOS TÍTULOS DA LISTA - TREEVIEW
        self.listaAmbulantes.column('#0', width=1)
        self.listaAmbulantes.column('#1', width=50)
        self.listaAmbulantes.column('#2', width=200)
        self.listaAmbulantes.column('#3', width=100)
        self.listaAmbulantes.column('#4', width=100)
        self.listaAmbulantes.column('#5', width=100)
        self.listaAmbulantes.column('#6', width=100)
        self.listaAmbulantes.column('#7', width=100)
        self.listaAmbulantes.column('#8', width=100)
        self.listaAmbulantes.column('#9', width=100)
        self.listaAmbulantes.column('#10', width=100)
        self.listaAmbulantes.column('#11', width=200)
        self.listaAmbulantes.column('#12', width=100)
        self.listaAmbulantes.column('#13', width=100)

        # POSICIONANDO A LISTA - TREEVIEW
        self.listaAmbulantes.place(relx=0, rely=0.1,relwidth=0.98, relheight=0.95)

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

if __name__ == '__main__':
    #LoginView()
    View()