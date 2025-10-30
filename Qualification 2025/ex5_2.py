def corrections_minimales(n: int, a: list, b: list) -> None:
    da = {}
    for elt_a in a :
        if elt_a in da :
            da[elt_a] += 1
        else :
            da[elt_a] = 1
    
    db = {}
    for elt_b in b :
        if elt_b in db :
            db[elt_b] += 1
        else :
            db[elt_b] = 1
    t = []
    for elt in da.values() :
        for elt2 in db.values() :
            t.append(elt*elt2)
    
    t = sorted(t)
    t_f = []
    for v in range(t[0], t[-1]+1) :
        res = 0
        for elt in t :
            if elt >= v :
                res += elt-v 
            else :
                if elt < v-elt :
                    res += elt
                else :
                    res += v-elt
        t_f.append(res)
    print(min(t_f))

if __name__ == "__main__":
    n = int(input())
    a = [input() for _ in range(n)]
    b = [input() for _ in range(n)]
    corrections_minimales(n, a, b)