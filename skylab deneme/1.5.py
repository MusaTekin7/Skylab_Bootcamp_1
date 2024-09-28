import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Housing.csv')

house_areas = [
    (16000, '16k'),
    (15000, '15k'),
    (14000, '14k'),
    (13000, '13k'),
    (12000, '12k'),
    (11000, '11k'),
    (10000, '10k'),
    (9000, '9k'),
    (8000, '8k'),
    (7000, '7k'),
    (6000, '6k'),
    (5000, '5k'),
    (4000, '4k'),
    (3000, '3k'),
    (2000, '2k'),
    (1000, '1k'),
]


def house_area(area):
    for alt_sinir, k in house_areas:
        if area >= alt_sinir:
            return k

df['house area'] = df['area'].apply(house_area)

alan_sayilari = df['house area'].value_counts()

# plt.barh(alan_sayilari.index, alan_sayilari.values)
# plt.title('zort')
# plt.xlabel('zurt')
# plt.ylabel('zart')




house_prices = [
    (13000000, '13billion'),
    (12000000, '12billion'),
    (11000000, '11billion'),
    (10000000, '10billion'),
    (9000000, '9billion'),
    (8000000, '8billion'),
    (7000000, '7billion'),
    (6000000, '6billion'),
    (5000000, '5billion'),
    (4000000, '4billion'),
    (3000000, '3billion'),
    (2000000, '2billion'),
    (1000000, '1billion'),
]

def house_price(price):
    for kucuk_sinir, l in house_prices:
        if price >= kucuk_sinir:
            return l

df['house price'] = df['price'].apply(house_price)

fiyat_sayilari = df['house price'].value_counts()

# plt.barh(fiyat_sayilari.index, fiyat_sayilari.values)
# plt.title('zort')
# plt.xlabel('zurt')
# plt.ylabel('zart')



plt.scatter(df['house area'], df['house price'])

plt.show()
