#Quick Sort
#Sanchez Alcaraz Gabriela 33229, De la Torre Juan 33162, Machado Gonzalez Alex 28111

from random import randint
#imports the randint to generate the random numbers


start = 0 #this is the starting and stopping point of the random numbers
stop = 101
n = int(input("Input the amount of elements you want: ")) #this makes the user to input the amount of elements they want
numlist = [randint(start, stop) for i in range(n)]
print("Your original list: ", numlist)

#this function sorts the numbers in order with recursion, it will place the lower number to the left of the pivot and
#the bigger number to the right of the pivot.
def QuickSort(A, l, r):
    if l >= r: #
        return
    m = Partition(A, l, r) #A[m] is the final position
    QuickSort(A, l, m)
    QuickSort(A, m + 1, r)
    return

#this functin checks if the number is lower or equal than the pivot it changes place with the index
def Partition(A, l, r):
    x = A[l] #pivote
    j = l #index of the smaller number
    for i in range (l+1, r):
        if A[i] <= x:
            print(f"Corrida: {A}")
            j = j + 1 #the index changes +1
            A[j], A[i] = A[i], A[j] #the array A[j] will now be A[i]
    A[l], A[j] = A[j], A[l]


    return j

r = len(numlist)
x = QuickSort(numlist, 0, r)
print("Your QuickSort List: ", numlist)

#Last Update . 26/08/2021. Gabriela Sánchez Alcaraz Tijuana, Baja California
#Alex Machado Gonzalez and Juan De la Torre