def force_maximale(longueur: int, tunnel: list) -> None:
    t = [[],[0]]
    actuel = tunnel[0]
    compteur = 1
    for c in tunnel[1:] :
        if c == actuel :
            compteur += 1
        else :
            t[actuel].append(compteur)
            compteur = 1
            actuel = c
    t[actuel].append(compteur)
    # print(t)
    print(min(t[0]) - max(t[1]))



if __name__ == "__main__":
    longueur = int(input())
    tunnel = list(map(int, input().split()))
    force_maximale(longueur, tunnel)
