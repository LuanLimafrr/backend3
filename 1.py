class Carro:
    rodas = 4  # Atributo de classe

    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

    def ligar(self):
        print(f'O carro {self.marca} ({self.ano}) está ligado')

    @classmethod
    def mudar_numero_rodas(cls, novas_rodas):
        cls.rodas = novas_rodas
        print(f'Agora todos os carros têm {cls.rodas} rodas')

    @staticmethod
    def calcular_idade(ano_fabricacao, ano_atual):
        return ano_atual - ano_fabricacao
    


marca = input("Digite a marca do carro: ")
ano = int(input("Digite o ano do carro: "))

meu_carro = Carro( marca, ano)

meu_carro.ligar()


ano_atual = 2025

idade = Carro.calcular_idade(meu_carro)
print(f'O carro tem {idade} anos.')


