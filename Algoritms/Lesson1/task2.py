x1 = int(input('введите x первой точки:\n'))
y1 = int(input('введите y первой точки:\n'))1
x2 = int(input('введите x второй точки:\n'))
y2 = int(input('введите y второй точки:\n'))
k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2
print(f'y = {k}x + {b}')