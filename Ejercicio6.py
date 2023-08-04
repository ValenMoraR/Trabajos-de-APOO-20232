# Crear un programa que calcule la suma de los números en una lista dada.

list_num= [3,2,44,95,39,1,2,6]

def calculate_sum(list):
    sum=0
    for num in list:
        sum += num
    print(f"La suma de la lista dada es de: {sum}")

result= (calculate_sum(list_num))


        