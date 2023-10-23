# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Round 2 - Problem D. Tower Rush
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-2/problems/D
#
# Time:  O(NlogN)
# Space: O(N)
#

from collections import Counter

def linear_sieve_of_eratosthenes(n):  # Time: O(n), Space: O(n)
    primes = []
    spf = [-1]*(n+1)  # the smallest prime factor
    for i in range(2, n+1):
        if spf[i] == -1:
            spf[i] = i
            primes.append(i)
        for p in primes:
            if i*p > n or p > spf[i]:
                break
            spf[i*p] = p
    return spf  # modified

# https://www.geeksforgeeks.org/program-for-mobius-function-set-2/
def mobius(spf):  # Time: O(n), Space: O(n)
    mu = [0]*len(spf)
    for i in range(1, len(mu)):
        mu[i] = 1 if i == 1 else 0 if spf[i//spf[i]] == spf[i] else -mu[i//spf[i]]
    return mu

def lazy_init(n):
    while len(INV) <= n:  # lazy initialization
        FACT.append(FACT[-1]*len(INV) % MOD)
        INV.append(INV[MOD%len(INV)]*(MOD-MOD//len(INV)) % MOD)  # https://cp-algorithms.com/algebra/module-inverse.html
        INV_FACT.append(INV_FACT[-1]*INV[-1] % MOD)

def factorial(n):
    lazy_init(n)
    return FACT[n]

def inv_factorial(n):
    lazy_init(n)
    return INV_FACT[n]

def nCr(n, k):
    if n < k:
        return 0
    return factorial(n)*inv_factorial(k)*inv_factorial(n-k) % MOD

def tower_rush():
    N, K, D = list(map(int, input().split()))
    H = list(map(int, input().split()))
    cnt = Counter()
    for x in H:
        for d in DIVISORS[x]:
            cnt[d] += 1
    max_d = max(cnt.keys())
    result = 0
    for d in DIVISORS[D]:
        for i in range(max_d//d+1):
            if d*i not in cnt:
                continue
            result = (result+nCr(cnt[d*i], K)*MU[i])%MOD
    return result*factorial(K)%MOD

MOD = 10**9+7
MAX_N = 10**6
FACT, INV, INV_FACT = [[1]*2 for _ in range(3)]
MU = mobius(linear_sieve_of_eratosthenes(MAX_N))
DIVISORS = [[] for _ in range(MAX_N+1)]
for i in range(1, MAX_N+1):
    for j in range(i, MAX_N+1, i):
        DIVISORS[j].append(i)
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, tower_rush()))
