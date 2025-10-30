def situation_finale(n: int, m: int, villes: list, actions: list) -> None:
    t = villes.copy()
    rota = "d"
    t = ["tete"] + t
    manger = []
    for a in actions : 
        index_tete = t.index("tete")
        if rota == "d" :
            if a == "A" :
                if index_tete != len(t) - 1 :
                    t[index_tete], t[index_tete + 1] = t[index_tete + 1], t[index_tete]
                else :
                    t = [t[0]] + ["tete"] + t[1:len(t)-1]
            elif a == "M" :
                if index_tete != len(t) - 1 :
                    manger.append(t.pop(index_tete + 1))
                else :
                    manger.append(t.pop(0))
            elif a == "R" :
                rota = "g"
            else :
                t = t[0 : index_tete + 1] + [manger.pop(-1)] + t[index_tete + 1 : len(t)]
        else :
            if a == "A" :
                if index_tete != 0 :
                    t[index_tete], t[index_tete - 1] = t[index_tete - 1], t[index_tete]
                else :
                    t = t[1:len(t)-1] + ["tete"] + [t[len(t)-1]]
            elif a == "M" :
                if index_tete != 0 :
                    manger.append(t.pop(index_tete - 1))
                else :
                    manger.append(t.pop(-1))
            elif a == "R" :
                rota = "d"
            else :
                t = t[0 : index_tete] + [manger.pop(-1)] + t[index_tete : len(t)]
    
    if rota == "g" :
        t = t[::-1]
    index_tete = t.index("tete")
    t = t[index_tete + 1 : len(t)] + t[0 : index_tete]
    for elt in t :
        print(elt)


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    villes = [input() for _ in range(n)]
    actions = list(input())
    situation_finale(n, m, villes, actions)