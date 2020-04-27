"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и
возвращающую его же, но с прописной первой буквой.Например, print(int_func(‘text’)) -> Text
"""

def int_func(string: str)-> str:
    """
    Делаем певрую букву в строке заглавной
    :param string: str
    :return: str
    """
    return string.title()


#простой вариант
while True:
    # простой вариант
    data = input("Введите строку на латиннице\n")
    print(int_func(data))

    # более сложный вариант с перебором каждого слова:
    data = data.split(' ')
    result = ""
    for key in data:
        key = int_func(key)
        result += key + ' '
    print(result[0:-1]) #последний пробел можно убрать и по другому. Решил попробовать принцип простое лучше сложного )
