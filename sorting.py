def bubblesort(initialArray):

    for i in range(len(initialArray) - 1):
        for j in range(len(initialArray) - 1 - i):
            print(initialArray[j], initialArray[j + 1])
            if initialArray[j] > initialArray[j + 1]:
                temp = initialArray[j]
                initialArray[j]  = initialArray[j + 1] 
                initialArray[j + 1] = temp
                print(initialArray)

    return initialArray