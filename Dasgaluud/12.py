# 12. Өгөгдсөн 4 тооны их тоог ол.

n = int(input())
numb1 = n % 10
numb2 = n // 10 % 10
numb3 = n // 100 % 10
numb4 = n // 1000 % 10 
if numb1 > numb2 or numb2 > numb3 and numb3 > numb4: 
    print(numb1)
elif numb2 > numb1 and numb1 > numb3 and numb3 > numb4:
    print(numb2)
elif numb3 > numb1 and numb1 > numb2 and numb2 > numb4:
    print(numb3)
elif numb4 > numb1 and numb1 > numb2 and numb2 > numb3:
    print(numb4)