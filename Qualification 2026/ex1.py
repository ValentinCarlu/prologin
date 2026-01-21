
def mouvement_minimum(n: int, a: int, b: int) -> None:
    a -= 1
    b -= 1
    xa, ya = a//n, a%n
    xb, yb = b//n, b%n
    # print(xa, ya)
    # print(xb,yb)
    print(abs(xa-xb)+abs(ya-yb))


if __name__ == "__main__":
    n = int(input())
    a = int(input())
    b = int(input())
    mouvement_minimum(n, a, b)
