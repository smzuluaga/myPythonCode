#In this kata, you will write a function that returns the positions and the values of the "peaks" (or local maxima) of a numeric array. For example, the array arr = [0, 1, 2, 5, 1, 0] has a peak at position 3 with a value of 5 (since arr[3] equals 5). The output will be returned as an object with two properties: pos and peaks. Both of these properties should be arrays. If there is no peak in the given array, then the output should be {pos: [], peaks: []}. All input arrays will be valid integer arrays (although it could still be empty), so you won't need to validate the input. The first and last elements of the array will not be considered as peaks (in the context of a mathematical function, we don't know what is after and before and therefore, we don't know if it is a peak or not).
# Example: pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]) should return {pos: [3, 7], peaks: [6, 3]} (or equivalent in other languages)
# Also, beware of plateaus !!! [1, 2, 2, 2, 1] has a peak while [1, 2, 2, 2, 3] and [1, 2, 2, 2, 2] do not. In case of a plateau-peak, please only return the position and value of the beginning of the plateau. For example: pickPeaks([1, 2, 2, 2, 1]) returns {pos: [1], peaks: [2]} (or equivalent in other languages)


def pick_peaks2(arr):
    dictionary = {}
    dictionary['pos'] = [num for num in range(1,len(arr)-1) if arr[num-1]< arr[num] and arr[num] > arr[num+1] or arr[num-1] == arr[num] and arr[num] > arr[num+1]]
    dictionary['peaks'] = [arr[num] for num in range(1,len(arr)-1) if arr[num-1]< arr[num] and arr[num] > arr[num+1] or arr[num-1] == arr[num] and arr[num] > arr[num+1]]
    return dictionary

def pick_peaks(arr):    
    peaks = []
    pos =[]
    dictionary = {}

    for i in range(1,len(arr)-1):
        if arr[i-1]< arr[i]:
            for j in range (i,len(arr)-1):
                if arr[j] > arr[j+1]:
                    pos.append(i)
                    peaks.append(arr[i])
                    break
                elif arr[j] < arr[j+1]:
                    break
                elif arr[j] == arr[j+1]:
                    continue          
        else:
            continue
    dictionary['pos'] = pos
    dictionary['peaks'] = peaks

    return dictionary

# Pruebas en consola / Test cases 
print(pick_peaks([1,2,3,6,4,1,2,3,2,1])) # {"pos":[3,7], "peaks":[6,3]}   
print(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1])) # {"pos":[3,7,10], "peaks":[6,3,2]}   
print(pick_peaks([2,1,3,1,2,2,2,2,1]))  # {"pos":[2,4], "peaks":[3,2]}
print(pick_peaks([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3])) #{"pos":[2,7,14,20], "peaks":[5,6,5,5]}
print(pick_peaks([18, 18, 10, -3, -4, 15, 15, -1, 13, 17, 11, 4, 18, -4, 19, 4, 18, 10, -4, 8, 13, 9, 16, 18, 6, 7])) # {'pos': [5, 9, 12, 14, 16, 20, 23], 'peaks': [15, 17, 18, 19, 18, 13, 18]})
