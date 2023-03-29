'''
백준 초6 수학
https://www.acmicpc.net/problem/2702
'''

def gcd(a,b): #최대 공약수 함수
 return gcd(b%a, a) if b%a else a


T = int(input())

for i in range(T):
    A, B = map(int, input().split())
  
    if A > B: A, B = B, A #A가 B보다 클 때 A=B, B=A
    
    G = gcd(A, B)
    l = A * B // G #최대공배수

    print(l, G)

