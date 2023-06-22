# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/python
# You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.
# Example: 
#   *[7, 1]  =>  [1, 7]
#   *[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
#   *[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

def sort_array(source_array):
    odd_num = sorted(list(filter(lambda num: num % 2 != 0, source_array)))
    new_arr = []
    counter = 0

    for i in range (0,len(source_array)):
        if source_array[i] %2 != 0 :
            new_arr.append(odd_num[counter])
            counter +=1
        else:
            new_arr.append(source_array[i])
            
    
    return new_arr

#Pruebas en consola // Test cases
print(sort_array([5, 3, 2, 8, 1, 4]))