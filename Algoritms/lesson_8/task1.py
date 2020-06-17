"""
1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
"""
n = int(input('Введите число друзей:\n'))
graph = list()

for i in range(n):
    graph.append([0] * (n - i) + [1] * i if n >= i else [1 * n - i])

print(*graph, sep='\n')
final = 0
for itm in graph:
    final += sum(itm)
print(f'Количество рукопожатий: {final}')
check = n * (n - 1)/2
print(f'Проверочное число: {check}')