""" Uma classe que pode ser usada para representar um carro!"""

class Car():
    """ Uma tentativa simples de representar. """

    def __init__(self, make, model, year):
        """ Inicializa os atributos que descrevem um carro."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """ Exibe uma frase que mostra a milhagem do carro."""
        long_name = str(self.year) + self.make + self.model
        return long_name

    def read_odometer(self):
        """ Exibe uma frase que mostra a milhagem do carro. """
        print("This car has " + str(self.odometer_reading) + "miles on it.")

    def update_odometer(self, mileage):
        """
        Define o valor de leitura do hodômetro com o valor especificado
        Rejeita a alteração se tentativa de definir um valor menor para o
        hodômetro.
        """
        if miliage >= self.odometer_reading:
            self.odometer_reading = miliage
        else:
            print("you can't roll back an odometer!")

    def increment_odometer(self, miles):
        """ Soma a quantidade especificada ao valor de leitura do hodômetro."""
        self.odometer_reading += miles
