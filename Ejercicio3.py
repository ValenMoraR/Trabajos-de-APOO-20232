# Crear un programa que genere una lista de números aleatorios y los imprima en pantalla.

import random 

    
num_list = []  # Definir la lista vacía fuera del bucle
for i in range(10):
    num_list.append(random.randint(1, 100))  # Agregar elementos a la lista
print(num_list)