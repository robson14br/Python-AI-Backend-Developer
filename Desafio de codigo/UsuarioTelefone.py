class UsuarioTelefone:
    # TODO: Defina um método especial `__init__`, que é o construtor da classe.
    # O método `__init__`, irá inicializar os atributos da classe: `nome`, `numero` e `plano`.
    def __init__(self, nome, numero, plano):
        self.__nome = nome
        self.__numero = numero
        self.__plano = plano

    # TODO: Aplique o conceito de encapsulamento, onde os atributos serão encapsulados dentro da classe.
    # Getters
    @property
    def nome(self):
        return self.__nome

    @property
    def numero(self):
        return self.__numero

    @property
    def plano(self):
        return self.__plano

    # Setters
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @plano.setter
    def plano(self, plano):
        self.__plano = plano

    # A classe `UsuarioTelefone` define um método especial `__str__`, que retorna uma representação em string do objeto.
    def __str__(self):
        return f"Usuário {self.nome} criado com sucesso."

# Entrada:
nome = input()  
numero = input()  
plano = input()  

# TODO: Crie um novo objeto `UsuarioTelefone` com os dados fornecidos:
usuario = UsuarioTelefone(nome, numero, plano)

# Imprimir a mensagem de sucesso
print(usuario)
