import unittest

from cities_function import name_city

class NamesTestCase(unittest.TestCase):
    """ Testes para 'city_function.py'."""

    def test_city_country(self):
        """ Nomes para testar Cidade/País"""

        testar_nomes = name_city('Berlin','Alemanha')
        self.assertEqual(testar_nomes, 'Berlin, Alemanha')

unittest.main()