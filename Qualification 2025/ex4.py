def le_juste_etal(n: int, valeur: int, boites: list) -> None:
    res = 0
    b = 0
    for i in range(len(boites)) :
        tmp = 0
        for j in range(i,len(boites)) :
            b += 1
            tmp += boites[j]
            if tmp % valeur == 0 :
                res += 1
        res %= 1000000007
    print(b)

def le_juste_etal2(n: int, valeur: int, boites: list) -> None:
    res = 0
    prefix_sums = {0: 1}  # initialiser avec une somme préfixe de 0
    
    current_sum = 0
    
    for i in range(n):
        current_sum += boites[i]
        mod_value = current_sum % valeur
        print(boites[i])
        if mod_value in prefix_sums:
            res += prefix_sums[mod_value]
            res %= 1000000007
        else:
            prefix_sums[mod_value] = 0
        print("----")
        print(res)
        print()
        prefix_sums[mod_value] += 1
    
    print(res)

if __name__ == "__main__":
    n = int(input())
    valeur = int(input())
    boites = list(map(int, input().split()))
    le_juste_etal2(n, valeur, boites)
