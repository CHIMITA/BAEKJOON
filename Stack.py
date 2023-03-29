import sys
 
num = int(sys.stdin.readline())
stack = []
 
for i in range(num):
    order = sys.stdin.readline().split()
 
    if(order[0] == 'pop') : # POP 연산 (삭제)
        if(len(stack) == 0):
            print(-1)
        else:
            print(stack.pop())
 
    elif(order[0] == 'empty'): # 비어있는지 확인
        if(len(stack) == 0):
            print(1)
        else:
            print(0)
 
    elif(order[0] == 'size'): # 가득 찼는지 확인
        print(len(stack))
 
    elif(order[0] == 'top'): # TOP 위치 가리키기
        if(len(stack) != 0) :
            print(stack[-1]) 
        else:
            print(-1)
    
    elif(order[0] == 'push'): # PUSH 연산 (삽입)
        stack.append(order[1])
        
        