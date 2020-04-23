with open('task1.txt', 'w', encoding='UTF-8') as file:      #w, чтобы файл заново перезаписывался с нуля
    while True:
        text = input()
        if text!='':
            file.write(f'{text}\n')
        else:
            break