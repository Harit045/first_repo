start = 2
end = 50
primes = list()
for num in range(start, end):
    prime = True
    for j in range(2,num):
        if (num%j == 0):
            prime = False
    if (prime):
        primes.append(num)

print(primes)    





