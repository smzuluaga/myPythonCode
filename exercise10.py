# The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}. What if the string is empty? Then the result should be empty object literal, {}.

def count(s):
    import collections
    return collections.Counter(s)

#Pruebas en consola / test cases
print(count('aba'))
print(count(''))
print(count('Holo'))