import numpy as np

def bubble_sort(n):
    arr = np.random.randint(0, 100, n)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def linear_search(n):
    for i in range(n):
        if i == n-1:
            return i

def binary_search(n):
    arr = list(range(n))
    target = -1
    left, right = 0, n-1
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid+1
        else:
            right = mid-1

def nested_loops(n):
    for i in range(n):
        for j in range(n):
            pass
