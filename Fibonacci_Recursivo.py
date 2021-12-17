#Fibonacci Recursivo

#Sanchez Alcaraz Gabriela

#Se pide el numero que se desea calcular segun la secuencia fibonacci

n = int(input("Cuantos numeros fibonacci deseas?"))

#Se crea una funcion donde se calcula el fibonacci, si es mayor que 1, se suman los numeros donde se encuentre la
# posicion del fib en la tabla

def fib(n):
    if (n<=1):
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(n))


#Sanchez Alcaraz Gabriela, 15 de agosto del 2020