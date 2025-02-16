# 2. First Missing Positive Integer

def find_missing(arr):
    darr = list(range(min(arr), max(arr) + 1))

    for i in range(len(arr)):
        if arr[i] != darr[i]:
            return darr[i]
    
    return "No missing number"

print(find_missing([1, 2, 3, 4, 5]))
print(find_missing([1, 2, 3, 5]))