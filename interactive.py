import sys
from functools import partial
# sys.setrecursionlimit(250_000) # uncomment for recursion

input = lambda: sys.stdin.readline().rstrip('\r\n')
print = partial(print, flush=True)

def solve():
    from math import gcd, lcm, sqrt, ceil, floor, log, e
    from bisect import bisect_left, bisect_right, insort
    from collections import defaultdict, Counter, deque
    from itertools import permutations, combinations, islice
    from heapq import heappush, heappop, heapify
    from functools import cache, lru_cache

    I = lambda n=None: int(input()) if n is None else list(map(int,input().split()))
    S = lambda n=None: input() if n is None else input().split()

    INF = 10**18
    MOD = 10**9 + 7 #998_244_353
    
    raw_t = input()
    if not raw_t: return
    
    t = int(raw_t)
    for _ in range(t):
        pass#ans

if __name__ == "__main__":
    solve()