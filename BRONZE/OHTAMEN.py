'''
백준 오타맨
https://www.acmicpc.net/problem/2711
'''
for _ in range(int(input())):
    n, string = input().split()
    n = int(n)
    print(string[:n-1], string[n:], sep='') #sep = 분리하여 출력
