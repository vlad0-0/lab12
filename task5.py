def Fact2(n):
    a = 1
    b = 1
    for i in range(2, n+1):
        if i%2 == 0:
            a = a*i
        else:
            b = b*i
    return(a, b)
n = int(input())
while n < 1:
    n = int(input())
print(Fact2(n))
