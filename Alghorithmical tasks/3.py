# 3. Rotate an Array
def rotate_arr(arr, k):
    listn = [""] * len(arr)
    
    for i in range(len(arr)):
        if i + k >= len(arr):
            listn[(i + k) % len(arr)] = arr[i]
        else:
            listn[i + k] = arr[i]

    return listn


print(rotate_arr([1, 2, 3], 2))
print(rotate_arr([1, 2, 3, 4], 3))