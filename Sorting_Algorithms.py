def bubbleSort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            yield array[:], j, j + 1 # Yied array and the indeces being compared
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                yield array[:], j, j + 1  # Yield the array and the indices of the compared elements

def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        yield array[:], j, i # Yied array and the indeces being compared
        while j >= 0 and array[j] > key:
            array[j + 1]= array[j]
            j -= 1
        array[j + 1] = key
        yield array[:], j + 1, i # Yield the array after placing the key