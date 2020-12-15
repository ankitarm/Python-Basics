# bubblesort

def bubbleSort(x):
    l =len(x)
    for i in range(l-1):
        for j in range(l-i-1): # last elements are already sorted
            if x[j]>x[j+1]:
                x[j],x[j+1]=x[j+1],x[j]

    return x



def mergeSort(x):
    min = 0
    max = len(x) - 1
    mid = (max+min)//2
    print( min,max,mid)

if __name__ == '__main__':
    x = [9, 6, 3, 6, 7, 8]
    # print(bubbleSort(x))
    mergeSort(x)

