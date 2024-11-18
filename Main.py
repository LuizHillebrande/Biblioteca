from Biblioteca import Biblioteca
from Pessoa import Pessoa
from Livro import Livro
from Emprestimo import Emprestimo
from Pessoa import Pessoa
import os

class Main:
    def __init__(self):
        self.biblioteca = Biblioteca()

    def limpa_tela(self):
        try:
            if os.name == "nt":
                os.system('cls')
            else:
                os.system('clear')
        except Exception as e:
            print(f"Erro ao limpar tela: {e}")

    def pausa(self):
        input("Pressione Enter para continuar...")

    def menu(self):
        self.limpa_tela()
        print("=== Sistema de Biblioteca ===")
        print("1. Cadastrar Pessoa")
        print("2. Cadastrar Livro")
        print("3. Realizar Empréstimo")
        print("4. Listar Pessoas")
        print("5. Listar Livros")
        print("6. Listar Livros Disponíveis")
        print("7. Listar Livros Emprestados")
        print("8. Realizar Devolução")
        print("0. Sair")
        opcao = int(input("Escolha uma opção: "))
        return opcao

    def cad_pessoa(self):
        nome = input("Nome: ")
        cpf = input("CPF: ")
        telefone = input("Telefone: ")
        self.biblioteca.cadastrar_pessoa(nome, cpf, telefone)
        self.pausa()

    def cad_livro(self):
        categoria = input("Categoria: ")
        titulo = input("Título: ")
        autor = input("Autor: ")

        
        self.biblioteca.cadastrar_livro(categoria, titulo, autor)

        # Pausa para continuar
        self.pausa()

    def emprestar(self):
        pessoa_index = int(input("Índice da Pessoa: "))
        livro_index = int(input("Índice do Livro: "))
        self.biblioteca.realizar_emprestimo(pessoa_index, livro_index)
        self.pausa()

    def listar(self, opcao):
        if opcao == 4:
            self.biblioteca.listar_pessoas()
        elif opcao == 5:
            self.biblioteca.listar_livros()
        elif opcao == 6:
            self.biblioteca.listar_livros_disponiveis()
        elif opcao == 7:
            self.biblioteca.listar_livros_emprestados()
        self.pausa()

    def devolver(self):
        livro_index = int(input("Índice do Livro para Devolução: "))
        self.biblioteca.devolver_livro(livro_index)
        self.pausa()

    def executa_opcao(self, opcao):
        if opcao == 1:
            self.cad_pessoa()
        elif opcao == 2:
            self.cad_livro()
        elif opcao == 3:
            self.emprestar()
        elif opcao in [4, 5, 6, 7]:
            self.listar(opcao)
        elif opcao == 8:
            self.devolver()
        elif opcao == 0:
            print("Encerrando o sistema...")
        else:
            print("Opção inválida!")
            self.pausa()

    def run(self):
        opcao = -1
        while opcao != 0:
            opcao = self.menu()
            self.executa_opcao(opcao)

if __name__ == "__main__":
    app = Main()
    app.run()
