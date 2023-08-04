# Escribir un programa que determine si un número dado es par o impar.

def par_impar(num):
    if num % 2==0:
        print(f"The number {num} is pair")
    else: 
        print(f"The number {num} is odd")
    
num= int(input("Enter a number: "))
result= (par_impar(num))
    
