import pandas as pd
import matplotlib.pyplot as plt

data = {
    'День': ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'],
    'Температура (°C)': [18, 20, 22, 19, 17, 15, 14],
    'Осадки (мм)': [0, 2, 1, 5, 3, 10, 8]
}

df = pd.DataFrame(data)
print("DataFrame с данными о погоде:")
print(df)

plt.figure(figsize=(8, 5))
plt.plot(df['День'], df['Температура (°C)'], marker='o', linestyle='-', color='red', linewidth=2)
plt.title('Изменение температуры за неделю')
plt.xlabel('День недели')
plt.ylabel('Температура (°C)')
plt.grid(True)
plt.savefig('temperature_plot.png')
plt.show()