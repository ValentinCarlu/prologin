def chercher(dist : list,dist_arrive : list, d : dict, k : int, a : int, b : int, passe1 : bool) :
    if a == b and passe1 and k >= 0 :
        return True
    else :
        if k >= 0 :
            if not passe1 :
                if 1 in d[a] :
                    return chercher(dist,dist_arrive,d,k-1,1,b,True)
                else :
                    for elt in dist :
                        if elt in d[a] :
                            return chercher(dist,dist_arrive,d,k-1,elt,b,passe1)
            else :
                if b in d[a] :
                    return chercher(dist,dist_arrive,d,k-1,b,b,passe1)
                else :
                    for elt in dist_arrive :
                        if elt in d[a] :
                            return chercher(dist,dist_arrive,d,k-1,elt,b,passe1)
        else :
            return False

def distance(d : dict, c : int) :
    t = []
    a_faire = [c]
    while len(a_faire) > 0 :
        en_cours = a_faire.pop(0)
        t.append(en_cours)
        for elt in d[en_cours] :
            if elt not in a_faire and elt not in t :
                a_faire.append(elt)
    return t

def score_total(n: int, m: int, k: int, scores: list, routes: list) -> None:
    d = {}
    for elt in routes :
        if elt[0] in d.keys() :
            d[elt[0]].append(elt[1])
        else :
            d[elt[0]] = [elt[1]]
        if elt[1] in d.keys() :
            d[elt[1]].append(elt[0])
        else :
            d[elt[1]] = [elt[0]]
    dist1 = distance(d,1)
    res = 0
    for i in range(1,n+1) :
        for j in range(1,n+1):
            if i == 1 or j == 1 :
                if chercher(dist1, distance(d,j), d, k, i, j, True) :
                    res += scores[i-1]*scores[j-1]
                    print(i,j)
            else :
                if chercher(dist1, distance(d,j), d, k, i, j, False) :
                    res += scores[i-1]*scores[j-1]
                    print(i,j)
            res %= 1000000007
    print(res)


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    k = int(input())
    scores = list(map(int, input().split()))
    routes = [list(map(int, input().split())) for _ in range(m)]
    score_total(n, m, k, scores, routes)