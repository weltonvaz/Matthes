class Dog():
    """Uma tentativa simples de modelar um cachorro"""

    def __init__(self, name, age):
        """Inicializa os atributos name(nome) e age(idade)"""

        self.name = name
        self.age = age

    def sit(self):
        """Simula um cachorro sentado em resposta a um comando."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simula um cachorro rolando em resposta a um comando"""
        print(self.name.title() + " rolled over")
