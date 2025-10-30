def minimum_exclus(n: int, m: int, criteres: list) -> None :
    d = {}
    c = []
    for elt in criteres :
        c.append("".join(str(x) for x in elt))
    for elt in c :
        if elt in d.keys() :
            d[elt] += 1
        else :
            d[elt] = 1
    res = 0
    for elt in d.values() :
        res += elt%2
    print(res)



if __name__ == "__main__":
    n = int(input())
    m = int(input())
    criteres = [list(map(int, input().split())) for _ in range(n)]
    minimum_exclus(n, m, criteres)
