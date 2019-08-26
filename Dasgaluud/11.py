# 11. Өгөгдсөн 3 тооны бага тоог ол.

n = int(input())
a = n % 10
b = n // 10 % 10
c = n // 100 % 10
if a < b and a < c:
    print(a)
elif b < a and b < c:
    print(b)
elif c < a and c < b:
    print(c)