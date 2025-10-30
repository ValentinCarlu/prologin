from typing import List

def ethanol_maximal(nombre_recettes: int, recettes: List[List[int]], quantite_miel: int) -> None:
    """
    :param nombre_recettes: le nombre de recettes
    :param recettes: la liste des recettes
    :param quantite_miel: la quantité de miel dont vous disposez
    """
    # TODO Affichez, sur une ligne, la quantité maximale d'alcool que vous
    # pouvez concocter pour les vikings à l'aide des ingrédients dont vous
    # disposez.
    rapport = {}
    for elt in recettes :
        c = elt[0]/elt[1]
        if c in rapport.keys() :
            rapport[c].append(elt) 
        else :
            rapport[c] = [elt]

    coeff = sorted(rapport)[::-1]

    nb_litre = 0

    for elt in coeff :
        t = rapport[elt] 
        for tablo in t :
            i = 0
            while i < tablo[2] and quantite_miel != 0 :
                if quantite_miel >= tablo[1] :
                    nb_litre += tablo[0]
                    i += 1
                    quantite_miel -= tablo[1]
                else :
                    nb_litre += round((quantite_miel/tablo[1])*tablo[0], 5)
                    return float(nb_litre)
    return float(nb_litre)

if __name__ == "__main__":
    nombre_recettes = int(input())
    recettes = [list(map(int, input().split())) for _ in range(nombre_recettes)]
    quantite_miel = int(input())
    print(ethanol_maximal(nombre_recettes, recettes, quantite_miel))