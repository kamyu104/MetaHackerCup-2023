# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Round 1 - Problem B1. Sum 41 (Chapter 1)
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/problems/B1
#
# Time:  precompute: O(sqrt(MAX_P))
#        runtime: O(logP + pi(sqrt(P))) = O(logP + sqrt(P)/log(sqrt(P)))
# Space: O(K), K = 41
#

def linear_sieve_of_eratosthenes(n):
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
    return primes  # len(primes) = O(n/(logn-1)), reference: https://math.stackexchange.com/questions/264544/how-to-find-number-of-prime-numbers-up-to-to-n

def sum_41_chapter_1():
    P = int(input())
    result = []
    total = 0
    p = 2
    for p in PRIMES:
        if p*p > P:
            break
        while P%p == 0:
            P //= p
            result.append(p)
            total += result[-1]
            if total > TARGET:
                return -1
        p += 1
    if P != 1:
        result.append(P)
        total += result[-1]
        if total > TARGET:
            return -1
    result.extend((1 for _ in range(TARGET-sum(result))))
    return f'{len(result)} {" ".join(map(str, result))}'

TARGET = 41
MAX_P = 10**9
PRIMES = linear_sieve_of_eratosthenes(int(MAX_P**0.5))
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, sum_41_chapter_1()))
