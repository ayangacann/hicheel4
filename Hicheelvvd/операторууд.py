# Логик операторууд
# Оператор	Тайлбар	                                                Жишээ
and	        Хэрэв хоёр илэрхийлэл зэрэг биелж байвал үнэн	        x < 5 and x < 10
or	        Хэрэв хоёр илэрхийллийн аль нэг нь биелж байвал үнэн	x < 5 or x < 4
not	        илэрхийллийн үр дүнг худал болгоно	                    not(x < 5 and x < 10)
max         Хамгийн их утгыг олно                                   print(max(num1, num2, ...))

# Арифметик операторууд
# Оператор	Нэр	                Жишээ
+	        Нэмэх	            3+5=8
-	        Хасах	            8-3=5
*	        Үржих	            3*5=15
/	        Хуваах	            34/10=3.4
%	        Үлдэгдэлтэй хуваах	34%10=4
//	        Бүхэл хуваах	    34//10=3
**	        Зэрэгт	            2**5=32

# Утга олгох операторууд
# Оператор	Жишээ	    Тайлбар
=	        x = 5	    x = 5
-=	        x -= 3	    x = x - 3
+=	        x += 3	    x = x + 3
*=	        x *= 3	    x = x * 3
/=	        x /= 3	    x = x / 3
%=	        x %= 3	    x = x % 3
//=	        x //= 3	    x = x // 3
**=	        x **= 3	    x = x ** 3

# Харьцуулах операторууд
# Оператор	Name	            Жишээ
==	        Тэнцүү	            x == y
!=	        Тэнцүү биш	        x != y
>	        Эрс их	            x > y
<	        Эрс бага	        x < y
>=	        Их юмуу Тэнцүү	    x >= y
<=	        Бага юмуу Тэнцүү	x <= y

# Шууд гараас өгсөн тоон утгуудыг "i" гэснээр input дотор оруулна
x1, y1, x2, y2 = [int(i) for i in input()]

# Өгөгдөл дотор байгаа хэсгийг хайж хэвлэх "in" функц
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)

