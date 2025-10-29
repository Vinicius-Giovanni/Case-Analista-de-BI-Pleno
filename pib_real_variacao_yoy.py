import pandas as pd
import matplotlib.pyplot as plt
from dataframes import creating_dataframe

pib_real_variacao_yoy = creating_dataframe(['ano', 'pib_real_variacao_yoy'])

# Plotando

plt.figure(figsize=(12,6))

plt.plot(pib_real_variacao_yoy['ano'],
         pib_real_variacao_yoy['pib_real_variacao_yoy'],
         marker='o')

# mostrando todos os ticks do eixo-x
plt.xticks(pib_real_variacao_yoy['ano'], rotation=45)

# Adicionar rótulos de valor
for i, row in pib_real_variacao_yoy.iterrows(): # iterrows() é um iterador linha-a-linha sobre um df
    plt.text(
        row['ano'], 
        row['pib_real_variacao_yoy'] + 0.002,  # deslocamento vertical
        f"{row['pib_real_variacao_yoy']*100:.1f}%", 
        ha='center', 
        va='bottom'
    )

plt.title("Variação Anual do PIB Real (YoY)")
plt.xlabel("Ano")
plt.ylabel("Variação (YoY)")
plt.grid(True)

plt.show()