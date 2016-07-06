import unittest
<<<<<<< HEAD

from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """ Testes para 'name_function.py'."""

    def test_first_last_name(self):
        """ Nomes como 'Janes Joplin' funcionam? """
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """ Nomes como 'Wolfgang Amadeus Mozart' funcionam? """
        formatted_name = get_formatted_name('wolfgang', 'mozart','amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()
=======
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """ Testes para 'city_function.py'."""

    def test_first_last_name(self):
        """ Nomes como 'Janis Joplin' funcionam? """
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEquals(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """" Nomes como 'Wolfgang Amadeus Mozart' funcionam? """
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEquals(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()
>>>>>>> 6c462b875e6a1a37ebac18cec3bce6b7525c125e
