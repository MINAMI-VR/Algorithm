import random


def InsertSort(arr):
    i = 1
    while i < len(arr):
        j = i
        while j > 0:
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
        i += 1
    return arr


arr = [0] * random.randint(10, 20)
i = 0
while i < len(arr):
    arr[i] = random.randint(0, 100)
    i += 1
print(arr)
tmp = arr
sorted_arr = InsertSort(arr)
arr = tmp
print(sorted_arr)
print(sorted(arr) == sorted_arr)
