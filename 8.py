#{horizontal} <= {-n,n} >> Горизонтальное смещение ровно на n клеток

x = int(input("x: "))
y = int(input("y: "))
a = int(input("a: "))
b = int(input("b: "))

#Для ладьи (по прямой)
if x == a or y == b: print("1) Ладья сможет сменить позицию данным образом за один ход")
else: print("1) Ладья НЕ сможет сменить позицию данным образом за один ход")



#Для слона (по диагонали)
vertical = x-a
horizontal = y-b


if {vertical} <= {-horizontal,horizontal} or {horizontal} <= {-vertical,vertical}:
    print("2) Слон сможет сменить позицию данным образом за один ход")
else: print("2) Слон НЕ сможет сменить позицию данным образом за один ход")



#Для коня (буквой "Г")
if {horizontal} <= {-2,2} and {vertical} <= {-1,1}: print("3) Конь сможет сменить позицию данным образом за один ход")
elif {horizontal} <= {-1,1} and {vertical} <= {-2,2}: print("3) Конь сможет сменить позицию данным образом за один ход")
else: print("3) Конь НЕ сможет сменить позицию данным образом за один ход")



#Для пешки будем считать только одно направление (Ходит на 1 клетку вперёд, а если стоит на изначальном месте, то ходит на 2, также может сходить на 1 клетку по диагонали при условии, что на той находится вражеская фигура)
if a-x == 1 and y == b: print("4) Пешка сможет сменить позицию данным образом за один ход")
elif a-x == 2 and x == 2 and y == b: print("4) Пешка сможет сменить позицию данным образом за один ход (Т.К. по правилам игры, находясь на второй линии, она может сходить на 2 клетки вперёд)") #Условие можно заменить на x == 2 and a == 4
elif a-x == 1 and {horizontal} <= {-1,1}: print("4) Пешка сможет сменить позицию данным образом за один ход только если в точке назначения стоит вражеская фигура")
else: print("4) Пешка НЕ сможет сменить позицию данным образом за один ход")

input() #Из-за количества информации закрытие программы лучше доверить пользователю
