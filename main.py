#Fibonacci

num = 0
num_nuevo = 1
limit = int(input("Cuantos numeros fibonacci deseas?"))

for i in range(limit):
    print(num) #imprime el num inicial
    suma = num + num_nuevo #se suma el num viejo y el nuevo
    num = num_nuevo #el num nuevo ahora es el viejo
    num_nuevo = suma #la suma es el num nuevo



