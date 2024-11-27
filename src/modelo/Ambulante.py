import re
from datetime import datetime

# |=======| CLASSE AMBULANTE |=======|
class Ambulante():
    # ======= CONSTRUTOR =======
    def __init__(self, nome, cpf, rg, email, telefone, cep, cidade, bairro, rua, atividade, data_nascimento, 
                 nome_mae, raca, genero, deficiencia, escolaridade, trabalha, faixa_salarial):
        self.id              = None
        self.nome            = nome
        self.cpf             = cpf
        self.rg              = rg
        self.email           = email
        self.telefone        = telefone
        self.cep             = cep
        self.cidade          = cidade
        self.bairro          = bairro
        self.rua             = rua
        self.atividade       = atividade
        self.data_nascimento = data_nascimento
        self.nome_mae        = nome_mae
        self.raca            = raca
        self.genero          = genero
        self.deficiencia     = deficiencia
        self.escolaridade    = escolaridade
        self.ajudantes       = []
        self.trabalha        = trabalha
        self.faixa_salarial  = faixa_salarial

        # PEGAR NA HORA QUE FOR INSERIDO:
        self.hora_atualizacao = None

        # PEGAR AUTOMÁTICO - TELEFONE:
        self.ddd_celular  = None
        self.ddd_whatsapp = None
        self.whatsapp     = None

    # ======= MÉTODOS =======

    # CONFERIR CPF:
    def ConferirCpf(self):
        # PEGA APENAS OS DIGITOS, RETIRANDO OS CHAR ESPECIAIS
        numeros = [int(digito) for digito in self.cpf if digito.isdigit()]

        # ETAPAS DE VALIDAÇÕES DO CPF:
        formatacao   = False
        qtde_digitos = False
        validacao01  = False
        validacao02  = False

        # Conferindo a foratação
        if re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', self.cpf):
            formatacao = True

        # Conferindo o tamanho:
        if(len(numeros) == 11):
            qtde_digitos = True

            # Primeira validação:
            soma_produtos01   = sum(a*b for a, b in zip (numeros[0:9], range (10, 1, -1)))
            digito_esperado01 = (soma_produtos01 * 10 % 11) % 10  

            if numeros[9] == digito_esperado01:
                validacao01 = True       

            # Segunda Validação:
            soma_produtos02   = sum(a*b for a, b in zip(numeros [0:10], range (11, 1, -1)))
            digito_esperado02 = (soma_produtos02 *10 % 11) % 10

            if numeros[10] == digito_esperado02:
                validacao02 = True
        
        # Conferindo se todas as validações são verdadeiras
        if ((formatacao == True) and (qtde_digitos == True) and (validacao01 == True) and (validacao02 == True)):
            return True
        else:
            print(formatacao, qtde_digitos, validacao01, validacao02)
            return False
    
    # CONFERIR SE É MAIOR DE IDADE
    def ConferirMaiorIdade(self):
        # Define o formato de data brasileira (dd/mm/aaaa)
        formato_data = "%d/%m/%Y"
        
        # CONFERIR SE FOI ENVIADO LETRA OU NÚMERO - FAZER

        print(len(self.data_nascimento))

        if(len(self.data_nascimento) != 10):
                return False

        # Converte a data de nascimento do formato string para um objeto datetime
        data_nascimento = datetime.strptime(self.data_nascimento, formato_data)
        
        # Obtém a data atual
        data_atual = datetime.now()
        
        # Calcula a idade
        idade = data_atual.year - data_nascimento.year

        # Ajusta a idade se o aniversário ainda não aconteceu este ano
        if (data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day):
            idade -= 1
        
        if(idade >= 18):
            return True
        else:
            return False

# |=======| CLASSE AJUDANTE |=======|
class Ajudante():
    # ======= CONSTRUTOR =======
    def __init__(self, nome_ajudante, cpf_ajudante, dataNascimeto):
        self.nome_ajudante  = nome_ajudante
        self.cpf_ajudante   = cpf_ajudante
        self.dataNascimento = dataNascimeto

        # AMBULANTE VINCULADO - CONTINUAR DEPOIS
        #self.idAmbulante    = idAmbulante

    # ======= MÉTODOS =======

    # CONFERIR CPF:
    def ConferirCpf(self):
        # PEGA APENAS OS DIGITOS, RETIRANDO OS CHAR ESPECIAIS
        numeros = [int(digito) for digito in self.cpf if digito.isdigit()]

        # ETAPAS DE VALIDAÇÕES DO CPF:
        formatacao   = False
        qtde_digitos = False
        validacao01  = False
        validacao02  = False

        # Conferindo a foratação
        if re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', self.cpf):
            formatacao = True

        # Conferindo o tamanho:
        if(len(numeros) == 11):
            qtde_digitos = True

            # Primeira validação:
            soma_produtos01   = sum(a*b for a, b in zip (numeros[0:9], range (10, 1, -1)))
            digito_esperado01 = (soma_produtos01 * 10 % 11) % 10  

            if numeros[9] == digito_esperado01:
                validacao01 = True       

            # Segunda Validação:
            soma_produtos02   = sum(a*b for a, b in zip(numeros [0:10], range (11, 1, -1)))
            digito_esperado02 = (soma_produtos02 *10 % 11) % 10

            if numeros[10] == digito_esperado02:
                validacao02 = True
        
        # Conferindo se todas as validações são verdadeiras
        if ((formatacao == True) and (qtde_digitos == True) and (validacao01 == True) and (validacao02 == True)):
            return True
        else:
            print(formatacao, qtde_digitos, validacao01, validacao02)
            return False
        

    # CONFERIR SE É MAIOR DE IDADE
    def ConferirMaiorIdade(self):
        # Define o formato de data brasileira (dd/mm/aaaa)
        formato_data = "%d/%m/%Y"
        
        # Converte a data de nascimento do formato string para um objeto datetime
        data_nascimento = datetime.strptime(self.data_nascimento, formato_data)
        
        # Obtém a data atual
        data_atual = datetime.now()
        
        # Calcula a idade
        idade = data_atual.year - data_nascimento.year

        # Ajusta a idade se o aniversário ainda não aconteceu este ano
        if (data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day):
            idade -= 1
        
        if(idade >= 18):
            return True
        else:
            return False
