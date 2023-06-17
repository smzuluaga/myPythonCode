# https://www.codewars.com/kata/585d7d5adb20cf33cb000235/python
# There is an array with some numbers. All numbers are equal except for one. Try to find it! It’s guaranteed that array contains at least 3 numbers. The tests contain some very huge arrays, so think about performance. This is the first kata in series:
# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

def find_uniq(arr):
    import collections
    counter = list(collections.Counter(arr).items()) 
    if (counter[0][1]>counter[1][1]):
        return counter[1][0]
    else:
        return counter[0][0]
    
print (find_uniq([ 1, 1, 1, 2, 1, 1 ]))
print (find_uniq([ 0, 0, 0.55, 0, 0 ]))
print (find_uniq([ 3, 10, 3, 3, 3 ]))