import json

numbers = 2**57885161-1

filename = 'numbers.json'

with open(filename, 'w') as f_obj:
   json.dump(numbers,f_obj)
