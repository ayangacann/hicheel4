# 14. Шатрын хөлөг дээр байрлах 2 тэргийн коардинат x1, y1, x2, y2 хэлбэртэй өгөгдсөн бол 
# биесээ идэх бол true үгүй бол false гэж хэвлэ.

x1 = input("Эхний тэрэгний х координатыг оруул: ")
y1 = input("Эхний тэрэгний y координатыг оруул: ")
x2 = input("2 дахь тэрэгний х координатыг оруул: ")
y2 = input("2 дахь тэрэгний y координатыг оруул: ")

if x1 == y1 and x2 == y2 and x1 == x2 and y1 == y2:
    print("2 тэрэг нэг нүдэнд байж болохгүй!")
elif x1 == x2 or y1==y2:
    print("true")
else:
    print("false")