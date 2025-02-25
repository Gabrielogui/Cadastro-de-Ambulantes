import tkinter as tk
from tkinter import messagebox
import sqlite3

from src.modelo.Ambulante import *

# |=======| CONTROLE |=======|
class Controle():
    # ======= MÉTODO LIMPAR TELA (LIMPA OS ENTRYS DO FRAME 02) =======
    def limpa_tela(self):
        # ID:
        self.id = ''
        self.id_entry.config(text=f'{self.id}')

        # ENTRYS:
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
        self.dataNascimento_calendario.delete(0, tk.END)

        # OPTIONS MENU:
        self.atividade_selecao.set('Escolha')
        self.raca_selecao.set('Escolha a raca')
        self.genero_selecao.set('Escolha o genero')
        self.possuiDeficiencia_selecao.set(self.opcoes_possuiDeficiencia[0])
        self.escolaridade_selecao.set('Escolha')
        self.possuiTrabalho_selecao.set(self.opcoes_possuiTrabalho[0])
        self.faixaSalarial_selecao.set('Escolha')

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
                id INTEGER PRIMARY KEY NOT NULL,
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
        ''')

        self.cursor.execute('''                               
            CREATE TABLE IF NOT EXISTS ajudante(
                id_ajudante INTEGER PRIMARY KEY NOT NULL,
                nome_ajudante char(50) NOT NULL,
                cpf_ajudante char(11) NOT NULL,
                data_nascimento date NOT NULL,
                id_ambulante INTEGER NOT NULL,
                FOREIGN KEY (id_ambulante) REFERENCES ambulante(id)
            )
        ''')

        self.conn.commit()
        print('Banco de dados Criado!')
        self.desconecta_bd()

    # |=======| FORMATAÇÃO DOS ENTRYS |=======|
    # ======= FORMATAÇÃO DO CPF =======
    def formatarCPF(self, event):

        # Tirando sinais, deixando só os números e limite de 11 caracteres
        self.cpf = self.cpf_entry.get().replace(".", "").replace("-", "")[:11] 
        novo_Texto = ""

        # Conferindo se a tecla "backspace" (Espaço) foi apertada
        if event.keysym.lower() == "backspace": 
            return
        
        # Conferido se os digitos do CPF são números e adicionando no texto o '.' e o '-'
        for i in range(len(self.cpf)):
            if(not self.cpf[i] in '0123456789'):
                continue
            if(i in [2, 5]):
                novo_Texto += self.cpf[i] + '.'
            elif(i in [8]):
                novo_Texto += self.cpf[i] + '-'
            else:
                novo_Texto += self.cpf[i]

        self.cpf_entry.delete(0, 'end')
        self.cpf_entry.insert(0, novo_Texto)

    # ======= FORATAÇÃO DO TELEFONE =======
    def formatarTelefone(self, event):

        # TIRANDO SINAIS(COM EXCEÇÃO DE '()', '-' e ' '), DEIXANDO SÓ OS NÚMEROS E MARCANDO O LIMITE DO CARACTER
        self.telefone = self.telefone_entry.get().replace("(", "").replace(')', "").replace("-", '').replace(' ', '')[:11]
        novo_Texto = '('

        # Conferindo se a tecla "backspace" (Espaço) foi apertada
        if event.keysym.lower() == "backspace": 
            return
        
        # Conferido se os digitos do telefone são números e adicionando no Texto o '()' e o '-'
        for i in range(len(self.telefone)):
            if(not self.telefone[i] in '0123456789'):
                continue
            if(i in [1]):
                novo_Texto += self.telefone[i] + ') '
            elif(i in [2]):
                novo_Texto += self.telefone[i] + ' '
            elif(i in [6]):
                novo_Texto += self.telefone[i] + '-'
            else:
                novo_Texto += self.telefone[i]

        self.telefone_entry.delete(0, 'end')
        self.telefone_entry.insert(0, novo_Texto)

    # ======= FORMATAÇÃO DO RG =======
    def formatarRG(self, event):
        pass

    # ======= FORMATAÇÃO DO CEP =======
    def formatarCEP(self, event):
        
        # TIRANDO OS SINAIS(COM EXCEÇÃO DE '-') E COLOCANDO LIMITE DE 8 CHARS
        self.cep = self.cep_entry.get().replace('-', '')[:8]

        novo_Texto = ""

        # Conferindo se a tecla "backspace" (Espaço) foi apertada
        if event.keysym.lower() == "backspace": 
            return
        
        for i in range(len(self.cep)):
            if(not self.cep[i] in '0123456789'):
                continue
            if(i in [4]):
                novo_Texto += self.cep[i] + '-'
            else:
                novo_Texto += self.cep[i]

        self.cep_entry.delete(0, 'end')
        self.cep_entry.insert(0, novo_Texto)


    # ======= FORMATAÇÃO DA DATA DE NASCIMENTO =======
    def formatarDataNascimento(self, event):
        # TIRANDO OS SINAIS(COM EXCEÇÃO DE '/') E COLOCANDO LIMITE DE 8 CHARS
        self.dataNascimento = self.dataNascimento_entry.get().replace('/', '')[:8]

        novo_Texto = ""

        # Conferindo se a tecla "backspace" (Espaço) foi apertada
        if event.keysym.lower() == "backspace": 
            return
        
        for i in range(len(self.dataNascimento)):
            if(not self.dataNascimento[i] in '0123456789'):
                continue
            if(i in [1, 3]):
                novo_Texto += self.dataNascimento[i] + '/'
            else:
                novo_Texto += self.dataNascimento[i]

        self.dataNascimento_entry.delete(0, 'end')
        self.dataNascimento_entry.insert(0, novo_Texto)

    # |=======| MÉTODOS 'CRUD' |=======|
    # ======= MÉTODO PARA PEGAR TODOS OS ENTRYS DO AMBULANTE =======
    def pegandoEntrysAmbulante(self):
        # ENTRYS:
        #self.id             = self.id_entry.get()
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
        #self.dataNascimento = self.dataNascimento_entry.get()
        self.dataNascimento = self.dataNascimento_calendario.get()

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

        # QUANTIDADE DE AJUDANTE:
        if(self.atividadeSelecao == 'Escolha'):
            self.ajudanteSelecao = 0
        else:
            self.ajudanteSelecao = int(self.ajudante_selecao.get())

        # TESTE:
        print(self.ajudanteSelecao)
       
    # ======= MÉTODO PARA PEGAR TODOS OS ENTRYS DO AJUDANTE =======
    def pegandoEntryAjudante(self):
        # LISTA DE RETORNO:
        listaAjudante = []

        print(f'Nº ajudantes: {self.ajudanteSelecao}')

        # CONDICIONAL DA QUANTIDADE DE AJUDANTES:
        if(self.ajudanteSelecao == 0):
            return
        elif(self.ajudanteSelecao == 1):            
            self.nomeAjudante01           = self.nomeAjudante01_entry.get()
            self.cpfAjudante01            = self.cpfAjudante01_entry.get()
            self.dataNascimentoAjudante01 = self.dataNascimentoAjudante01_entry.get()

            ajudante01 = (self.nomeAjudante01, self.cpfAjudante01, self.dataNascimentoAjudante01)
            listaAjudante.append(ajudante01)
  
        elif(self.ajudanteSelecao == 2):
            self.nomeAjudante01           = self.nomeAjudante01_entry.get()
            self.cpfAjudante01            = self.cpfAjudante01_entry.get()
            self.dataNascimentoAjudante01 = self.dataNascimentoAjudante01_entry.get()

            ajudante01 = (self.nomeAjudante01, self.cpfAjudante01, self.dataNascimentoAjudante01)
            listaAjudante.append(ajudante01)

            self.nomeAjudante02           = self.nomeAjudante02_entry.get()
            self.cpfAjudante02            = self.cpfAjudante02_entry.get()
            self.dataNascimentoAjudante02 = self.dataNascimentoAjudante02_entry.get()

            ajudante02 = (self.nomeAjudante02, self.cpfAjudante02, self.dataNascimentoAjudante02)
            listaAjudante.append(ajudante02)

        elif(self.ajudanteSelecao == 3):
            self.nomeAjudante01           = self.nomeAjudante01_entry.get()
            self.cpfAjudante01            = self.cpfAjudante01_entry.get()
            self.dataNascimentoAjudante01 = self.dataNascimentoAjudante01_entry.get()

            ajudante01 = (self.nomeAjudante01, self.cpfAjudante01, self.dataNascimentoAjudante01)
            listaAjudante.append(ajudante01)

            self.nomeAjudante02           = self.nomeAjudante02_entry.get()
            self.cpfAjudante02            = self.cpfAjudante02_entry.get()
            self.dataNascimentoAjudante02 = self.dataNascimentoAjudante02_entry.get()

            ajudante02 = (self.nomeAjudante02, self.cpfAjudante02, self.dataNascimentoAjudante02)
            listaAjudante.append(ajudante02)

            self.nomeAjudante03           = self.nomeAjudante03_entry.get()
            self.cpfAjudante03            = self.cpfAjudante03_entry.get()
            self.dataNascimentoAjudante03 = self.dataNascimentoAjudante03_entry.get()

            ajudante03 = (self.nomeAjudante03, self.cpfAjudante03, self.dataNascimentoAjudante03)
            listaAjudante.append(ajudante03)
            
        return listaAjudante

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
        
        # CONFERIR SE AINDA HÁ VAGAS DISPONÍVEIS

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
        self.conecta_bd()

        lista = self.cursor.execute('''SELECT cpf, rg FROM ambulante''')

        for elemento in lista:
            if(elemento[0] == ambulante.cpf):
                messagebox.showinfo('Aviso!' f'O CPF do ambulante {ambulante.nome} passado já foi cadastrado!')
                return
            elif(elemento[1] == ambulante.rg):
                messagebox.showinfo('Aviso!' f'O CPF do ambulante {ambulante.nome} passado já foi cadastrado!')
                return

        self.conn.commit()
        self.desconecta_bd()

        

        # CONFERINDO SE A DATA PASSADA É VÁLIDA:

        # CONFERINDO SE O AMBULANTE É MAIOR DE IDADE:

        if(ambulante.ConferirMaiorIdade() == False):
            messagebox.showinfo('Aviso!', f'O ambulante {self.nome} não é maior de idade')
            return

        # ADICIONANDO NO BANCO DE DADOS - TESTAR
        self.conecta_bd()

        self.cursor.execute('''
            INSERT INTO
                ambulante (
                nome, cpf, rg, email, telefone, cep, cidade, bairro, rua, atividade, data_nascimento, 
                nome_mae, raca, genero, deficiencia, escolaridade, trabalha, faixa_salarial)
            VALUES
                (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (ambulante.nome, ambulante.cpf, ambulante.rg, ambulante.email, ambulante.telefone, ambulante.cep, ambulante.cidade, 
              ambulante.bairro, ambulante.rua, ambulante.atividade, ambulante.data_nascimento, ambulante.nome_mae, ambulante.raca, 
              ambulante.genero, ambulante.deficiencia, ambulante.escolaridade, ambulante.trabalha, ambulante.faixa_salarial)
        ) # Adicionar o número de ajudantes
 
        self.conn.commit()
        self.desconecta_bd()

        self.visualizarListaAmbulante()

        # CONFERÊNCIA DOS AJUDATES: - CONTINUAR

        # PEGANDO AJUDANTES:
        listaAjudante = self.pegandoEntryAjudante()

        listaAjudanteDTO = []
        for ajudante in listaAjudante:
            listaAjudanteDTO.append(Ajudante(ajudante[0], ajudante[1], ajudante[2]))
                   
        if(self.ajudanteSelecao not in [0, 1, 2, 3]):
            messagebox.showerror('ERRO', f'Foi na passagem do nº de ajuantes')
            return
        
        ambulante.ajudantes = listaAjudanteDTO

        # CONFERIR SE TODOS OS CAMPOS FORAM PASSADOS:

        # CONFERINDO SE CPF É VÁLIDO E SE JÁ FOI CADASTRADO:

        # CONFERINDO SE A DATA PASSADA É VÁLIDA:

        # CONFERIR SE É MAIOR DE IDADE:


        # ATUALIZANDO O TOTAL DE CADASTRADOS
        self.qtdeCadastrados = self.totalAmbulante()
        print(f'ADICIONANDO AMBULANTE {self.qtdeCadastrados} | {self.totalAmbulante()}')
        self.totalCadastrados.config(text=f'[TESTE ADICIONAR]: {self.qtdeCadastrados}') 
        
    # ======= MÉTODO DE VISUALIZAR O AMBULANTE NA LISTA (FRAME 03) - TREEVIEW =======
    def visualizarListaAmbulante(self):
        self.listaAmbulantes.delete(*self.listaAmbulantes.get_children())

        self.conecta_bd()

        lista = self.cursor.execute('''
            SELECT 
                id, nome, cpf, rg, email, telefone, cep, cidade, bairro, rua, atividade, 
                nome_mae, raca
            FROM ambulante
            ORDER BY id;
        ''')

        '''
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
        '''

        for ambulante in lista:
            self.listaAmbulantes.insert('', tk.END, values=ambulante)

        self.conn.commit()
        self.desconecta_bd()


    # ======= MÉTODO DE REMOVER O AMBULANTE =======
    def removerAmbulante(self):
        idDeletar = self.id_entry.cget("text") # PEGAR ID

        self.conecta_bd()

        self.cursor.execute('''
            DELETE from ambulante
            where id = (?)
        ''', (idDeletar))

        self.conn.commit()
        self.desconecta_bd()

        self.visualizarListaAmbulante()
        self.limpa_tela()

        # ATUALIZANDO O TOTAL DE CADASTRADOS
        self.qtdeCadastrados = self.totalAmbulante()
        print(self.qtdeCadastrados, self.totalAmbulante())
        self.totalCadastrados.config(text=f'[TESTE DELETAR]: {self.qtdeCadastrados}') 

    # ======= METODO PARA ATUALIZAR O AMBULANTE =======
    def atualizarAmbulante(self):
        self.pegandoEntrysAmbulante()

        idAtualizar = self.id_entry.cget("text") # PEGAR ID

        # CONFERINDO SE O ID FOI ASSADO (DEU DOBLE CLICK)
        if not idAtualizar:
            messagebox.showinfo("Aviso!", "Não foi passado nenhum ID para atualizar!")
            return
        
        self.conecta_bd()

        # CONFERINDO SE USUÁRIO DEIXOU VAZIO ALGUMA SESSÃO
        # NOME:
        if(not self.nome):
            self.cursor.execute(''' SELECT nome from ambulante
                                where id = (?) ''', (idAtualizar))
            resultado = self.cursor.fetchone()
            if resultado:
                self.nome = resultado[0]

        # CPF:
        if(not self.cpf):
            self.cursor.execute(''' SELECT cpf from ambulante
                                where id = (?) ''', (idAtualizar))
            resultado = self.cursor.fetchone()
            if resultado:
                self.cpf = resultado[0]

        # RG:
        if(not self.rg):
            self.cursor.execute(''' SELECT rg from ambulante
                                where id = (?) ''', (idAtualizar))
            resultado = self.cursor.fetchone()
            if resultado:
                self.rg = resultado[0]

        # EMAIL:
        if(not self.email):
            self.cursor.execute(''' SELECT email from ambulante
                                where id = (?) ''', (idAtualizar))
            resultado = self.cursor.fetchone()
            if resultado:
                self.email = resultado[0]
        
        # TELEFONE:
        if(not self.telefone):
            self.cursor.execute(''' SELECT telefone from ambulante
                                where id = (?) ''', (idAtualizar))
            resultado = self.cursor.fetchone()
            if resultado:
                self.telefone = resultado[0]

        # CEP:
        if(not self.cep):
            self.cursor.execute(''' SELECT cep from ambulante
                                where id = (?) ''', (idAtualizar))
            resultado = self.cursor.fetchone()
            if resultado:
                self.cep = resultado[0]

        # CIDADE:
        if(not self.cidade):
            self.cursor.execute(''' SELECT cidade from ambulante
                                where id = (?) ''', (idAtualizar))
            resultado = self.cursor.fetchone()
            if resultado:
                self.cidade = resultado[0]

        # BAIRRO:
        if(not self.bairro):
            self.cursor.execute(''' SELECT bairro from ambulante
                                where id = (?) ''', (idAtualizar))
            resultado = self.cursor.fetchone()
            if resultado:
                self.bairro = resultado[0]

        # RUA:
        if(not self.rua):
            self.cursor.execute(''' SELECT rua from ambulante
                                where id = (?) ''', (idAtualizar))
            resultado = self.cursor.fetchone()
            if resultado:
                self.rua = resultado[0]

        # ATIVIDADE:
        if(not self.atividadeSelecao):
            self.cursor.execute(''' SELECT atividade from ambulante
                                where id = (?) ''', (idAtualizar))
            resultado = self.cursor.fetchone()
            if resultado:
                self.atividadeSelecao = resultado[0]

        # DATA DE NASCIMENTO:
        if(not self.dataNascimento):
            self.cursor.execute(''' SELECT data_nascimento from ambulante
                                where id = (?) ''', (idAtualizar))
            resultado = self.cursor.fetchone()
            if resultado:
                self.dataNascimento = resultado[0]

        # NOME DA MÃE:
        if(not self.nomeMae):
            self.cursor.execute(''' SELECT nome_mae from ambulante
                                where id = (?) ''', (idAtualizar))
            resultado = self.cursor.fetchone()
            if resultado:
                self.nomeMae = resultado[0]

        # RAÇA:
        if(not self.racaSelecao):
            self.cursor.execute(''' SELECT raca from ambulante
                                where id = (?) ''', (idAtualizar))
            resultado = self.cursor.fetchone()
            if resultado:
                self.racaSelecao = resultado[0]

        # GÊNERO
        if(not self.generoSelecao):
            self.cursor.execute(''' SELECT genero from ambulante
                                where id = (?) ''', (idAtualizar))
            resultado = self.cursor.fetchone()
            if resultado:
                self.generoSelecao = resultado[0]

        # DEFICIÊNCIA
        if(not self.possuiDeficienciaSelecao):
            self.cursor.execute(''' SELECT deficiencia from ambulante
                                where id = (?) ''', (idAtualizar))
            resultado = self.cursor.fetchone()
            if resultado:
                self.possuiDeficienciaSelecao = resultado[0]

        # ESCOLARIDADE
        if(not self.escolaridadeSelecao):
            self.cursor.execute(''' SELECT escolaridade from ambulante
                                where id = (?) ''', (idAtualizar))
            resultado = self.cursor.fetchone()
            if resultado:
                self.escolaridadeSelecao = resultado[0]

        # TRABALHA:
        if(not self.possuiTrabalhoSelecao):
            self.cursor.execute(''' SELECT trabalho from ambulante
                                where id = (?) ''', (idAtualizar))
            resultado = self.cursor.fetchone()
            if resultado:
                self.possuiTrabalhoSelecao = resultado[0]

        # FAIXA SALARIAL:
        if(not self.faixaSalarialSelecao):
            self.cursor.execute(''' SELECT faixa_salarial from ambulante
                                where id = (?) ''', (idAtualizar))
            resultado = self.cursor.fetchone()
            if resultado:
                self.faixaSalarialSelecao = resultado[0]

        ambulante = Ambulante(self.nome, self.cpf, self.rg, self.email, self.telefone, self.cep, self.cidade, self.bairro, self.rua,
                              self.atividadeSelecao, self.dataNascimento, self.nomeMae, self.racaSelecao, self.generoSelecao, 
                              self.possuiDeficienciaSelecao, self.escolaridadeSelecao, self.possuiTrabalhoSelecao, self.faixaSalarialSelecao)

        self.conn.commit()
        self.desconecta_bd()

        # CONFERÊNCIAS PARA ATUALIZAR
        # CONFERINDO SE CPF É VÁLIDO:
        if(ambulante.ConferirCpf() == False):
            messagebox.showinfo('Aviso!', f'O CPF do ambulante {ambulante.nome} passado foi inválido!')
            return
        
        # CONFERINDO SE O CPF/RG DO AMBULANTE JÁ FOI CADASTRADO
        self.conecta_bd()

        lista = self.cursor.execute('''SELECT cpf, rg FROM ambulante
                                       WHERE id != (?) ''', (idAtualizar))

        for elemento in lista:
            if(elemento[0] == ambulante.cpf):
                messagebox.showinfo('Aviso!' f'O CPF do ambulante {ambulante.nome} passado já foi cadastrado!')
                return
            elif(elemento[1] == ambulante.rg):
                messagebox.showinfo('Aviso!' f'O CPF do ambulante {ambulante.nome} passado já foi cadastrado!')
                return

        self.conn.commit()
        self.desconecta_bd()


        # CONFERINDO SE A DATA PASSADA É VÁLIDA:

        # CONFERINDO SE O AMBULANTE É MAIOR DE IDADE:
        if(ambulante.ConferirMaiorIdade() == False):
            messagebox.showinfo('Aviso!', f'O ambulante {self.nome} não é maior de idade')
            return
        
        self.conecta_bd()

        self.cursor.execute(''' UPDATE ambulante
                                SET nome = (?), cpf = (?), rg = (?), email = (?), telefone = (?), cep = (?), cidade = (?), bairro = (?), 
                                    rua = (?), atividade = (?), data_nascimento = (?), nome_mae = (?), raca = (?), genero = (?), 
                                    deficiencia = (?), escolaridade = (?), trabalha = (?), faixa_salarial = (?)
                                WHERE id = (?)''', (ambulante.nome, ambulante.cpf, ambulante.rg, ambulante.email, ambulante.telefone, 
                                                    ambulante.cidade, ambulante.cep, ambulante.bairro, ambulante.rua, ambulante.atividade, 
                                                    ambulante.data_nascimento, ambulante.nome_mae, ambulante.raca, ambulante.genero, 
                                                    ambulante.deficiencia, ambulante.escolaridade, ambulante.trabalha, ambulante.faixa_salarial,
                                                    idAtualizar))
        
        
        self.conn.commit()
        self.desconecta_bd()

        self.visualizarListaAmbulante()
        self.limpa_tela()

        # CONFERÊNCIA DOS AJUDATES: - CONTINUAR

        # PEGANDO AJUDANTES:
        '''listaAjudante = self.pegandoEntryAjudante()

        listaAjudanteDTO = []
        for ajudante in listaAjudante:
            listaAjudanteDTO.append(Ajudante(ajudante[0], ajudante[1], ajudante[2]))
                   
        if(self.ajudanteSelecao not in [0, 1, 2, 3]):
            messagebox.showerror('ERRO', f'Foi na passagem do nº de ajuantes')
            return
        
        ambulante.ajudantes = listaAjudanteDTO'''

        # CONFERIR SE TODOS OS CAMPOS FORAM PASSADOS:

        # CONFERINDO SE CPF É VÁLIDO E SE JÁ FOI CADASTRADO:

        # CONFERINDO SE A DATA PASSADA É VÁLIDA:

        # CONFERIR SE É MAIOR DE IDADE:
        
    
    # ======= MÉTODO PARA PEGAR O AMBULANTE E SUBI-LO AO FRAME 02 QUANDO FOR CLICADO 2X =======
    def onDoubleClick(self, event):
        self.limpa_tela()
        self.listaAmbulantes.selection()

        for n in self.listaAmbulantes.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13 = self.listaAmbulantes.item(n, 'values')

        idAmbulante = col1

        self.conecta_bd()

        self.cursor.execute('''
            SELECT 
                id, nome, cpf, rg, email, telefone, cep, cidade, bairro, rua, atividade, data_nascimento, 
                nome_mae, raca, genero, deficiencia, escolaridade, trabalha, faixa_salarial
            FROM ambulante
            WHERE id = (?)
        ''', (idAmbulante))        

        lista = self.cursor.fetchone()

        self.conn.commit()
        self.desconecta_bd()

        self.id = lista[0]
        self.id_entry.config(text=f'{self.id}')
        self.nome_entry.insert(tk.END, lista[1])
        self.cpf_entry.insert(tk.END, lista[2])
        self.rg_entry.insert(tk.END, lista[3])
        self.email_entry.insert(tk.END, lista[4])
        self.telefone_entry.insert(tk.END, lista[5])
        self.cep_entry.insert(tk.END, lista[6])
        self.cidade_entry.insert(tk.END, lista[7])
        self.bairro_entry.insert(tk.END, lista[8])
        self.rua_entry.insert(tk.END, lista[9])
        self.nomeMae_entry.insert(tk.END, lista[10])
        self.dataNascimento_calendario.insert(tk.END, lista[11])
        self.atividade_selecao.set(lista[12])
        self.raca_selecao.set(lista[13])
        self.genero_selecao.set(lista[14])
        self.possuiDeficiencia_selecao.set(lista[15])
        self.escolaridade_selecao.set(lista[16])
        self.possuiTrabalho_selecao.set(lista[17])
        self.faixaSalarial_selecao.set(lista[18])

    # ======= MÉTODO DE BUSCA DO AMBULANTE(NOME, CPF, ID) =======
    def buscarAmbulante(self):
        pass

    # |=======| MÉTODOS DE CONTAGEM DE AMBULANTES |=======|

    def totalAmbulante(self):

        self.conecta_bd()

        self.cursor.execute('''
        SELECT count(*) FROM ambulante
        ''')

        qtdeAmbulantes = self.cursor.fetchone()

        self.conn.commit()
        self.desconecta_bd()

        self.qtdeCadastrados = qtdeAmbulantes[0]

        return self.qtdeCadastrados
        
