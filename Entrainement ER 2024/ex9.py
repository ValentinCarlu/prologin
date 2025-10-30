from typing import List

def fatigue_minimale(n: int, loki: List[int], m: int, heimdall: List[int]) -> None:
    """
    :param n: le nombre de troupes de Loki
    :param loki: les positions des troupes de Loki
    :param m: le nombre de troupes de Heimdall
    :param heimdall: les positions des troupes de Heimdall
    """
    # TODO Afficher, sur une ligne, la distance totale que vont parcourir les
    # troupes.
    loki = sorted(loki)
    heimdall = sorted(heimdall)
    compteur = 0
    j = 0
    for i in range(len(loki)) :
        current = loki[i]
        while j < len(heimdall)-1 and abs(current - heimdall[j]) >= abs(current - heimdall[j+1]) :
            j += 1
        compteur += (current - heimdall[j])**2

    #print(compteur)
    j = 0 
    for i in range(len(heimdall)) :
        current = heimdall[i]
        while j < len(loki)-1 and abs(current - loki[j]) >= abs(current - loki[j+1]) :
            j += 1
        #print(compteur, i, j)
        compteur += (current - loki[j])**2

    print(compteur)

if __name__ == "__main__":
    n = int(input())
    loki = list(map(int, input().split()))
    m = int(input())
    heimdall = list(map(int, input().split()))
    fatigue_minimale(n, loki, m, heimdall)