import pandas as pd
import matplotlib.pyplot as plt
from dataframes import creating_dataframe

inflacao = creating_dataframe(['ano', 'inflacao'])

# Plotando

plt.figure()

plt.plot(inflacao['ano'],
         inflacao['inflacao'],
         marker='o')

# mostrando todos os ticks do eixo-x
plt.xticks(inflacao['ano'], rotation=45)

# Adicionar rótulos de valor
for i, row in inflacao.iterrows(): # iterrows() é um iterador linha-a-linha sobre um df
    plt.text(
        row['ano'], 
        row['inflacao'] + 0.002,  # deslocamento vertical
        f"{row['inflacao']*100:.2f}%", 
        ha='center', 
        va='bottom'
    )

plt.title("Inflação Anual")
plt.xlabel("Ano")
plt.ylabel("Inflação")
plt.grid(True)

plt.show()