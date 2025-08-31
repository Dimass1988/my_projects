import pandas as pd
import numpy as np

# Загрузка данных
df1 = pd.read_excel('C:/Users/Dimas/Desktop/Таблица1.xlsx').fillna('')
df2 = pd.read_excel('C:/Users/Dimas/Desktop/Таблица2.xlsx').fillna('')

# Проверяем, одинаковы ли формы таблиц
if df1.shape != df2.shape:
    print("Таблицы имеют разную размерность.")
else:
    # Создаем массив boolean, где True означает различие
    diff_mask = (df1 != df2)
    # Получаем индексы строк и столбцов, где есть различия
    rows, cols = np.where(diff_mask)

    if len(rows) == 0:
        print("Таблицы идентичны.")
    else:
        print("Различия найдены в следующих ячейках:")
        for row, col in zip(rows, cols):
            print(f"Строка {row + 1}, Колонка {col + 1}:")
            print(f"  В file1: {df1.iloc[row, col]}")
            print(f"  В file2: {df2.iloc[row, col]}")