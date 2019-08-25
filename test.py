n = int(input())
a = n % 10
b = n // 10 % 10
c = n // 100 % 10
d = n // 1000 % 10
e = n // 10000
print(a + b + c + d + e)