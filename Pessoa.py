class Pessoa:
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    # Getters e Setters
    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_cpf(self):
        return self.cpf

    def set_cpf(self, cpf):
        self.cpf = cpf

    def get_telefone(self):
        return self.telefone

    def set_telefone(self, telefone):
        self.telefone = telefone

    def __str__(self):
        return f"Pessoa{{nome='{self.nome}', cpf='{self.cpf}', telefone='{self.telefone}'}}"
