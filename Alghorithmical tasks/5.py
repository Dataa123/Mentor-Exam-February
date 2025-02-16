# 5. Product of Array Except Self
def product_of_arr(arr):
    res = []

    for i in range(len(arr)):
        list1 = [i for i in arr]
        list1.pop(i)

        x = 1
        for i in list1:
            x *= i
        res.append(x)

    return res

# print(product_of_arr([1, 2, 3]))
# print(product_of_arr([1, 2, 3, 4]))


# one liner

def product_of_arr_one_liner(arr):
    return [eval("*".join(y)) for y in [[str(arr[x]) for x in range(len(arr)) if x != i] for i in range(len(arr))]]

print(product_of_arr_one_liner([1, 2, 3]))
print(product_of_arr_one_liner([1, 2, 3, 4]))