
funcionariosParaCadastrar = [
    {"nome": "Pablo", "sobrenome": "Araujo", "idade": 34, "altura": 1.71, "temHabilitacao": True},
    {"nome": "Ana", "sobrenome": "Silva", "idade": 28, "altura": 1.65, "temHabilitacao": False},
    {"nome": "Carlos", "sobrenome": "Souza", "idade": 40, "altura": 1.80, "temHabilitacao": True},
    {"nome": "Luan", "sobrenome": "Lima", "idade": 23, "altura": 1.61, "temHabilitacao": True},
    {"nome": "Luan", "sobrenome": "Lima", "idade": 23, "altura": 1.61, "temHabilitacao": True},
    {"nome": "Ruan", "sobrenome": "Barros", "idade": 21, "altura": 1.65, "temHabilitacao": False},
    {"nome": "Rhyan", "sobrenome": "Henrique", "idade": 18, "altura": 1.70, "temHabilitacao": False}
]

cadastrosParaEnviarParaOBanco = []


class Pessoa:
    def __init__(self, nome, sobrenome, idade, altura, temHabilitacao):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.altura = altura
        self.temHabilitacao = temHabilitacao


def cadastrar_funcionarios(lista_de_dicionarios):
    for dados in lista_de_dicionarios:
        pessoa = Pessoa(
            nome=dados["nome"],
            sobrenome=dados["sobrenome"],
            idade=dados["idade"],
            altura=dados["altura"],
            temHabilitacao=dados["temHabilitacao"]
        )
        cadastrosParaEnviarParaOBanco.append(pessoa)
        


def salvar_cadastros(lista_de_pessoas):
    for pessoa in lista_de_pessoas:
        print(f"O usuário {pessoa.nome} {pessoa.sobrenome} foi salvo com sucesso.")
        
        



cadastrar_funcionarios(funcionariosParaCadastrar)
salvar_cadastros(cadastrosParaEnviarParaOBanco)
