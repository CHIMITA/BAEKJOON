'''
백준 두 수 비교하기
https://www.acmicpc.net/problem/1330
'''

a, b = map(int, input().split())

if a > b: #a가 b보다 클 때
    print('>')
elif a < b: #b가 a보다 클 때
    print('<')
else:#a랑 b가 같을 때
    print('==')
