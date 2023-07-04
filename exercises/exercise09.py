#https://www.codewars.com/kata/60d2325592157c0019ee78ed/train/python"
""" Let's define two functions:

S(N) — sum of all positive numbers not more than N
S(N) = 1 + 2 + 3 + ... + N

Z(N) — sum of all S(i), where 1 <= i <= N
Z(N) = S(1) + S(2) + S(3) + ... + S(N) 

You will be given an integer N as input; your task is to return the value of S(Z(N)). For example, let N = 3:

Z(3) = 1 + 3 + 6 = 10
S(Z(3)) = S(10) = 55

The input range is 1 <= N <= 10^9 and there are 80 ( 40 in LC ) test cases, of which most are random.
"""

def sum_of_sums(n):
    suma = 0
    suma1 = 0
    array =[]
    
    for i in range (1,n+1):
        suma+= i
        array.append(suma)
        
    for j in array:
        if j == array[-1]:
            continue
        else:
            suma += j

    for k in range (1,suma+1):
        suma1+=k
    
    return suma1
        
print(sum_of_sums(3))
print(sum_of_sums(5))
print(sum_of_sums(100))
