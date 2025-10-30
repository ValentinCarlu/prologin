if __name__ == "__main__":
    n = int(input())
    differences = list(map(int, input().split()))

def le_plus_grand_saut(n : int, differences : list) -> None:
    if min(differences) >= 0 :
        return max(differences)
    else :
        hauteurs = []
        hoder = 1
        for nb in differences :
            hauteurs.append(hoder+nb)
            hoder += nb
        return max(differences[0:hauteurs.index(max(hauteurs))+1])
    
print(le_plus_grand_saut(n, differences))
