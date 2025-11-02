import pandas as pd
import matplotlib.pyplot as plt
from dataframes import creating_dataframe
import matplotlib.pyplot as plt
import seaborn as sns


df = creating_dataframe([
    'ano', 
    'pib_real_variacao_yoy',
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

def pearson_pip_per_capita():
    # Estilo
    sns.set(style="whitegrid", context="talk")

    # grafico de dispersão com linha de tendência
    plt.figure(figsize=(10,6))

    sns.regplot(
        data=df,
        x='pip_per_capita',
        y='unidades_notebooks',
        scatter_kws={'s':70, 'alpha':0.8},
        line_kws={'color':'red'}
    )

    # rótulos de dados: anos
    for i in range(len(df)):
        plt.text(
            df['pip_per_capita'].iloc[i],
            df['unidades_notebooks'].iloc[i],
            df['ano'].iloc[i],
            fontsize=10,
            ha='left', va='bottom'
        )

    # correlação númerica
    corr = df['pip_per_capita'].corr(df['unidades_notebooks'])

    # title e rotulo
    plt.title(f'Variação do PIB Per Capita % (YoY) vs Unidades de Notebooks | Correlação: {corr:.2f}', fontsize=16)
    plt.xlabel('PIB Per Capita - variação % (YoY)')
    plt.ylabel('Unidades de Notebooks Vendidas')
    plt.grid(False)

    plt.tight_layout()
    plt.show()

def pearson_pib_real_variacao_yoy():
    # Estilo
    sns.set(style="whitegrid", context="talk")

    # grafico de dispersão com linha de tendência
    plt.figure(figsize=(10,6))

    sns.regplot(
        data=df,
        x='pib_real_variacao_yoy',
        y='unidades_notebooks',
        scatter_kws={'s':70, 'alpha':0.8},
        line_kws={'color':'red'}
    )

    # rótulos de dados: anos
    for i in range(len(df)):
        plt.text(
            df['pib_real_variacao_yoy'].iloc[i],
            df['unidades_notebooks'].iloc[i],
            df['ano'].iloc[i],
            fontsize=10,
            ha='left', va='bottom'
        )
    
    # correlação númerica
    corr = df['pib_real_variacao_yoy'].corr(df['unidades_notebooks'])

    # title e rotulo
    plt.title(f'Variação do PIB Real % (YoY) vs Unidades de Notebooks | Correlação: {corr:.2f}', fontsize=16)
    plt.xlabel('PIB real - variação % (YoY)')
    plt.ylabel('Unidades de Notebooks Vendidas')

    plt.tight_layout()
    plt.show()

def renda_media_familia_pnad():
    # estilo
    sns.set(style="whitegrid", context="talk")

    # grafico de dispersão com linha de tendência
    plt.figure(figsize=(10,6))

    sns.regplot(
        data=df,
        x='renda_media_familia_pnad',
        y='unidades_notebooks',
        scatter_kws={'s':70, 'alpha':0.8},
        line_kws={'color':'red'}
    )

    # rotulos de dados:anos
    for i in range(len(df)):
        plt.text(
            df['renda_media_familia_pnad'].iloc[i],
            df['unidades_notebooks'].iloc[i],
            df['ano'].iloc[i],
            fontsize=10,
            ha='left',
            va='bottom'
        )

    # correlação númerica
    corr = df['renda_media_familia_pnad'].corr(df['unidades_notebooks'])

    # title and rotulo
    plt.title(f'Variação da Renda Média Familiar R$ vs Unidades de Notebooks | Correlação: {corr:.2f}')
    plt.xlabel('Renda Familiar - Média R$)')
    plt.ylabel('Unidade de Notebooks Vendidas')

    plt.tight_layout()
    plt.show()

def taxa_de_desemprego():
    # estilo
    sns.set(style="whitegrid", context="talk")
    # grafico de dispersão com linha de tendência
    plt.figure(figsize=(10,6))

    sns.regplot(
        data=df,
        x='taxa_de_desemprego',
        y='unidades_notebooks',
        scatter_kws={'s':70, 'alpha':0.8},
        line_kws={'color':'red'}
    )

    # rotulos de dados: anos
    for i in range(len(df)):
        plt.text(
            df['taxa_de_desemprego'].iloc[i],
            df['unidades_notebooks'].iloc[i],
            df['ano'].iloc[i],
            fontsize=10,
            ha='left',
            va='bottom'
        )

    #correlacao numerica
    corr = df['taxa_de_desemprego'].corr(df['unidades_notebooks'])

    # title and rotulo
    plt.title(f'Variação da Taxa de Desemprego % | Correlação: {corr:.2f}')
    plt.xlabel('Taxa de Desemprego - Percentual %')
    plt.ylabel('Unidade de Notebooks Vendidas')

    plt.tight_layout()
    plt.show()

def taxa_de_cambio():
    # estilo
    sns.set(style='whitegrid',context='talk')
    # grafico de dispersão com linha de tendência
    plt.figure(figsize=(10,6))

    sns.regplot(
        data=df,
        x='taxa_de_cambio',
        y='unidades_notebooks',
        scatter_kws={'s':70, 'alpha':0.8},
        line_kws={'color':'red'}
    )

    # rotulo de dados: anos
    for i in range(len(df)):
        plt.text(
            df['taxa_de_cambio'].iloc[i],
            df['unidades_notebooks'].iloc[i],
            df['ano'].iloc[i],
            fontsize=10,
            ha='left',
            va='bottom'
        )

    # correlacao numerica
    corr = df['taxa_de_cambio'].corr(df['unidades_notebooks'])

    # title and rotulo
    plt.title(f'Variação da Tava de Cambio R$ | Correlação: {corr:.2f}')
    plt.xlabel('Taxa de Câmbio - Real R$')
    plt.ylabel('Unidade de Notebooks Vendidas')

    plt.tight_layout()
    plt.show()

def selic():
    # estilo 
    sns.set(style="whitegrid", context='talk')
    # grafico de dispersao com linha de tendencia
    plt.figure(figsize=(10,6))

    sns.regplot(
        data=df,
        x='selic',
        y='unidades_notebooks',
        scatter_kws={'s':70, 'alpha':0.8},
        line_kws={'color':'red'}
    )

    # rotulos de dados: anos
    for i in range(len(df)):
        plt.text(
            df['selic'].iloc[i],
            df['unidades_notebooks'].iloc[i],
            df['ano'].iloc[i],
            fontsize=10,
            ha='left',
            va='bottom'
        )

    # correlação linear
    corr = df['selic'].corr(df['unidades_notebooks'])

    #title and rotulo
    plt.title(f'Variação da Selic % | Correlação: {corr:.2f}')
    plt.xlabel('Selic - Percentual %')
    plt.ylabel('Unidade de Notebooks Vendidas')

    plt.tight_layout()
    plt.show()

selic()