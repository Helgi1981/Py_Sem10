# Задача №4. Общее обсуждение

# Изобразить гистограмму по flipper_length_mm с оттенком height_group. Сделать анализ

import seaborn as sns
import matplotlib.pyplot as plt

# Загрузка датасета
penguins = sns.load_dataset("penguins")

# Удаление строк с пропущенными значениями
penguins = penguins.dropna()

# Функция для классификации длины клюва
def classify_bill_length(bill_length):
    if bill_length >= 42:
        return 'high'
    elif 35 <= bill_length < 42:
        return 'middle'
    else:
        return 'low'

# Добавление нового столбца с классификацией длины клюва
penguins['bill_length_category'] = penguins['bill_length_mm'].apply(classify_bill_length)

# Гистограмма по flipper_length_mm с оттенком bill_length_category
plt.figure(figsize=(10, 6))
sns.histplot(data=penguins, x='flipper_length_mm', hue='bill_length_category', multiple='stack', kde=True)
plt.title('Distribution of Flipper Length with Bill Length Category')
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Frequency')
plt.show()


"""
Анализ:

1. Распределение по категориям: На гистограмме видно, как распределены пингвины с разной 
длиной клюва (high, middle, low) по длине ласт (flipper_length_mm). Можно заметить, 
что каждая категория имеет определенный диапазон значений.
2. Основная масса: Для каждой категории длины клюва существует определенная плотность 
пингвинов в диапазонах длины ласт. Например, пингвины с маленьким клювом (low) в 
основном сосредоточены в нижней части распределения длины ласт.
3. Перекрытие категорий: Наблюдается некоторое перекрытие между категориями, особенно 
между middle и high, что может свидетельствовать о том, что длина ласт не всегда четко 
коррелирует с длиной клюва.
4. Кривая KDE: Добавление кривой KDE (Kernel Density Estimate) помогает лучше понять 
распределение данных и дает представление о вероятностной плотности для каждой категории.

Эти наблюдения могут быть полезны для дальнейшего анализа биологических характеристик 
пингвинов и их возможных взаимосвязей.
"""