from dataframes import creating_dataframe
import statsmodels.api as sm
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

df = creating_dataframe([
    'ano', 
    'pib_real_variacao_yoy',
    'taxa_de_cambio',
    'inflacao',
    'unidades_notebooks'
])

x = df[[
    'taxa_de_cambio'
]]

y = df['unidades_notebooks']

# adiciona intercepto
x = sm.add_constant(x)
model = sm.OLS(y, x).fit()

# previsao
y_pred = model.predict(x)
y_true = y

# MAE  e RMSE
mae = mean_absolute_error(y, y_pred)
rmse = np.sqrt(mean_squared_error(y, y_pred))

print(model.summary())
print('R² ajustado:', model.rsquared_adj)
print('MAE:', round(mae,2))
print('RMSE:', round(rmse,2))

# real vs previsto
plt.figure(figsize=(10,6))
plt.scatter(y_pred, y_true, color=['blue'])
plt.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], 'r--', lw=2)
plt.xlabel('Venda Reais (unidades)')
plt.ylabel('Vendas Previstas (unidades)')
plt.title('Real vs Previsto - Taxa de Câmbio')
plt.grid(True)
plt.show()

# Residuos vs Previsto
residuos = y_true - y_pred
plt.figure(figsize=(10,6))
plt.scatter(y_pred, residuos, color='orange')
plt.axhline(0, color ='red', linestyle='--', lw=2)
plt.xlabel('Vendas Previstas (unidades)')
plt.ylabel('Resíduos')
plt.title('Resíduos vs Previsto')
plt.grid(True)
plt.show()

# previsão de vendas para análise de sensibilidade
cambio_test = np.linspace(df['taxa_de_cambio'].min()-1, df['taxa_de_cambio'].max()+1, 50)
previcoes = model.params['const'] + model.params['taxa_de_cambio'] * cambio_test

plt.plot(cambio_test, previcoes)
plt.xlabel('Taxa de Câmbio')
plt.ylabel('Previsão de vendas (unidades)')
plt.title('Análise de Sensibilidade: Impacto da Taxa de Câmbio')
plt.grid(True)
plt.show()