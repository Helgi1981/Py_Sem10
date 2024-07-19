# Задача №3. Решение в группах

# Создать новый столбец в таблице с пингвинами, который будет отвечать за показатель 
# длины клюва пингвина.
# high - длинный(от 42)
# middle - средний(от 35 до 42)
# low - маленький(до 35)

# Чтобы подключить датасет с пингвинами, воспользуйтесь данным скриптом:
# penguins = sns.load_dataset("penguins")
# penguins.head()

import seaborn as sns

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

# Просмотр первых нескольких строк с новым столбцом
print(penguins.head())


"""
Этот код:

- Загружает датасет и удаляет строки с пропущенными значениями.
- Определяет функцию classify_bill_length, которая классифицирует длину клюва на три 
категории: high, middle и low.
- Применяет эту функцию к столбцу bill_length_mm с помощью метода apply, создавая новый 
столбец bill_length_category.
"""