# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c
# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:  
# Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.
# Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.
# Example:
# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) => should be 6: [4, -1, 2, 1]


def max_sequence(arr):
    counter = sum(arr)
    max_range = len(arr)-1
    
    if len(list(filter(lambda x: x >=0, arr))) == 0:
        return 0
    else:
        while max_range > 0:

            for i in range(0, len(arr)-max_range+1):
                eval = sum(arr[i:i+max_range])
                if eval > counter:
                    counter = eval
            max_range -= 1
        return counter


# Pruebas en consola // Test cases
array = [7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]
array2 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(max_sequence(array))
print(max_sequence(array2))
print(max_sequence([-2, -1, -3, -4, -1, -2, -1, -5, -4]))
print(max_sequence([]))


