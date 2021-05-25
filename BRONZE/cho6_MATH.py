def gcd(a,b):
 return gcd(b%a, a) if b%a else a


T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    if A > B: A, B = B, A
    G = gcd(A, B)
    l = A * B // G

    print(l, G)

