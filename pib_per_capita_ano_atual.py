import pandas as pd
import matplotlib.pyplot as plt
from dataframes import creating_dataframe

pib_per_capita_ano_atual = creating_dataframe(['ano','pib_per_capita_ano_atual'])

plt.plot(pib_per_capita_ano_atual['ano'],
         pib_per_capita_ano_atual['pib_per_capita_ano_atual'],
         marker='o')

# mostrando todos os ticks do eixo-x
plt.xticks(pib_per_capita_ano_atual['ano'], rotation=45)

# Adicionar rótulos de valor
for i, row in pib_per_capita_ano_atual.iterrows(): # iterrows() é um iterador linha-a-linha sobre um df
    plt.text(
        row['ano'],
        row['pib_per_capita_ano_atual'] + 0.002, # deslocamento vertical
        f"{row['pib_per_capita_ano_atual']}",
        ha='center',
        va='bottom'
    )

plt.title("PIB Per Capita R$")
plt.xlabel("Ano")
plt.ylabel("PIB R$")
plt.grid(True)

plt.show()