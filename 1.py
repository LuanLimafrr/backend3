class carro:
    rodas = 4
    
    
def __init__ (self, marca, ano):
    self.marca = marca
    self.ano = ano
    

def ligar(self):
    print(f'O carro{self.marca}({self.ano}) está ligado')
    


@classmethod
def mudar_numero_rodas(cls, novas_rodas):
    cls.rodas = novas_rodas
    print(f'Agora todos os carros tem {cls.rodas} rodas')
    
    
@staticmethod
def calcular_idade(ano_fabricacao, ano_atual):
    return ano_atual - ano_fabricacao