# 12. Өгөгдсөн 4 тооны их тоог ол.

n = int(input())
numb1 = n % 10
numb2 = n // 10 % 10
numb3 = n // 100 % 10
numb4 = n // 1000 % 10 
print(max(numb1, numb2, numb3, numb4))