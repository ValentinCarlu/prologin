#refaire ex6 en prenant en compte la distance de chaque maison avec la maison 1

def distance_1(d : dict, scores : list) :
    list_1 = [scores[0]]
    fait = set()
    a_faire_entier = set([1])
    a_faire = [[0,1]]
    while len(a_faire) > 0 :
        dist,valeur = a_faire.pop(0)
        a_faire_entier.remove(valeur)
        fait.add(valeur)
        for elt in set(d[valeur])-fait-a_faire_entier :
            a_faire.append([dist+1,elt])
            a_faire_entier.add(elt)
            if dist+1 >= len(list_1) :
                list_1.append(scores[elt-1])
            else :
                list_1[dist+1] += scores[elt-1]
    return list_1

def score_total(n: int, m: int, k: int, scores: list, routes: list) -> None:
    d = {}
    for elt in routes :
        if elt[0] in d.keys() :
            d[elt[0]].add(elt[1])
        else :
            d[elt[0]] = {elt[1]}
        if elt[1] in d.keys() :
            d[elt[1]].add(elt[0])
        else :
            d[elt[1]] = {elt[0]}
    dist1 = distance_1(d, scores)
    res = 0
    long = 0
    t_v = []
    for elt in dist1 :
        if len(t_v) == 0 :
            t_v.append(elt)
        else :
            t_v.append(t_v[-1]+elt)
    if k+1 > len(dist1) :
        long = len(dist1)
    else :
        long = k+1
    for i in range(long) :
        if k-i < len(t_v) :
            res += dist1[i]*t_v[k-i]
        else :
            res += dist1[i]*t_v[len(t_v)-1]
        res %= 1000000007
    # print(dist1)
    print(res)

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    k = int(input())
    scores = list(map(int, input().split()))
    routes = [list(map(int, input().split())) for _ in range(m)]
    score_total(n, m, k, scores, routes)