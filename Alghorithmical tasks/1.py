# 1. Find the Majority Element

def find_majority(arr):
    return list(set([i for i in arr if arr.count(i) > len(arr) / 2]))[0] if list(set([i for i in arr if arr.count(i) > len(arr) / 2])) != [] else None

print(find_majority([1, 1, 1, 2, 2, 2]))
print(find_majority([1, 1, 1, 1, 2, 2, 2]))