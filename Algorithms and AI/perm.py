from itertools import permutations
list1 = ["a", "b", "c"]

for i in list(permutations(list1)):
    print("<".join(i))