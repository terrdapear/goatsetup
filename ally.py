import sys
import os
from time import time
#sys.setrecursionlimit(250_000) uncomment for recursion

if os.path.exists("hatdog.txt"):
    sys.stdin= open("hatdog.txt","r")

def solve():
    from math import gcd, lcm, sqrt, ceil, floor, log, e
    from bisect import bisect_left, bisect_right, insort
    from collections import defaultdict, Counter, deque
    from itertools import permutations, combinations
    from heapq import heappush, heappop, heapify
    from functools import cache, lru_cache

    input_dat = sys.stdin.read().split()

    it = iter(input_dat)
    out = []
   
    INF = 10**18
    MOD = 10**9 + 7

    #int(next(it))
    #next(it)
    #out.append(str(inp))
   
    t = int(next(it))
    for _ in range(t):
        pass#ans

    sys.stdout.write("\n".join(out)+"\n")


if __name__ == "__main__":
    start = time()
    solve()
    end = time()
    if os.path.exists("hatdog.txt"):
        print(end-start)