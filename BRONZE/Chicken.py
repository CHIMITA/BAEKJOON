'''
백준 치킨 쿠폰
https://www.acmicpc.net/problem/1673

'''


for i in range(3):

    coupon_n, stamp_k = map(int, input().split())

    stamp = 0
    result = 0

    result += coupon_n

    while coupon_n//stamp_k:
        result += coupon_n//stamp_k
        #stamp += coupon_n #가지고 있던 치킨쿠폰 다 쓰기
        #coupon_n = 0 
        #coupon_n += stamp/stamp_k #치킨 쿠폰 쓴 후 생긴 치킨쿠폰
        coupon_n = coupon_n//stamp_k + coupon_n%stamp_k
        #stamp %= stamp_k #치킨쿠폰으로 바꾸지 못한 도장

    print(result)