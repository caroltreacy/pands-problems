# Carol Treacy
# check if a number is prime 
# The primes are2, 3, 5, 7, 11, 13, ...


p = 221
m = 2
isprime = True

while m < p:
    if p % m == 0:
        # print(m, "divides", p,  "and therefore", p, "is not prime.")
        isprime = False 
    m = m - 1

if isprime:
    print(p, "is a prime number.")    
else:
    print("is not a prime.")



