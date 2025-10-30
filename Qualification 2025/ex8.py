def desequilibre_minimal(n: int, k: int, barres: list) -> None:
    ba = sorted(barres)
    d = {}
    t = []
    for i in range(n-1) :
        v = ba[i+1]-ba[i] 
        if v in d.keys() :
            d[v].append(i)
        else :
            d[v] = [i]
        t.append([v,[ba[i],ba[i+1]]])
    res = 0
    for i in range(k) :
        m = min(d.keys())
        res += m
        print(ba)
        print(d)
        print(t)
        print(m)
        v_milieu = d[m].pop(-1)
        if len(d[m]) == 0 :
            del d[m] 
        a = False
        b = False
        for i in range(v_milieu-1,-1,-1) :
            if t[i] != None :
                tab_avant = t[i]
                t[i] = None
                v = tab_avant[0]
                d[v].pop(d[v].index(i))
                a = True
                if len(d[v]) == 0 :
                    del d[v]
                break
        for i in range(v_milieu+1,n-1) :
            if t[i] != None :
                tab_apres = t[i]
                t[i] = None
                v = tab_apres[0]
                d[v].pop(d[v].index(i))
                b = True
                if len(d[v]) == 0 :
                    del d[v]
                break
        if a and b :
            v = tab_apres[1][1] - tab_avant[1][0]
            if v in d.keys() :
                d[v].append(v_milieu) 
            else :
                d[v] = [v_milieu]
            t[v_milieu] = [v,[tab_avant[1][0],tab_apres[1][1]]]
    print(res)
        
if __name__ == "__main__":
    n = int(input())
    k = int(input())
    barres = list(map(int, input().split()))
    desequilibre_minimal(n, k, barres)
