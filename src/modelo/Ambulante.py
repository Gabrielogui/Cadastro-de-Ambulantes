# |=======| CLASSE AMBULANTE |=======|
class Ambulante():
    # ======= CONSTRUTOR =======
    def __init__(self):
        self.id              = None
        self.nome            = None
        self.cpf             = None
        self.rg              = None
        self.email           = None
        self.telefone        = None
        self.cep             = None
        self.cidade          = None
        self.bairro          = None
        self.rua             = None
        self.atividade       = None
        self.data_nascimento = None
        self.nome_mae        = None
        self.raca            = None
        self.genero          = None
        self.deficiencia     = None
        self.escolaridade    = None
        self.ajudantes       = []
        self.trabalha        = None
        self.faixaSalarial   = None

        # PEGAR NA HORA QUE FOR INSERIDO:
        self.hora_atualizacao = None

        # PEGAR AUTOMÁTICO - TELEFONE:
        self.ddd_celular  = None
        self.ddd_whatsapp = None
        self.whatsapp     = None

    # ======= MÉTODOS =======

# |=======| CLASSE AJUDANTE |=======|
class Ajudante():
    def __init__(self):
        self.nome           = None
        self.cpf            = None
        self.dataNascimento = None

        # AMBULANTE VINCULADO
        self.idAmbulante    = None

