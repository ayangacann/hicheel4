# Өгөгдсөн тоо тэгш бол 3т хувааж үлдэгдлийг гарга, үгүй бол 3т хувааж бүхлийг хэвлэ.

n = int(input())
if (n % 2 == 0):
    print(n % 3)
else:
    print(n // 3)