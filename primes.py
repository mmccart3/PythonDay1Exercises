list_of_primes=[2]

for x in range(2,10000):
    prime = True
    for y in list_of_primes:
        if (x % y) == 0:
            prime = False
    if prime:
        list_of_primes.append(x)

print (list_of_primes)
print (len(list_of_primes))