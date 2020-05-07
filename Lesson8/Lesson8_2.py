import requests


class AmyError(Exception):
    def __init__(self, text):
        self.text = text

class Product:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    def __str__(self):
        return getattr(self, 'name')

class SpecialOfferCatalog:
    def __init__(self, url):
        self.__url = url
        self.__products = []
        self.headers = {'User-agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36'}
        self.__parse()
    def __parse(self):
        url = self.__url
        while url:
            response = requests.get(url, headers=self.headers)
            data = response.json()
            url = data['next']
            # self.__products.extend(data['results'])
            self.__products.extend([Product(**itm) for itm in data['results']])
            # print(self.__products)
    def __iter__(self):
        return self.__products.__iter__()

    @staticmethod
    def get_page(url):
        return requests.get(url, headers=SpecialOfferCatalog.headers)


class MyTemp:
    __item1 = 12354
    @staticmethod
    def func1():
        return 22

    @classmethod
    def cls_method(cls):
        return cls.__item1

if __name__ == '__main__':
    a = MyTemp.func1()
    a = MyTemp.cls_method()
    # raise AmyError('SOME TEXT')
    # url = 'https://5ka.ru/api/v2/special_offers/'
    # catalog = SpecialOfferCatalog(url)
    #
    # for itm in catalog:
    #     print(itm)
    #     print(1)


date = {'ddf': 'sdfsdf'}

print(date.item())