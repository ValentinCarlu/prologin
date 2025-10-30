def ordre(k : int, n : int, tailles : list) -> None :
    t = []
    current = 0
    for elt in tailles :
        if elt not in t :
            t.append(elt)
    t = sorted(t)
    for i in range(0, len(t)) :
        en_cours = t.pop(0)
        t_index = []
        for j in range(0, len(tailles)) :
            if tailles[j] == en_cours :
                t_index.append(j)
        tt = []
        for j in range(current, current + len(t_index)) :
            tt.append(j%k)
        for index in t_index :
            if index%k in tt :
                tt.pop(tt.index(index%k))
                current += 1
            else :
                return "NON"
    return "OUI"
            
        
    
if __name__ == "__main__":
    k = int(input())
    n = int(input())
    tailles = list(map(int, input().split()))
    print(ordre(k, n, tailles))
