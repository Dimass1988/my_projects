import diff
import pandas as pd

# Загрузка данных из файлов
df1 = pd.read_excel('C:/Users/Dimas/Desktop/Таблица1.xlsx')
df2 = pd.read_excel('C:/Users/Dimas/Desktop/Таблица2.xlsx')

# Сравнение на равенство (без учета индексов)
comparison = df1.equals(df2)

if comparison:
    print("Таблицы идентичны.")
else:
    print("Таблицы различаются.")

# Если нужно найти конкретные различия, можно использовать другие методы, например:
# Сравнение по ячейкам
#diff = df1 != df2

# Найти строки и столбцы, где есть различия
changed_cells = diff.any(axis=1)

# Вывести строки с различиями
if changed_cells.any():
    print("Различия найдены в следующих строках:")
    print(df1[changed_cells])
    print(df2[changed_cells])
else:
    print("Различий нет.")
