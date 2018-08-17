import random


def SequentialSearch(arr, val):
    i = 0
    while i < len(arr):
        if arr[i] == val:
            return i, val
        i += 1


arr = [0] * random.randint(10, 20)
i = 0
while i < len(arr):
    arr[i] = random.randint(0, 100)
    i += 1
val = arr[random.randint(0, len(arr))]
print(arr)
print(SequentialSearch(arr, val))
