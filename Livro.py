class Livro:
    def __init__(self, categoria, titulo, autor):
        self.categoria = categoria
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True  #disponivel por padrao

    # Métodos Getters e Setters
    def get_categoria(self):
        return self.categoria

    def set_categoria(self, categoria):
        self.categoria = categoria

    def get_titulo(self):
        return self.titulo

    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_autor(self):
        return self.autor

    def set_autor(self, autor):
        self.autor = autor

    def is_disponivel(self):
        return self.disponivel
    
     #método para alterar a disponibilidade do livro
    def set_disponivel(self, disponivel):
        self.disponivel = disponivel

    def __str__(self):
        return f"Livro{{categoria='{self.categoria}', titulo='{self.titulo}', autor='{self.autor}', disponivel={'Sim' if self.disponivel else 'Não'}}}"
