from math import inf
def desequilibre_minimal(n: int, k: int, barres: list) -> None:
    # Trier les barres pour faciliter la sélection
    barres = sorted(barres)
    # Initialiser une table DP
    # dp[i][j] : déséquilibre minimal pour construire j étages avec les i premières barres
    dp = []
    for _ in range(n+1) :
        dp.append([inf]*(k+1))
    dp[0][0] = 0  
    for i in range(2, n + 1):  # On a besoin d'au moins 2 barres pour un étage
        for j in range(1, k + 1):  # Pas plus d'étages que possible avec i barres
            # Soit on inclut les barres i-1 et i-2 pour cet étage
            dp[i][j] = min(dp[i][j], dp[i - 2][j - 1] + abs(barres[i - 1] - barres[i - 2]))
            # Soit on ne les inclut pas, et on garde le meilleur précédent
            dp[i][j] = min(dp[i][j], dp[i - 1][j])

    # Le résultat est dans dp[N][dp[N][K]
    for elt in dp :
        print(elt)
    print(dp[n][k])

if __name__ == "__main__":
    n = int(input())
    k = int(input())
    barres = list(map(int, input().split()))
    desequilibre_minimal(n, k, barres)
