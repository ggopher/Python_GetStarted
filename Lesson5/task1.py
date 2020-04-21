with open('task1.txt', 'w', encoding='UTF-8') as file:
    while True:
        text = input()
        if text!='':
            file.write(f'{text}\n')
        else:
            break