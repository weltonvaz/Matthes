<<<<<<< HEAD
=======
import os
os.system('clear')

>>>>>>> 6c462b875e6a1a37ebac18cec3bce6b7525c125e
def get_formatted_name(first, last, middle=''):
    """ Gera um nome completo formatado de modo elegante."""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
<<<<<<< HEAD
    return full_name.title()
=======

    return full_name.title()

#print(get_formatted_name('janis','joplin'))
>>>>>>> 6c462b875e6a1a37ebac18cec3bce6b7525c125e
