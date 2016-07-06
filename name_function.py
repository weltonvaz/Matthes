import os
os.system('clear')

def get_formatted_name(first, last, middle=''):
    """ Gera um nome completo formatado de modo elegante."""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last

    return full_name.title()

#print(get_formatted_name('janis','joplin'))
