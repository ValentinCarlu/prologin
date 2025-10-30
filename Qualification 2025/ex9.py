def meilleure_muraille(n: int, sortie: list, entree: list) -> None:
    t = []
    for i in range(n) :
        tmp = []
        for j in range(n) :
            if i == j :
                tmp.append(None)
            else :
                tmp.append((sortie[i]-entree[j])**2)
        t.append(tmp)
    tab_base = []
    for i in range(n) :
        tab_base.append(i)
    tab_base.append(0)
    t_final = []
    for _ in range(n) :
        for i in range(1,n-1) :
            tmp = tab_base[i]
            tab_base[i] = tab_base[i+1]
            tab_base[i+1] = tmp
            print(tab_base)
            t_final.append(tab_base.copy())
    print(t_final)
    print(len(t_final))

if __name__ == "__main__":
    n = int(input())
    sortie = list(map(int, input().split()))
    entree = list(map(int, input().split()))
    meilleure_muraille(n, sortie, entree)