def force_maximale(n: int, pont: list) -> None:
    t = []
    actuel = pont[0]
    compteur = 1
    if actuel == 0 :
        nb_zero = 1
        start_un = False
    else :
        nb_zero = 0
        start_un = True
    for c in pont[1:] :
        if c == actuel :
            compteur += 1
        else :
            t.append([actuel, compteur])
            compteur = 1
            actuel = c
            if actuel == 0 :
                nb_zero += 1
    t.append([actuel,compteur])

    t_1 = []
    t_0 = []
    for i in range(2**nb_zero-1) :
        tmp = t.copy()
        s = str(bin(i))[2:]
        if len(s) < nb_zero :
            s = "0"*(nb_zero-len(s)) + s
        # print(s, nb_zero)
        for j in range(len(s)) :
            if s[j] == '1' :
                index = j*2+int(start_un)
                tmp[index] = [1,tmp[index][1]]
        # print(tmp)
        actuel = tmp[0][0]
        compteur = tmp[0][1]
        tmp_0 = []
        tmp_1 = [0]
        for elt in tmp[1:] :
            if elt[0] == actuel :
                compteur += elt[1]
            else :
                if actuel == 1 :
                    tmp_1.append(compteur)
                    actuel = 0
                    compteur = elt[1]
                else :
                    tmp_0.append(compteur)
                    actuel = 1
                    compteur = elt[1]
        if actuel == 1 :
            tmp_1.append(compteur)
        else :
            tmp_0.append(compteur)

        # print(tmp_0,tmp_1)
        t_1.append(max(tmp_1))
        t_0.append(min(tmp_0))

    t_f = []
    for i in range(len(t_0)) :
        t_f.append(t_0[i]-t_1[i])
    # print(t_f)
    print(max(t_f))

if __name__ == "__main__":
    n = int(input())
    pont = list(map(int, input().split()))
    force_maximale(n, pont)