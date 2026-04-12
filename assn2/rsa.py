import random

# odd, n > 2 
# n-1 = 2^s d (can always be done)
# gcd(a,n) = 1 (base chosen randomly)

# In our implementation, we are skipping it since the
# chances of finding a which is not co-prime to n are
# very low since it essentially means we have factored
# a very large number by chance


# n strong probable prime to base a if either:
#   - a^d = 1 (mod(n)). If doesn't hold then exponentiate a^d to 2^r power.
#   - a^{2^r d} = -1 (mod(n)), 0 <= r < s

# k = number of rounds of testing

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

# to generate primes, keep generating random bits 
# with msb and lsb as 1 and keep checking if prime
def gen_prime(size):
    while True:
        p = random.getrandbits(size) | 1 << (size-1) | 1

        if miller_rabin(p):
            return p

def eea(a,b):
    old_r, r = a, b     
    old_s, s = 1,0      
    old_t, t = 0, 1     

    while r != 0:
        q = old_r//r
        old_r, r =r, old_r - q*r
        old_s, s =s, old_s - q*s
        old_t, t =t, old_t - q*t
    
    # old_r = gcd(a,b), old_s*a + old_t*b = gcd(a,b)
    return old_r, old_s, old_t

def gen_keys(bits=512):
    p = gen_prime(bits)
    q = gen_prime(bits)

    n = p*q
    phi_n = (p-1)*(q-1)

    # chosing 10000000000000001 = 65537 so that m^e is fast
    e = 65537

    gcd, x,y = eea(e,phi_n)
    if gcd != 1:
        print("Highly unlikely event occurred! Can't move on.")
        return

    d = x%phi_n

    return (e,n), (d,n)

pub_key, priv_key = gen_keys()
e,n = pub_key
d,_ = priv_key

print(f"Public Exponent (e): {e}")
print(f"Private Exponent (d): {d}")
print(f"Modulus (n): {n}")

m = random.randrange(2, n - 1)

print(f"Random Message (m): {m}")

# ciphertext c = m ^ e mod(n)
c = pow(m,e,n)
print(f"Ciphertext (c): {c}")

decrypted = pow(c,d,n)
print(f"Decrypted Message (m): {decrypted}")

if m == decrypted:
    print("Success!")
else:
    print("We failed, even with the odds overwhelmingly on our side.")




