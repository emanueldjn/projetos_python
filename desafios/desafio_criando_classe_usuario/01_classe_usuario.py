# Crie uma classe UsuarioTelefone.  
class UsuarioTelefone:
    # Defina um método especial `__init__`, que é o construtor da classe.
    # O método `__init__`, irá inicializar os atributos da classe: `nome`, `numero` e `plano`.
    
    def __init__(self, nome, numero, plano):
    
        # Aplique o conceito de encapsulamento, onde os atributos serão encapsulados dentro da classe.
        self.nome = nome
        self.numero = numero
        self.plano = plano
    # A classe `UsuarioTelefone` define um método especial `__str__`, que retorna uma representação em string do objeto.
    def __str__(self):
        return f"Usuario {self.nome} criado com sucesso."
    
  
# Entrada 
nome = input("Nome do usuário: ")
numero = input("Número de telefone: ")
plano = input("Plano: ")

# Crie um novo objeto `UsuarioTelefone` com os dados fornecidos:
usuario = UsuarioTelefone(nome, numero, plano)
print(usuario)