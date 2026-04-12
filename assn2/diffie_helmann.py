import random


def miller_rabin(n, k=40):
    if (n == 2 or n == 3):
        return True
    if (n%2 == 0) or n <= 1:
        return False
        
    s, d = 0, n-1
    while d % 2 == 0:
        s += 1
        d = d//2 

    for _ in range(k):
        a = random.randrange(2, n-1)    # n is always probable base 1 and n-1 
                                        # since they are always 1 mod (n)
        x = pow(a,d,n)

        # 2^s is not included hence loop s-1 times
        if x == 1 or x == n-1:
            continue
        
        for _ in range(s-1):
            x = pow(x,2,n)

            if x == n-1:
                break
        else:
            # inner loop didn't break
            return False
    
    return True


def gen_sophie(bits=512):
    while True:
        pd = random.getrandbits(bits - 1) | 1 << (bits - 2) | 1

        if miller_rabin(pd):
            p = 2 * pd + 1 

            if miller_rabin(pd):
                return p, pd
            

def find_generator(p, pd):
    while True:
        g = random.randrange(2, p-1)

        if pow(g, pd, p) != 1 and pow(g, 2, p) != 1:
            return g

p, pd = gen_sophie(512)
print(f"Sophie Prime: {p}")
print(f"Prime p': {pd}")

g = find_generator(p, pd)
print(f"Generator: {g}")

# generate secret primes
a = random.randrange(2, p-1)
b = random.randrange(2, p-1)

print(f"Party A secret prime: {a}")
print(f"Party B secret prime: {b}")

# calculate the public exponents
A = pow(g, a, p)
B = pow(g, b, p)

print(f"Party A public key: {A}")
print(f"Party A public key: {B}")

secret_A = pow(B,a,p)
secret_B = pow(A,b,p)

print(f"Shared secret key A: {secret_A}")
print(f"Shared secret key B: {secret_B}")

if secret_A == secret_B:
    print("Same key!")


