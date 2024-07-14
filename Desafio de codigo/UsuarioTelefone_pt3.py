# Classe UsuarioTelefone e o encapsulamento dos atributos nome, numero e plano:
class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.__nome = nome
        self.__numero = numero
        self.__plano = plano

    # Encapsulamento
    @property
    def nome(self):
        return self.__nome

    @property
    def numero(self):
        return self.__numero

    @property
    def plano(self):
        return self.__plano

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @plano.setter
    def plano(self, plano):
        self.__plano = plano

    # Método para fazer uma chamada telefônica
    def fazer_chamada(self, destinatario, duracao):
        custo = self.plano.custo_chamada(duracao)
        if self.plano.deduzir_saldo(custo):
            return f"Chamada para {destinatario} realizada com sucesso. Saldo: ${self.plano.verificar_saldo():.2f}"
        else:
            return "Saldo insuficiente para fazer a chamada."

# Classe Plano, representa o plano de um usuário de telefone:
class Plano:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial

    # Método para verificar saldo
    def verificar_saldo(self):
        return self.__saldo

    # Método para calcular o custo de uma chamada
    def custo_chamada(self, duracao):
        return 0.10 * duracao

    # Método para deduzir o valor do saldo do plano
    def deduzir_saldo(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            return True
        else:
            return False

# Classe UsuarioPrePago, herda de UsuarioTelefone:
class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))

# Recebendo as informações do usuário:
nome = input("Nome do usuário: ")
numero = input("Número do telefone: ")
saldo_inicial = float(input("Saldo inicial do plano: "))

# Criando objeto de UsuarioPrePago com os dados fornecidos:
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)

# Recebendo informações da chamada:
destinatario = input("Número do destinatário: ")
duracao = int(input("Duração da chamada em minutos: "))

# Chamando o método fazer_chamada do objeto usuario_pre_pago e imprimindo o resultado:
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))
