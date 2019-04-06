import math
import string

T = int(input())
for t in range(T):
    _ = input()
    s = [int(x) for x in input().split()]
    j = 1
    pending = []
    while s[0] == s[j]:
        j += 1
    f = math.gcd(s[0], s[j])
    primes = [f]
    if not j % 2:
        primes.append(s[0] // f)
    else:
        primes = [s[0] // f] + primes
    f = primes[1]
    for i in range(1, len(s)):
        f = s[i] // f
        primes.append(f)
    tab = dict(zip(sorted(set(primes)), string.ascii_uppercase))
    decoded = [tab[x] for x in primes]
    print("Case #{}: {}".format(t+1, "".join(decoded)))