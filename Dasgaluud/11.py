# 11. Өгөгдсөн 3 тооны бага тоог ол.

n = int(input())
a = n % 10
b = n // 10 % 10
c = n // 100 % 10
if a == b and b == c:
    print("Өгөгдсөн 3 тоо тэнцүү байна.")
elif a < b and a < c:
    print(a)
elif b < a and b < c:
    print(b)
else:
    print(c)