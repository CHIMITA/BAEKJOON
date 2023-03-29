'''
백준 FBI
https://www.acmicpc.net/problem/2857
'''
li = []
for i in range(1,6):
    FBI_name = input()

    if 'FBI' in FBI_name: #FBI_name에 FBI가 있다면 
        li.append(i) #li에 i를 마지막에 추가 

if li:
    print(*li)
else:
    print("HE GOT AWAY!")
