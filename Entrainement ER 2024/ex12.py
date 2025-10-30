from typing import List

def compte_chemins(
    nombre_sommets: int,
    hauteurs: List[int],
    nombre_aretes: int,
    aretes: List[tuple],
    pied: int,
    sommet: int,
) -> None:
    """
    :param nombre_sommets: le nombre de sommets du graphe
    :param hauteurs: la hauteur de tous les sommets du graphe
    :param nombre_aretes: le nombre d'arêtes du graphe
    :param aretes: les arêtes du graphe
    :param pied: le pied de la montagne
    :param sommet: le sommet de la montagne
    """
    # TODO Afficher le nombre de chemins de hauteur strictement croissante,
    # allant du pied au sommet de la montagne
    d = {}
    for elt in aretes :
        print(elt[0])
        if hauteurs[elt[0]-1] in d.keys() :
            d[hauteurs[elt[0]-1]].append(hauteurs[elt[1]-1])
        else :
            d[hauteurs[elt[0]-1]] = [hauteurs[elt[1]-1]]
        if hauteurs[elt[1]-1] in d.keys() :
            d[hauteurs[elt[1]-1]].append(hauteurs[elt[0]-1])
        else :
            d[hauteurs[elt[1]-1]] = [hauteurs[elt[0]-1]]
    pied = hauteurs[pied-1]
    sommet = hauteurs[sommet-1]
    deja_explo = []
    a_faire = [sommet]
    chemin = {sommet : 0}
    while len(deja_explo) > 0 :
        en_cours = a_faire.pop(0)
        deja_explo.append(en_cours)
        for elt in d[en_cours] :
            if elt not in deja_explo :
                a_faire.append(elt)
        

    


if __name__ == "__main__":
    nombre_sommets = int(input())
    hauteurs = list(map(int, input().split()))
    nombre_aretes = int(input())
    aretes = [tuple(map(int, input().split())) for _ in range(nombre_aretes)]
    pied = int(input())
    sommet = int(input())
    compte_chemins(nombre_sommets, hauteurs, nombre_aretes, aretes, pied, sommet)