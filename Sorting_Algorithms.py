def bubblesort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            yield array[:], j, j + 1 #Yied array and indeces being compared
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                yield array[:], j, j + 1  # Yield the array and the indices of the compared elements
