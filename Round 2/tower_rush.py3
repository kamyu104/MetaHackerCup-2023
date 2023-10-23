# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Round 2 - Problem D. Tower Rush
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-2/problems/D
#
# Time:  precompute: O(MAX_N + max(MAX_D, MAX_H) * log(max(MAX_D, MAX_H)))
#        runtime:    O(N * F + (max_h) * log(max_h)), F = max(len(DIVISORS[x]) for x in H)
# Space: O(MAX_N + max(MAX_D, MAX_H) * log(max(MAX_D, MAX_H)))
#

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

def nCr(n, k):
    if n < k:
        return 0
    return (((FACT[n]*INV_FACT[k])%MOD)*INV_FACT[n-k])%MOD

def tower_rush():
    N, K, D = list(map(int, input().split()))
    H = list(map(int, input().split()))
    cnt = [0]*(max(H)+1)
    for x in H:
        for d in DIVISORS[x]:
            cnt[d] += 1
    result = 0
    for d in DIVISORS[D]:
        for i in range(d, len(cnt), d):
            result = (result+nCr(cnt[i], K)*MU[i//d])%MOD
    result = (result*FACT[K])%MOD
    return result

MOD = 10**9+7
MAX_N = MAX_D = MAX_H = 10**6
MU = mobius(linear_sieve_of_eratosthenes(MAX_H))
FACT, INV, INV_FACT = [[1]*2 for _ in range(3)]
while len(INV) <= MAX_N:
    FACT.append(FACT[-1]*len(INV) % MOD)
    INV.append(INV[MOD%len(INV)]*(MOD-MOD//len(INV)) % MOD)  # https://cp-algorithms.com/algebra/module-inverse.html
    INV_FACT.append(INV_FACT[-1]*INV[-1] % MOD)
DIVISORS = [[] for _ in range(max(MAX_D, MAX_H)+1)]
for i in range(1, len(DIVISORS)):
    for j in range(i, len(DIVISORS), i):
        DIVISORS[j].append(i)
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, tower_rush()))
