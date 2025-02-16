# 4. Find All Anagrams in a String

def find_anagrams(s, p):
    return sorted(s) == sorted(p)

print(find_anagrams("abc", "cab"))
print(find_anagrams("abch", "caab"))