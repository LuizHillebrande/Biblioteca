class Emprestimo:
    def __init__(self, pessoa, livro):
        self.pessoa = pessoa  # Pessoa que realiza o empréstimo
        self.livro = livro    # Livro emprestado

    # Métodos getters
    def get_pessoa(self):
        return self.pessoa

    def get_livro(self):
        return self.livro

    def __str__(self):
        return f"Emprestimo{{pessoa={self.pessoa.get_nome()}, livro={self.livro.get_titulo()}}}"
