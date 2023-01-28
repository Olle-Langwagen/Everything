import random
import time
import statistics
min = 1
max = 6
listlängd = 0
allakast = []
kast1lista = []
kast2lista = []
rolls = input("Hur många gånger vill du kasta tärningen?: ")

for i in range(int(rolls)):
    startTime = time.time()
    
    kast1 = (random.randint(min, max))
    kast2 = (random.randint(min, max))
    kast1lista.append(kast1)
    kast2lista.append(kast2)
    allakast.append(kast1)
    allakast.append(kast2)
    
for index, obj in enumerate(kast1lista):
    listlängd = listlängd + 1

for i in range(len(allakast)):
    pass




def partition(arr, low, high):
    i = (low-1)         # index av det mindre
    pivot = arr[high]     # pivot
 
    for j in range(low, high):
 
        # om den är mindre än eller
        # kollar om den är lika med pivot
        if arr[j] <= pivot:
 
            # index av mindre
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
 

# arr är allakast
# low är start index
# high är slut index

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
 
        # pi delar upp indexet

        pi = partition(arr, low, high)
 
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
 
 
arr = allakast

n = len(arr)
quickSort(arr, 0, n-1)
print("Sorterad Lista:")
#for i in range(n):
    #print("%d" % arr[i])
alla_kast_resultat = allakast
print(allakast)
median = (alla_kast_resultat[len(alla_kast_resultat) // 2] + alla_kast_resultat[(len(alla_kast_resultat) - 1) // 2]) / 2

print("median är: ", median)
executionTime = (time.time() - startTime)

print('Execution time in seconds: ' + str(executionTime))
