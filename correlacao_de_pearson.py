import pandas as pd
import matplotlib.pyplot as plt
from dataframes import creating_dataframe

df = creating_dataframe([
    'ano', 
    'pib_real_variacao_yoy',
    'pib_per_capita_ano_passado',
    'pib_per_capita_ano_atual',
    'pip_per_capita',
    'renda_media_familia_pnad',
    'taxa_de_desemprego',
    'taxa_de_cambio',
    'inflacao',
    'selic',
    'populacao_total',
    'domicilios',
    'unidades_notebooks'
])

# variáveis macro
macros = [
    'pib_real_variacao_yoy',
    'pib_per_capita_ano_passado',
    'pib_per_capita_ano_atual',
    'pip_per_capita',
    'renda_media_familia_pnad',
    'taxa_de_desemprego',
    'taxa_de_cambio',
    'inflacao',
    'selic',
    'populacao_total',
    'domicilios'
]

# correlação de Pearson
correlacoes = df[macros + ['unidades_notebooks']].corr(method='pearson')['unidades_notebooks'].sort_values(ascending=False)

# Gráfico de barras horizontais
plt.figure(figsize=(8,6))
bars = plt.barh(correlacoes.drop('unidades_notebooks').index, correlacoes.drop('unidades_notebooks').values, color='skyblue')
plt.title('Correlação de Pearson com Vendas de Notebooks')
plt.xlabel('Coeficiente r de Pearson')
plt.ylabel('Variável Macroeconômica')
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Adiciona os rótulos
for bar in bars:
    plt.text(
        bar.get_width() + 0.01 * (1 if bar.get_width() > 0 else -1),  # desloca um pouco pra direita ou esquerda
        bar.get_y() + bar.get_height()/2,
        f"{bar.get_width():.2f}",   # formata com 2 casas decimais
        va='center',
        ha='left' if bar.get_width() > 0 else 'right'
    )
print(correlacoes)
plt.tight_layout()
plt.show()


