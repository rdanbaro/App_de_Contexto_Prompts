# from collections import defaultdict

# # boton_dict = {
# #     original_text: str,
# #     truncated_text: str

# # }
# boton_dict = {}

# #ddict = defaultdict(list)
# boton_dict['original_text'] = "hola"
# boton_dict['truncate_text'] = "fuck you"

# # ddict['original'] = 'hola'
# # ddict['corto'] = 'q bola'

# #print(ddict)
# print(boton_dict)

from collections import defaultdict

default_diccionario = defaultdict(int)
default_diccionario['manzana'] = 0
default_diccionario['naranja'] = 1
default_diccionario['banana'] = 2

print(default_diccionario['manzana'])  # Salida: 3
print(default_diccionario['pera'])     # Salida: 0 (valor predeterminado para una clave inexistente es 0)
print(default_diccionario['pera'])     # Salida: 0 (valor predeterminado para una clave inexistente es 0)