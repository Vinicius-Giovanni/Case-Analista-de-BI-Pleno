import pandas as pd
import matplotlib.pyplot as plt
from dataframes import creating_dataframe

pip_per_capita = creating_dataframe(['ano', 'pip_per_capita'])

# Plotando

plt.figure()

plt.plot(pip_per_capita['ano'],
         pip_per_capita['pip_per_capita'],
         marker='o')

# mostrando todos os ticks do eixo-x
plt.xticks(pip_per_capita['ano'], rotation=45)

# Adicionar rótulos de valor
for i, row in pip_per_capita.iterrows(): # iterrows() é um iterador linha-a-linha sobre um df
    plt.text(
        row['ano'], 
        row['pip_per_capita'] + 0.002,  # deslocamento vertical
        f"{row['pip_per_capita']*100:.1f}%", 
        ha='center', 
        va='bottom'
    )

plt.title("Variação Anual do PIB Per Capita (YoY)")
plt.xlabel("Ano")
plt.ylabel("Variação (YoY)")
plt.grid(True)

plt.show()