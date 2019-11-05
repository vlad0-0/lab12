def RingS(r1, r2):
    if r1 < r2:
    return(3.14*(r1+r2)*abs(r1-r2))
for i in range(3):
    r1 = float(input())
    r2 = float(input())
    print(RingS(r1, r2))
