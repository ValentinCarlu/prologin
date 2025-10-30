from typing import List

def test(x, y, xfinal, yfinal, grille) :
    if x == xfinal and y == yfinal :
        return "oui"
    else:
        grille[y][x] = 2
        t = []
        print(grille)
        print(x,y,xfinal,yfinal)
        if x > 0 and grille[x-1][y] == 0:
            t.append(test(x-1, y, xfinal, yfinal, grille))
        if x < len(grille[0]) - 1 and grille[x+1][y] == 0:
            t.append(test(x+1, y, xfinal, yfinal, grille))
        if y > 0 and grille[x][y-1] == 0:
            t.append(test(x, y-1, xfinal, yfinal, grille))
        if y < len(grille) - 1 and grille[x][y+1] == 0:
            t.append(test(x, y+1, xfinal, yfinal, grille))
        if "oui" in t:
            return "oui"
        return "non"
        

def repondre_requetes(
    largeur: int,
    hauteur: int,
    nombre_brisures: int,
    brisures: List[List[int]],
    nombre_requetes: int,
    requetes: List[List[int]],
) -> None:
    """
    :param largeur: la largeur de la grille représentant Midgard
    :param hauteur: la hauteur de la grille représentant Midgard
    :param nombre_brisures: le nombre de brisures
    :param brisures: les positions de chaque brisure
    :param nombre_requetes: le nombre de requêtes
    :param requetes: la liste des requêtes
    """
    # TODO Pour chaque requête, indiquer sur une ligne si `oui` ou `non` le
    # couple peut se rejoindre.
    
    t = [[0 for _ in range(largeur)] for _ in range(hauteur)]
    
    for elt in brisures :
        t[elt[1]-1][elt[0]-1] = 1
    
    print(t)
    for elt in requetes :
        print(test(elt[0]-1, elt[1]-1, elt[2]-1, elt[3]-1, t))
    
    


if __name__ == "__main__":
    largeur = int(input())
    hauteur = int(input())
    nombre_brisures = int(input())
    brisures = [list(map(int, input().split())) for _ in range(nombre_brisures)]
    nombre_requetes = int(input())
    requetes = [list(map(int, input().split())) for _ in range(nombre_requetes)]
    repondre_requetes(largeur, hauteur, nombre_brisures, brisures, nombre_requetes, requetes)
