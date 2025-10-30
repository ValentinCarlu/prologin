from typing import List

def bon_etage(n: int, redirection: List[int]) -> None:
    """
    :param n: le nombre d'étages
    :param redirection: le tableau indiquant vers quels étages Jøsëf Marchand se fait rediriger.
    """
    # TODO En partant de l'étage 0 et en suivant les redirections, affichez sur
    # une ligne l'étage du bureau des voyages humains.
    i = 0
    while i != redirection[i] :
        i = redirection[i]
    print(i)
    


if __name__ == "__main__":
    n = int(input())
    redirection = list(map(int, input().split()))
    bon_etage(n, redirection)
