import sys
from time import time as time, sleep
import  requests
import json
import itertools

#from modules.main_module import my_sum
#print(my_sum(2, 5))


if __name__ == '__main__':
        # print(sys.argv)
        # print(__name__)
        # _, x, y, *z = sys.argv
        # print(int(x), int(y))
        times = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

        def my_cycle(my_iter):
                i = 0
                while True:
                        yield my_iter[i]
                        i += 1
                        if i == len(my_iter):
                                i = 0


        #for itm in itertools.cycle(times):
        for itm in my_cycle(times):
                print(itm)
                sleep(0.1)



"""
import datetime as dt

start = time()
for itm in range(10):
        print(itm)
 #       sleep(2)

end = time()
print(end - start)


now = dt.datetime.now
delta = dt.timedelta(days=2)
now = now - delta

print(dt.datetime.now())

now.timestamp()
"""


#response = requests.get('https://geekbrains.ru')
#response.headers
#print(response.hr)


#Вторая часть урока

"""
my_dict = {'name' : 275684554365,
           'surname' : 254564564365,
           'lastname' : 23565254365,
           'my_list': [1, 2, 3, 4],
           'my_tuple': (2, 3, 4, 5),
           'None': None,
           "BOOL": True, }
j_data = json.dumps(my_dict)
print(j_data)


new_data = json.loads(j_data)
print(new_data)
"""

#Третья часть урока

# my_list = [1, 2, 3, 4, 5, 6, 7, 8]
# #new_list = [itm ** 2 for itm in my_list if not itm & 1]
# new_list = {itm: itm ** 2 for itm in my_list if not itm & 1}
# print(new_list)


#Четвертая часть урока


