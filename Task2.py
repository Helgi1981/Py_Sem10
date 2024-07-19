# Задача №2. Решение в группах

# Написать EDA для датасета про пингвинов
# Необходимо:
# ● Использовать 2-3 точечных графика
# ● Применить доп измерение в точечных графиках, используя аргументы hue, size, stile
# ● Использовать PairGrid с типом графика на ваш выбор
# ● Изобразить Heatmap
# ● Использовать 2-3 гистограммы

# Чтобы подключить датасет с пингвинами, воспользуйтесь данным скриптом:
# penguins = sns.load_dataset("penguins")
# penguins.head()

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Загрузка датасета
penguins = sns.load_dataset("penguins")

# Удаление строк с пропущенными значениями
penguins = penguins.dropna()

# Точечные графики с дополнительными измерениями
plt.figure(figsize=(10, 6))

# Точечный график 1
plt.subplot(1, 2, 1)
sns.scatterplot(data=penguins, x='bill_length_mm', y='bill_depth_mm', hue='species', style='island', size='body_mass_g')
plt.title('Bill Length vs Bill Depth')

# Точечный график 2
plt.subplot(1, 2, 2)
sns.scatterplot(data=penguins, x='flipper_length_mm', y='body_mass_g', hue='species', style='island', size='bill_length_mm')
plt.title('Flipper Length vs Body Mass')

plt.tight_layout()
plt.show()

# PairGrid с типом графика на ваш выбор
g = sns.PairGrid(penguins, hue="species")
g.map_diag(sns.histplot)
g.map_offdiag(sns.scatterplot)
g.add_legend()

# Heatmap корреляции переменных
plt.figure(figsize=(10, 8))
# Использование только числовых данных для корреляционной матрицы
sns.heatmap(penguins.select_dtypes(include=['float64', 'int64']).corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Гистограммы
plt.figure(figsize=(12, 6))

# Гистограмма 1
plt.subplot(1, 3, 1)
sns.histplot(penguins['bill_length_mm'], kde=True)
plt.title('Bill Length Distribution')

# Гистограмма 2
plt.subplot(1, 3, 2)
sns.histplot(penguins['flipper_length_mm'], kde=True)
plt.title('Flipper Length Distribution')

# Гистограмма 3
plt.subplot(1, 3, 3)
sns.histplot(penguins['body_mass_g'], kde=True)
plt.title('Body Mass Distribution')

plt.tight_layout()
plt.show()


"""
Этот код включает:

- Два точечных графика с дополнительными измерениями.
- PairGrid с гистограммами на диагоналях и точечными графиками вне диагоналей.
- Тепловую карту корреляции переменных.
- Три гистограммы для распределения длины клюва, длины ласт и массы тела пингвинов.
"""