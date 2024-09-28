import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('Housing.csv')

# Bathroom sayısına göre ortalama ev fiyatlarını hesapla
bathroom_avg_price = data.groupby('bathrooms')['price'].mean()

plt.figure(figsize=(10, 5))
bathroom_avg_price.plot(kind='bar', color='skyblue')
plt.title('Ortalama Ev Fiyatları (Bathroom Sayısına Göre)')
plt.xlabel('Bathroom Sayısı')
plt.ylabel('Ortalama Fiyat')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()

# Furnishing status’a göre ortalama fiyatları hesapla
furnishing_avg_prices = data.groupby('furnishingstatus')['price'].mean().reset_index()

plt.figure(figsize=(10, 5))
plt.bar(furnishing_avg_prices['furnishingstatus'], furnishing_avg_prices['price'], color='salmon')
plt.title('Ortalama Ev Fiyatları - Furnishing Status’a Göre')
plt.xlabel('Furnishing Status')
plt.ylabel('Ortalama Fiyat')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()
