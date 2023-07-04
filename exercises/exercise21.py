# https://www.codewars.com/kata/56a5d994ac971f1ac500003e
# You are given an array(list) strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.
# n being the length of the string array, if n = 0 or k > n or k <= 0 return "" (return Nothing in Elm, "nothing" in Erlang).
# Note: consecutive strings : follow one after another without an interruption


def longest_consec(strarr, k):
    new_arr = []
    ind_arr = []
    
    if k <= 0 or k > len(strarr):
        return ''
    else:
        for i in range (len(strarr)-k+1):
            joined = ''
            for j in range (i,i+k):
                joined += strarr[j]
            new_arr.append(joined)
            ind_arr.append(len(joined))
    return new_arr[ind_arr.index(max(ind_arr))]  

#Pruebas en consola / Test cases
print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"],2))