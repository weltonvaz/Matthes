class Restaurant():
    """ Uma tentativa simples de modelar um cachorro. """
    def __init__(self, name, tipo):
        """ Incializa os atributos name e age """
        self.name = name
        self.tipo = tipo

    def describe_restaurant(self):
        """ Descriçao dos restautantes e estilo de cozinha. """
        print(self.name.title() + " estilo de Cozinha: " + self.tipo )

    def open_restaurant(self):
        """ Mostra se o restaurante esta aberto."""
        print("O Restaurante esta aberto")
