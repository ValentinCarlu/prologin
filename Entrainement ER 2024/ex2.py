
from typing import List


def connecter_les_iles(n: int, paysage: List[int]) -> None:
    """
    :param n: la taille du tableau représentant le paysage.
    :param paysage: le tableau décrivant le paysage. Un 1 représente la présence d'une île.
    """
    # TODO Afficher, sur une ligne, le nombre minimum d'îles que l'on doit
    # construire afin que toutes les îles soient connectées.
    start = 0
    while start < len(paysage) and paysage[start] == 0 :
        start += 1
    end = len(paysage) - 1
    while end >= 0 and paysage[end] == 0 :
        end -= 1
    compteur = 0
    for i in range(start, end) :
        if paysage[i] == 0 :
            compteur += 1
    print(compteur)


if __name__ == "__main__":
    n = int(input())
    paysage = list(map(int, input().split()))
    connecter_les_iles(n, paysage)
