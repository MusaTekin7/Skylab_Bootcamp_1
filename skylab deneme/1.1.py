import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Housing.csv')

numeric_data = data.select_dtypes(include='number')

correlation_matrix = numeric_data.corr()

plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar_kws={"shrink": .8})
plt.title('Korelasyon Matrisi')
plt.show()
