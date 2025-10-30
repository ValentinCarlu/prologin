from time import *
from random import randint

n = 100000
villes = [randint(1,20) for _ in range(n)]

r = 10000000
k = 100


start = perf_counter()

def batiments(n: int, r: int, k: int, villes: list) :
    if k >= n and r >= n: 
        m = max(villes)
        villes = [m for _ in range(n)]
    elif k >= n and r < n :
        m = max(villes)
        villes = [m for _ in range(r)] + villes[r:]
    else :
        for i in range(r) :
            tmp = [villes[j%n] for j in range(i, i+k)]
            villes[i%n] = max(tmp)
    print(' '.join(map(str, villes)))


"""       
if __name__ == "__main__":
    n = int(input())
    r = int(input())
    k = int(input())
    villes = list(map(int, input().split()))
    batiments(n, r, k, villes)"""

batiments(n, r, k, villes)
end = perf_counter()
print(end-start)