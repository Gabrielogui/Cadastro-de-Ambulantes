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
        )

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
        self.desconecta_bd


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


