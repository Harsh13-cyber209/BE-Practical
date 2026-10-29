import random
import time

def partition(arr, low, high):
    pivot = arr[high]
    i = low-1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j] , arr[i]
        
    arr[i+1], arr[high] = arr[high] , arr[i+1]
    
    return i + 1

def deterministic_quicksort(arr, low, high):
    
    if low < high:
        pi  = partition(arr,low,high)
        
        deterministic_quicksort(arr,low,pi-1)
        deterministic_quicksort(arr, pi+1, high)
        
def randomized_partition(arr,low,high):
    
    random_index = random.randint(low,high)
    arr[random_index], arr[high] = (arr[high], arr[random_index])
    
    return partition(arr,low,high)

n = int(input("Enter number of elements: "))
arr =[]

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    arr.append(num)
    

arr1 = arr.copy()
arr2 = arr.copy()

print("\nOriginal Array:", arr)

start = time.perf_counter()
deterministic_quicksort(arr1, 0, n-1)
end = time.perf_counter()

print("\nDeterministic Quick Sort: ")
print("Sorted Array: ", arr1)
print("Execution Time: ", end-start, "seconds")