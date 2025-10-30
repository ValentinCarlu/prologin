def corrections_minimales(n: int, a: list, b: list) -> None:
    d = {}
    for elt_a in a :
        for elt_b in b :
            tmp = elt_a + elt_b
            if tmp in d :
                d[tmp] += 1
            else :
                d[tmp] = 1
    # moyenne = sum(d.values())/(len(d))
    # d2 = {}
    # for elt in d.values() :
    #     if elt in d2 :
    #         d2[elt] += 1
    #     else :
    #         d2[elt] = 1
    # moyenne = sum([i*j for i,j in d2.items()])/sum(d2.values())
    # maxi = max(d2.values())
    # t = [elt for elt in d2.keys() if d2[elt] == maxi]
    # v = t[0]
    # for elt in t :
    #     print(elt , elt-moyenne)
    #     if abs(elt-moyenne) < abs(v-moyenne) :
    #         v = elt
    v = sorted(d.values())[len(sorted(d.values()))*3//4-1]
    res = 0
    for elt in d.values() :
        if elt > v :
            res += elt - v
        else :
            if v - elt < elt :
                res += v-elt
            else :
                res += elt
    # print(sorted(d.values()))
    # print(sorted(d.values())[len(sorted(d.values()))*3//4-1])
    # print(moyenne)
    # print(v)
    print(res)

if __name__ == "__main__":
    n = int(input())
    a = [input() for _ in range(n)]
    b = [input() for _ in range(n)]
    corrections_minimales(n, a, b)