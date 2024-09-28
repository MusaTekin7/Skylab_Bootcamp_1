import csv

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Housing.csv')

data = []
with open('Housing.csv') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        data.append(dict(row))

bedroom = [x['bedrooms'] for x in data]
priceone = [x['price'] for x in data]

plt.plot(bedroom, priceone,'co')
plt.show()