import matplotlib.pyplot as plt
import numpy as np
from playsound import playsound  # Optional - Makes the Sorting Visuals Better

"""  Visualization of Sorting Algorithms  """

def plot_sorting(array, sort_name):

    """
    This function plots the given array as a bar plot.

    """
    plt.clf()  # clear the previous plot
    plt.bar(range(len(array)), array, color = 'black')
    plt.title('Sorting Visualization - '+sort_name)
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.draw()
    plt.pause(0.001) 


"""  Algorithms  """

"""  1. Bubble Sort Algorithm  """

def bubble_sort(array):
    """
    This function implements the bubble sort algorithm.

    """
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                # swap the elements at indices j and j+1
                array[j], array[j+1] = array[j+1], array[j]

                # For the Visual: 
                plot_sorting(array, 'Bubble Sort')  # plot the array after each swap
                ## playsound('sound.wav')  # play sound after each swap
   

"""  2. Insertion Sort Algorithm  """

def insertion_sort(array):
    n = len(array)
    # Traverse through all array elements
    for i in range(1, n):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j] :
                array[j+1] = array[j]
                j -= 1
        array[j+1] = key

        # For the Visual:
        plot_sorting(array, 'Insertion Sort')


"""  3. Merge Sort Algorithm  """

def merge_sort(array):
    if len(array) > 1:
        mid = len(array)//2
        L = array[:mid]
        R = array[mid:]
        merge_sort(L)
        merge_sort(R)
        i, j, k = 0, 0, 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1
        plot_sorting(array, "Merge Sort")


"""  4. Selection Sort Algorithm  """

def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
        plot_sorting(array, "Selection Sort")  # plot the array after each swap


"""  5. Heap Sort Algorithm  """

def heapify(array, n, i):
    # Find largest among root, left child and right child
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[i] < array[left]:
        largest = left

    if right < n and array[largest] < array[right]:
        largest = right

    # If root is not the largest, swap with largest and continue heapifying
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        plot_sorting(array, "Heap Sort")
        heapify(array, n, largest)

def heap_sort(array):
    n = len(array)

    # Build max heap
    for i in range(n//2 - 1, -1, -1):
        heapify(array, n, i)

    # Extract elements from heap one by one
    for i in range(n-1, 0, -1):
        array[0], array[i] = array[i], array[0]
        plot_sorting(array, "Heap Sort")
        heapify(array, i, 0)


"""  6. Counting Sort Algorithm  """

def counting_sort(array):
    # Find the maximum element in the array
    max_val = max(array)
    
    # Create a counting array and initialize all elements to 0
    count = [0] * (max_val+1)
    
    # Count the frequency of each element in the array
    for i in range(len(array)):
        count[array[i]] += 1
        plot_sorting(count, "Counting Sort")

    # Modify the counting array to store the actual position of each element in the output array
    for i in range(1, len(count)):
        count[i] += count[i-1]

    # Create the output array and fill it with the sorted elements
    output = [0] * len(array)
    for i in range(len(array)):
        output[count[array[i]]-1] = array[i]
        count[array[i]] -= 1
        plot_sorting(output, "Counting Sort")
    
    # Copy the output array to the original array
    for i in range(len(array)):
        array[i] = output[i]


"""  7. Bucket Sort Algorithm  """

def bucket_sort(array):
    n = len(array)
    max_value = max(array)
    bucket = [[] for _ in range(n)]

    # put array elements in different buckets
    for i in range(n):
        index = int((n-1) * array[i] / max_value)
        bucket[index].append(array[i])
        plot_sorting(array, "Bucket Sort")

    # sort the elements of each bucket
    for i in range(n):
        bucket[i] = sorted(bucket[i])

    # concatenate the sorted buckets into the final array
    k = 0
    for i in range(n):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
            plot_sorting(array, "Bucket Sort")


"""  8. Quick Sort Algorithm  """
# Not going to implement it in the visual part 

def quick_sort(array, low, high):
    if low < high:
        # Partition the array
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] < pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
                #plot_sorting(array, "Quick Sort")
        array[i+1], array[high] = array[high], array[i+1]
        #plot_sorting(array, "Quick Sort")
        # Recursively sort the two halves
        quick_sort(array, low, i)
        quick_sort(array, i+2, high)


algorithms = {
        'bubble': bubble_sort,
        'insertion': insertion_sort,
        'merge': merge_sort,
        'selection': selection_sort,
        'heap': heap_sort,
        'counting': counting_sort,
        'bucket': bucket_sort
        }


def run(array):

    print('\nSelect a sorting algorithm:\n')
    for key in algorithms:
        print(key)
    algorithm = input()

    plt.ion()  # turn on interactive mode for continuous plotting
    plt.figure()
    plot_sorting(array, algorithm.capitalize()+' Sort')  # Unsorted 
    algorithms[algorithm](array)
    plt.ioff()
    plt.show()


while True:

    # Example 
    run(array = np.random.randint(0, 100, 20))