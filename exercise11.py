# https://www.codewars.com/kata/550554fd08b86f84fe000a58/train/python
# Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.
# Example = 
# a1 = ["arp", "live", "strong"] a2 = ["lively", "alive", "harp", "sharp", "armstrong"] // returns ["arp", "live", "strong"]
# a1 = ["tarp", "mice", "bull"] a2 = ["lively", "alive", "harp", "sharp", "armstrong"] // returns []

def in_array(array1, array2):
    r = []
    for i in range(0,len(array1)):
        for j in range(0,len(array2)):
            if array1[i] in array2[j] and not array1[i] in r:
                r.append(array1[i])
                break
    r.sort()
    return r


#Pruebas en consola / Test cases
arr1 = ["live", "arp", "strong"] 
arr2 = ["lively", "alive", "harp", "sharp", "armstrong"]
print(in_array(arr1,arr2))


arr3 = ["arp", "mice", "bull"] 
arr4 = ["lively", "alive", "harp", "sharp", "armstrong"]
print(in_array(arr3,arr4))