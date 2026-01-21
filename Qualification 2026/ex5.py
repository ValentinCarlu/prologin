from typing import List
import sys
sys.setrecursionlimit(200000)

def calcul_possibilites(n: int, a: List[int]) -> None:
    if sum(a) % 3 != 0 :
        print(0)
        return
    d = {}
    for i in range(n) :
        d[i] = {}
    res = f(0, n,a, d)
    print(res)
    
    # for elt in d.values() :
    #     print(len(elt.values()))

def f(current, n,a, d) :
    # print(a)
    res = 0
    boucle = a[current] // 3
    mod = a[current] % 3
      
    if mod > 0 and current < n-2 and (a[current+1] < mod or a[current+2] < mod) :
        return 0
    if current >= n-2 :
        if mod > 0 :
            return 0
        elif current == n-2 and a[current+1] % 3 == 0 :
            return 1
        elif current == n-1 and mod == 0:
            return 1
        else :
            return 0
    a[current+1] -= mod
    a[current+2] -= mod
    for i in range(boucle+1) :
        if current < n-2 and a[current+1] >= i*3 and a[current+2] >= i*3 :
            a[current+1] -= i*3
            a[current+2] -= i*3

            val = a[current+1]*1000+a[current+2]
            if val not in d[current].keys() :
                # print(current, i, a)
                valeur = f(current+1, n, a, d) % 1000000007
                res += valeur 
                d[current][val] = valeur
                # print(current, i, a)
            else :
                res += d[current][val] % 1000000007
                # print("prog")
            a[current+1] += i*3
            a[current+2] += i*3
        else :
            break

    a[current+1] += mod
    a[current+2] += mod

    return res % 1000000007
        




if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    calcul_possibilites(n, a)

