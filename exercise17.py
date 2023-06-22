# https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python
# Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p, we want to find a positive integer k, if it exists, such that the sum of the digits of n taken to the successive powers of p is equal to k * n.
# If it is the case we will return k, if not return -1.


def dig_pow(n, p):
    sum = 0
    
    for x in range(len(str(n))):
        sum += int(str(n)[x])**p
        p += 1
        
    if (sum/n)%1 == 0:
        return sum/n
    else:
        return -1

#Pruebas en consola / test cases

print (dig_pow(89, 1)) # should return 1 since 8¹ + 9² = 89 = 89 * 1
print (dig_pow(92, 1)) # should return -1 since there is no k such as 9¹ + 2² equals 92 * k
print (dig_pow(695, 2)) # should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
print (dig_pow(46288, 3)) # should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

    
