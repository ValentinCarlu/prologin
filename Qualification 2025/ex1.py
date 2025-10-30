def dechiffrer_message(n : int, message : list) -> str :
    t = []
    for i in range(len(message)) :
        if message[i] in ["0","1","2","3","4","5","6","7","8","9"] :
            t.append([i,message[i]])
    for i in range(len(t)-1,0,-1) :
        if int(t[i][1]) < int(t[i-1][1]) :
            message.pop(t[i][0])
    print(''.join(message))
    
if __name__ == "__main__":
    n = int(input())
    message = list(input())
    dechiffrer_message(n, message)