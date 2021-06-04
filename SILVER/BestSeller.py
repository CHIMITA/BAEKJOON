'''
백준 베스트셀러
https://www.acmicpc.net/problem/1302
'''

n = int(input()) #판매 개수

books = {} 

for _ in range(n): #판매한 개수만큼 반복
    book = input() #책 이름 입력
    if book not in books: #books에 없는 책일 때
        books[book] = 1 #books에 book을 넣어주고, 1 추가 ex) {'top' : 1} -> {'top' : 1, 'you' : 1}
    else: #books에 있는 책일 때
        books[book] += 1 #books에 book을 넣어주고, 1씩 증가 
                         #ex) {'top' : 1} -> {'top' : 2}

target = max(books.values()) # vlaues에서 최대값 얻어 target에 저장        
arr = [] 
 
for book, number in books.items(): # book, number가 books key, value 값에 있을 때 반복 
                                   # items : key, value 값을 출력해주는 함수
    if number == target: 
        arr.append(book) #arr이에 book추가
        
print(sorted(arr)[0])