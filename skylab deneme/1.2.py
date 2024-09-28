import csv

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Housing.csv')

data = []
with open('Housing.csv') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        data.append(dict(row))

stories_file = [x['stories'] for x in data]
price_two = [x['price'] for x in data]

plt.plot(stories_file,price_two,'co')
plt.show()

