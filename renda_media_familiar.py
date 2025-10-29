import pandas as pd
import matplotlib.pyplot as plt
from dataframes import creating_dataframe

renda_media_familia_pnad = creating_dataframe(['ano','renda_media_familia_pnad'])

plt.plot(renda_media_familia_pnad['ano'],
         renda_media_familia_pnad['renda_media_familia_pnad'],
         marker='o')

# mostrando todos os ticks do eixo-x
plt.xticks(renda_media_familia_pnad['ano'], rotation=45)

# Adicionar rótulos de valor
for i, row in renda_media_familia_pnad.iterrows(): # iterrows() é um iterador linha-a-linha sobre um df
    plt.text(
        row['ano'],
        row['renda_media_familia_pnad'] + 0.002, # deslocamento vertical
        f"{row['renda_media_familia_pnad']}",
        ha='center',
        va='bottom'
    )

plt.title("Renda Média Anual por Familia R$")
plt.xlabel("Ano")
plt.ylabel("Renda R$")
plt.grid(True)

plt.show()