
from typing import List


def verifier_classes(
    n: int, t: int, bornes: List[int], avant: List[int], apres: List[int]
) -> None:
    """
    :param n: le nombre de classes d'âge
    :param t: écart de temps entre les deux recensements
    :param bornes: la liste des bornes des classes d'âge
    :param avant: la liste du nombre de robots par classe d'âge lors du premier recensement
    :param apres: la liste du nombre de robots par classe d'âge lors du second recensement
    """
    index_avant = 0
    for i in range(n) :
        # print(i)
        borne = bornes[i]
        while apres[i] != 0 and index_avant < n:
            ok = True

            if index_avant != n-1 :
                if i != n-1 :
                    if bornes[index_avant+1] <= borne - t :
                        index_avant += 1
                        ok = False
                    elif bornes[index_avant] >= bornes[i+1] - t :
                        break
                else :
                    if bornes[index_avant+1] <= borne - t :
                        index_avant += 1
                        ok = False
            else :
                if i != n-1 :
                    break
                else :
                    if bornes[index_avant] < borne - t :
                        break
            
            # print("index avant : " + str(index_avant) + " i : " + str(i))
            # if index_avant != n-1 and bornes[index_avant+1] < borne - t :
            #     index_avant += 1
            #     ok = False
            #     # print("a1")
            # elif index_avant == n-1 and i != n-1 :
            #     # print("a2")
            #     break
            # elif i != n-1 and bornes[index_avant] >= bornes[i+1] - t :
            #     # print("b1")
            #     break
            # elif i == n-1 :
            #     if bornes[index_avant] < bornes[i] - t :
            #         # print("b2")
            #         index_avant += 1
            #         ok = False
                
            
            if ok :
                if avant[index_avant] < apres[i] : 
                    apres[i] -= avant[index_avant]
                    avant[index_avant] = 0
                    index_avant += 1
                    # print("c1")
                else :
                    avant[index_avant] -= apres[i]
                    apres[i] = 0
                    # print("c2")
            # print(avant, apres)
    print(sum(apres))
    print(sum(avant))


    


if __name__ == "__main__":
    n = int(input())
    t = int(input())
    bornes = list(map(int, input().split()))
    avant = list(map(int, input().split()))
    apres = list(map(int, input().split()))
    verifier_classes(n, t, bornes, avant, apres)
