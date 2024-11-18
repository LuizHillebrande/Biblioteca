from Pessoa import Pessoa
from Livro import Livro
from Emprestimo import Emprestimo
class Biblioteca:
    def __init__(self):
        self.pessoas = []  #lista de pessoas cadastradas
        self.livros = []    #lista de livros
        self.emprestimos = []  #lista de emprestimos

    
    def cadastrar_pessoa(self, nome, cpf, telefone):
        pessoa = Pessoa(nome, cpf, telefone)
        self.pessoas.append(pessoa) 
        print(f"Pessoa '{nome}' cadastrada com sucesso!")

    
    def cadastrar_livro(self, categoria, titulo, autor):
        self.livros.append(Livro(categoria, titulo, autor))
        print("Livro cadastrado com sucesso!")

    def get_pessoa_id(self): #pega o id
        pessoa_index = -1
        while pessoa_index < 0 or pessoa_index >= len(self.pessoas):
            pessoa_index = int(input("Índice da Pessoa: "))
            if pessoa_index < 0 or pessoa_index >= len(self.pessoas):
                print("Índice de Pessoa inválido.")
            else:
                print(self.pessoas[pessoa_index])
        return pessoa_index

    
    def realizar_emprestimo(self, pessoa_index, livro_index):
        if pessoa_index < len(self.pessoas) and livro_index < len(self.livros):
            livro = self.livros[livro_index]
            if livro.is_disponivel():
                pessoa = self.pessoas[pessoa_index]
                self.emprestimos.append(Emprestimo(pessoa, livro))
                livro.set_disponivel(False)
                print("Empréstimo realizado com sucesso!")
            else:
                print("O livro já está emprestado.")
        else:
            print("Pessoa ou Livro inválido!")

    # Método para devolver um livro
    def devolver_livro(self, livro_index):
        if livro_index < len(self.livros):
            livro = self.livros[livro_index]
            if not livro.is_disponivel():
                livro.set_disponivel(True)
                # Remover o empréstimo relacionado
                self.emprestimos = [emprestimo for emprestimo in self.emprestimos if emprestimo.get_livro() != livro]
                print("Livro devolvido com sucesso!")
            else:
                print("Este livro já está disponível.")
        else:
            print("Índice de livro inválido!")

    # Listar todas as pessoas cadastradas
    def listar_pessoas(self):
        for pessoa in self.pessoas:
            print(pessoa)

    # Listar todos os livros cadastrados
    def listar_livros(self):
        for livro in self.livros:
            print(livro)

    # Listar livros disponíveis
    def listar_livros_disponiveis(self):
        print("=== Livros Disponíveis ===")
        for livro in self.livros:
            if livro.is_disponivel():
                print(livro)

    # Listar livros emprestados
    def listar_livros_emprestados(self):
        print("=== Livros Emprestados ===")
        for emprestimo in self.emprestimos:
            print(emprestimo.get_livro())

    # Listar todos os empréstimos realizados
    def listar_emprestimos(self):
        for emprestimo in self.emprestimos:
            print(emprestimo)
