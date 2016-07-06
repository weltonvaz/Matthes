import os
os.system('clear')

def city_country_population(city, country, population=5000000):
    """ cidade, país e população."""
    if population:
        full_date = city + ', ' + country + ' - ' + str(population)
    else:
        full_date = city + ', ' + country

    return full_date.title()

print(city_country_population('Berlin','Alemanha'))