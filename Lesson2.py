var_str = "Это строка текста"

#var_str[-1:0:]
#var_str[0:0:]


# var_list = [1, 2.3, 'strings', True, None]
# var_tuple
# var_list[0] = 22
# [::2] #Через один

var_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for itm in var_list[:]:
    var_list.append(itm * 2)
print(var_list)


names = ['1', '2', '3', '4', '5', '6', '7', '6']
c = set(names)
