
def nombre_redirections(n: int) -> None:
    """
    :param n: l'étage initial de Jøsëf Marchand
    """
    # TODO Affichez, sur une ligne, le nombre de redirections que Jøsëf
    # Marchand va subir avant d'atteindre la chambre 1.
    compteur = 0
    while n != 1 :
        if n % 3 == 0 :
            n /= 3
        elif n % 2 == 0 :
            n /= 2
        else :
            n = 5 * n + 1
        compteur += 1
    print(compteur)


if __name__ == "__main__":
    n = int(input())
    nombre_redirections(n)
