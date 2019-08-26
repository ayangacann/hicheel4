# 11. Өгөгдсөн 3 тооны бага тоог ол.

n = int(input())
a = n % 10
b = n // 10 % 10
c = n // 100 % 10
if a > b or a > c or b > c:
    print(c)
elif b > a or c > a or b > a:
    print(a)
else: 
    print(b)