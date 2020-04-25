
###КЛАССИЧЕСКАЯ РАБОТА С ФАЙЛАМИ
#file = open('test.txt', 'rb') #Открыть в бинарном виде
# file = open('test.txt', 'a', encoding='UTF-8')
# try:
#     file.write('\nГаффи гаф')
# except Exception as e:
#     print(e)
# finally:
#     file.close()
# print(file)



###СИНТАКСИЧЕСКИЙ САХАР
import os

# data = {
#     'name': 'USER',
#     'surname': "SURNAME",
#     'id': 123321
# }

folder = 'data'
path = os.path.join(os.path.dirname(os.path.dirname(__file__)), folder)
# print(__file__)
#print(os.path.dirname(__file__))
# print(os.path.join(os.path.dirname(__file__), folder))
path = os.path.join(os.path.dirname(os.path.dirname(__file__)), folder)
# print(os.name)
# print(os.environ)
# print(os.path.isdir(path))
# print(os.listdir(path))

# os.mkdir(os.path.join(path, 'test')) #Создать папку
# os.rmdir(os.path.join(path, 'test')) #Удалить папку
# os.makedirs(['gav', 'gav1'], '')


import json

# data = {
#     'name': 'USER',
#     'surname': "SURNAME",
#     'id': 123321
# }

# with open('test.json', 'w', encoding='UTF-8') as file:
#     #file.write('\nГаффи гаф, гаф гаssф\n')
#     json.dump(data, file)
#     #print(file.read())
#
#
# with open('test.json', 'r', encoding='UTF-8') as file:
#     #file.write('\nГаффи гаф, гаф гаssф\n')
#     print(json.load(file))




import shutil
#
# folder2 = 'data2'
# path2 = os.path.join(os.path.dirname(os.path.dirname(__file__)), folder2)
#
# for itm in os.listdir(path):
#     # with open(os.path.join(path, itm), 'r') as file:
#     #     with open(os.path.join(path2, itm), 'w') as file2:
#     #         file2.write(file.read())
#     shutil.copy(os.path.join(path, itm), path2) #Копируем содержимое папки
#     #shutil.rmtree(path2) #удаляем рекурсивно директорию целиком



#os.environ['Ovcybyk'] = 'Овцебык'
print(os.environ)


# pyqt
# kiwi