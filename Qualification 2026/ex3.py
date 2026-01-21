def propager(current_set, other_set, joseph, prenom, nom, d, actuel, res, jour):
    new_set = set()
    for elt in current_set:
        joseph.add(elt)
        res[d[elt][1]] = jour

        if elt[0] in prenom:
            for p in prenom[elt[0]]:
                tpl = (elt[0], p)
                if tpl in joseph or tpl in current_set or p == elt[1]:
                    continue
                actuel[tpl] += 1
                if actuel[tpl] >= d[tpl][0]:
                    new_set.add(tpl)

        if elt[1] in nom:
            for no in nom[elt[1]]:
                tpl = (no, elt[1])
                if tpl in joseph or tpl in current_set or no == elt[0]:
                    continue
                actuel[tpl] += 1
                if actuel[tpl] >= d[tpl][0]:
                    new_set.add(tpl)

    return new_set

if __name__ == "__main__":
    n = int(input())
    
    nom = {}
    prenom = {}
    d = {}
    res = [-1 for _ in range(n)]
    i = 0
    
    joseph = set()
    suivant = set()

    actuel = {}

    for _ in range(n) :
        p,no,t,s = input().split(" ")

        if t == "P" :
            if p not in prenom.keys() :
                prenom[p] = set([no])
            else :
                prenom[p].add(no)
        else :
            if no not in nom.keys() :
                nom[no] = set([p])
            else :
                nom[no].add(p)

        d[(p,no)] = {0:int(s), 1:i}
        actuel[(p,no)] = 0
        if int(s) == 0 :
            suivant.add((p,no))

        i += 1

    jour = 0
    modif = True
    b = True
    set2 = set()

    while modif :
        jour += 1
        modif = False

        if b :
            set2 = propager(suivant, set2, joseph, prenom, nom, d, actuel, res, jour)
        else :
            suivant = propager(set2, suivant, joseph, prenom, nom, d, actuel, res, jour)

        modif = bool(set2) if b else bool(suivant)
        b = not b

    for elt in res :
        print(str(elt) + " ", end="")
