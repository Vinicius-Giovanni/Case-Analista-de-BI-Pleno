import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import warnings
from dataframes import creating_dataframe
import matplotlib.pyplot as plt
import statsmodels.api as sm

dataframe = creating_dataframe([
    'ano', 
    'pib_real_variacao_yoy',
    'taxa_de_cambio',
    'inflacao',
    'unidades_notebooks'
])  

warnings.filterwarnings('ignore')

# prevendo serie com ARIMA
def prev(df, col, years=2):
    serie = df.set_index('ano')[col]

    # ajude de modelo 
    model = ARIMA(serie, order=(1,1,0))
    result = model.fit()

    # prev
    forecast_result = result.get_forecast(steps=years)
    forecast = forecast_result.predicted_mean
    conf_int = forecast_result.conf_int()

    # new indice
    future_years = range(df['ano'].max() + 1, df['ano'].max() + years + 1)

    df_forecast = pd.DataFrame({'ano': future_years, col: forecast.values})

    # plot
    plt.figure(figsize=(10,6))
    plt.plot(df['ano'], df[col], label='Histórico', marker='o')
    plt.plot(future_years, forecast, label='Previsto', marker='x', color='orange')
    plt.fill_between(
        future_years,
        conf_int.iloc[:,0],
        conf_int.iloc[:,1],
        color = 'orange', alpha=0.2, label='IC 95%'
    )
    plt.title(f'Previsão {col} (ARIMA)')
    plt.xlabel('Ano')
    plt.ylabel(col)
    plt.legend()
    plt.grid(True)
    plt.show()

    return df_forecast


prev_pib = prev(dataframe, 'pib_real_variacao_yoy')
prev_cambio = prev(dataframe, 'taxa_de_cambio')
prev_inflacao = prev(dataframe, 'inflacao')

prevs = prev_pib.merge(prev_cambio, on='ano').merge(prev_inflacao, on='ano')

print(prevs)

cenarios = prevs.copy()
for col in ['inflacao']:
    base = prevs[col]
    std = dataframe[col].std()
    cenarios[f'{col}_pessimista'] = base + std
    cenarios[f'{col}_otimista'] = base - std

for col in ['taxa_de_cambio']:
    base = prevs[col]
    std = dataframe[col].std()
    cenarios[f'{col}_pessimista'] = base + std
    cenarios[f'{col}_otimista'] = base - std

for col in ['pib_real_variacao_yoy']:
    base = prevs[col]
    std = dataframe[col].std()
    cenarios[f'{col}_pessimista'] = base - std
    cenarios[f'{col}_otimista'] = base + std

print("\nCenários Gerados:")
print(cenarios[['ano', 'pib_real_variacao_yoy', 'taxa_de_cambio', 'inflacao']])
print(50*"-")
print(cenarios[['ano', 'pib_real_variacao_yoy_pessimista', 'taxa_de_cambio_pessimista', 'inflacao_pessimista']])
print(50*"-")
print(cenarios[['ano', 'pib_real_variacao_yoy_otimista', 'taxa_de_cambio_otimista', 'inflacao_otimista']])

# #Plotando (PIB)
# plt.figure(figsize=(8,4))
# plt.plot(dataframe['ano'], dataframe['pib_real_variacao_yoy'], label='Histórico', marker='o')
# plt.plot(prevs['ano'], prevs['pib_real_variacao_yoy'], label='Base', marker='x', color='orange')
# plt.plot(prevs['ano'], cenarios['pib_real_variacao_yoy_pessimista'], label='Pessimista', linestyle='--', color='red')
# plt.plot(prevs['ano'], cenarios['pib_real_variacao_yoy_otimista'], label='Otimista', linestyle='--', color='blue')


# plt.title("Cenários Macroeconômicos - PIB Real (%)")
# plt.xlabel("Ano")
# plt.ylabel("PIB (%)")
# plt.legend()
# plt.grid(True)
# plt.show()

#Plotando (inflacao)
plt.figure(figsize=(8,4))
plt.plot(dataframe['ano'], dataframe['inflacao'], label='Histórico', marker='o')
plt.plot(prevs['ano'], prevs['inflacao'], label='Base', marker='x', color='orange')
plt.plot(prevs['ano'], cenarios['inflacao_pessimista'], label='Pessimista', linestyle='--', color='red')
plt.plot(prevs['ano'], cenarios['inflacao_otimista'], label='Otimista', linestyle='--', color='blue')


plt.title("Cenários Macroeconômicos - Inflação (%)")
plt.xlabel("Ano")
plt.ylabel("Inflação (%)")
plt.legend()
plt.grid(True)
plt.show()

#Plotando (taxa de cambio)
plt.figure(figsize=(8,4))
plt.plot(dataframe['ano'], dataframe['taxa_de_cambio'], label='Histórico', marker='o')
plt.plot(prevs['ano'], prevs['taxa_de_cambio'], label='Base', marker='x', color='orange')
plt.plot(prevs['ano'], cenarios['taxa_de_cambio_pessimista'], label='Pessimista', linestyle='--', color='red')
plt.plot(prevs['ano'], cenarios['taxa_de_cambio_otimista'], label='Otimista', linestyle='--', color='blue')


plt.title("Cenários Macroeconômicos - Taxa de Câmbio US$")
plt.xlabel("Ano")
plt.ylabel("Taxa de Câmbio US$")
plt.legend()
plt.grid(True)
plt.show()

# prevendo vendas

def prev_vendas(model, cambio):
    return model.params['const'] + model.params['taxa_de_cambio'] * cambio


# model
x = dataframe[['taxa_de_cambio']]
x = sm.add_constant(x)
y = dataframe['unidades_notebooks']

model = sm.OLS(y, x).fit()

# Montando tabela de previsões
tabela_cenarios = pd.DataFrame({
    'ano': prevs['ano'],
    'cambio_base': prevs['taxa_de_cambio'],
    'cambio_pessimista': cenarios['taxa_de_cambio_pessimista'],
    'cambio_otimista': cenarios['taxa_de_cambio_otimista']
})

# Aplicando o modelo
tabela_cenarios['vendas_base'] = prev_vendas(model, tabela_cenarios['cambio_base'])
tabela_cenarios['vendas_pessimista'] = prev_vendas(model, tabela_cenarios['cambio_pessimista'])
tabela_cenarios['vendas_otimista'] = prev_vendas(model, tabela_cenarios['cambio_otimista'])

# Exibindo resultados
print("\nPrevisão de Vendas de Notebooks (por cenário):")
print(tabela_cenarios[['ano', 'vendas_pessimista', 'vendas_base', 'vendas_otimista']].round(0))

# plotando
plt.figure(figsize=(8,4))
plt.plot(tabela_cenarios['ano'], tabela_cenarios['vendas_base'], label='Base', marker='x', color='orange')
plt.plot(tabela_cenarios['ano'], tabela_cenarios['vendas_pessimista'], label='Pessimista', linestyle='--', color='red')
plt.plot(tabela_cenarios['ano'], tabela_cenarios['vendas_otimista'], label='Otimista', linestyle='--', color='blue')
plt.title("Previsão de Vendas de Notebooks (por cenário)")
plt.xlabel("Ano")
plt.ylabel("Vendas Previstas (unidades)")
plt.legend()
plt.grid(True)
plt.show()