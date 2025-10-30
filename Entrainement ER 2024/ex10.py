from typing import List

    
def routes_maximum(deb,fin,d: int, n: int, villes: List[int], cache : dict) -> None:
    """
    :param d: le nombre de dieux
    :param n: le nombre de villes
    :param villes: pour chaque ville, le dieu qui la contrôle
    """
    # TODO Affichez, sur une ligne, le plus grand nombre de routes que vous
    # pouvez construire sans provoquer le moindre conflit.
    if len(villes) == 0 :
        return 0
    else :
        d = {}
        for i in range(deb,fin+1) :
            elt = villes[i]
            if elt in d.keys() :
                d[elt].append(i)
            else :
                d[elt] = [i]
        t = []
        for elt in d.values() :
            for i in range(len(elt)) :
                for j in range(i, len(elt)) :
                    if (i,j) in d.keys() :
                        t.append(d[(i,j)])
                    else :
                        temp = villes.copy()
                        for k in range(i) :
                            temp[k] = None
                        for k in range(j+1,len(temp)) :
                            temp[k] = None
                        t.append(routes_maximum(i,j,d,n,temp,cache))
                        cache[(i,j)] = t[-1]
        return max(t)


if __name__ == "__main__":
    d = int(input())
    n = int(input())
    villes = list(map(int, input().split()))
    print(routes_maximum(0,len(villes)-1,d, n, villes, {}))
