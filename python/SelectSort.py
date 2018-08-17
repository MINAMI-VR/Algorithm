import random


def SelectSort(arr):
    i = 0
    while i < len(arr):
        min_i = i
        j = i + 1
        while j < len(arr):
            if arr[min_i] > arr[j]:
                min_i = j
            j += 1
        tmp = arr[min_i]
        j = min_i
        while i < j:
            arr[j] = arr[j - 1]
            j -= 1
        arr[i] = tmp
        i += 1
    return arr


arr = [0] * random.randint(10, 20)
i = 0
while i < len(arr):
    arr[i] = random.randint(0, 100)
    i += 1
print(arr)
tmp = arr
sorted_arr = SelectSort(arr)
arr = tmp
print(sorted_arr)
print(sorted(arr) == sorted_arr)
