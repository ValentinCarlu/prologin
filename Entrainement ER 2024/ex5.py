from typing import List

def porte_de_helheim(n: int, portes: List[int]) -> None:
    """
    :param n: le nombre de portes
    :param portes: les indications sur les portes
    """
    # TODO Afficher le premier indice $0 \le i < N$ tel que **portes[i]** ne
    # correspond pas au nombre d'occurrences de $i$ dans **portes**, ou -1
    # sinon.
    trouve = False
    d = {}
    for i in range(n) :
        d[i] = 0
    for elt in portes :
        d[elt] += 1
    for i in range(n) :
        c = d[i]
        if c != portes[i] :
            print(i)
            trouve = True
            break

    if not trouve :
        print(-1)


if __name__ == "__main__":
    n = int(input())
    portes = list(map(int, input().split()))
    porte_de_helheim(n, portes)
