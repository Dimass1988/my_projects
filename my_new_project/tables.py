import pandas as pd

# Загрузка файлов
df1 = pd.read_excel('C:/Users/Dimas/Desktop/Таблица1.xlsx')
df2 = pd.read_excel('C:/Users/Dimas/Desktop/Таблица2.xlsx')

# Сравнение
comparison = df1.compare(df2)
print(comparison)

# Сохранение результатов
comparison.to_excel('C:/Users/Dimas/Desktop/Задание/различия.xlsx')
