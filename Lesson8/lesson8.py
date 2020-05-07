import requests


class Product:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    def __str__(self):
        price_reg, price_min = getattr(self, 'current_prices').values()
        return getattr(self, 'name') + ' Цена: ' + str(price_min) + ' Цена старая: ' + str(price_reg)

class SpecialOfferCatalog:
    def __init__(self, url):
        self.__url = url
        self.__products = []
        self.headers = {'User-agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36'}
        self.__parse()
    def __parse(self):
        url = self.__url
        while url:
        # for i in range(1):
            response = requests.get(url, headers=self.headers)
            data = response.json()
            url = data['next']
            # self.__products.extend(data['results'])
            self.__products.extend([Product(**itm) for itm in data['results']])
            # print(self.__products)
    def __iter__(self):
        return self.__products.__iter__()


if __name__ == '__main__':
    url = 'https://5ka.ru/api/v2/special_offers/'
    catalog = SpecialOfferCatalog(url)

    for itm in catalog:
        print(itm)
        # print(itm.current_prices['price_promo__min'])
    # print(f'Всего товаров: {len(catalog)}')