import math

def answer(n):
    # your code here
    def primes(x):
        if x < 2: return []

        primes = [i for i in range(x)]
        primes[1] = 0

        for prime in primes:
            if prime > math.sqrt(x): break
            if prime == 0: continue
            for non_prime in range(2 * prime, x, prime): primes[non_prime] = 0

        return [prime for prime in primes if prime != 0]

    strings = primes(100000)
    maped_list = map(str, strings)
    string = ''.join(maped_list)


    return string[n:n+5]

def answer(l):
    # your code here
    res = []
    def find_min(e_list):
        if len(e_list) == 1:
            return e_list[0]
        else:
            min_num = min([e[0] for e in e_list])
            orderlist = [e[1:] for e in e_list if e[0] == min_num]
            return [min_num] + find_min(orderlist)
    while len(l) > 0:
        min_ver = find_min(l)
        res.append(min_ver)
        l.remove(min_ver)
    return res
