my_list = [1, 2, 1, 4, 5, 6, 7, 8]

#new_list = [itm ** 2 for itm in my_list if not itm & 1]
new_list = {itm: itm ** 2 for itm in my_list if not itm & 1}
print(new_list)