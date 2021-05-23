'''
백준 - 피시방 알바
https://www.acmicpc.net/problem/1453

'''

N = int(input()) #손님 수 

pc_sit = list(map(int, input().split())) #앉고싶은 자리 입력
pc_seat = [0] * 101 #pc방 좌석 
pc_rejected = 0 #거절 당한 사람

for i in pc_sit:
    if pc_seat[i] != 0:
        pc_rejected += 1
    else:
        pc_seat[i] += 1

print(pc_rejected)