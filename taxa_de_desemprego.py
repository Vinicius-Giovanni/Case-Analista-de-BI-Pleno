import pandas as pd
import matplotlib.pyplot as plt
from dataframes import creating_dataframe

taxa_de_desemprego = creating_dataframe(['ano', 'taxa_de_desemprego'])

# Plotando

plt.figure()

plt.plot(taxa_de_desemprego['ano'],
         taxa_de_desemprego['taxa_de_desemprego'],
         marker='o')

# mostrando todos os ticks do eixo-x
plt.xticks(taxa_de_desemprego['ano'], rotation=45)

# Adicionar rótulos de valor
for i, row in taxa_de_desemprego.iterrows(): # iterrows() é um iterador linha-a-linha sobre um df
    plt.text(
        row['ano'], 
        row['taxa_de_desemprego'] + 0.002,  # deslocamento vertical
        f"{row['taxa_de_desemprego']*100:.2f}%", 
        ha='center', 
        va='bottom'
    )

plt.title("Variação Anual da Taxa de Desemprego (YoY)")
plt.xlabel("Ano")
plt.ylabel("Variação (YoY)")
plt.grid(True)

plt.show()