# CASE - Projeto de Previsão de Demanda: Nootebooks e Variáveis Macroeconômicos
---
<img width="1895" height="1063" alt="image" src="https://github.com/user-attachments/assets/aaf22102-042e-4525-9f59-b5975f3c12cb" />

### Cenários Macroeconômicos e Projeções de Vendas (2025-2026)

| **Cenário**    | **Ano** | **PIB Real (var.%)** | **Taxa de Câmbio (R$/US$)** | **Inflação (var.%)** | **Vendas Previstas (unid.)** | **Variação vs Base** |
| -------------- | ------- | -------------------- | --------------------------- | -------------------- | ---------------------------- | -------------------- |
| **Pessimista** | 2025    | 0,52%                | 6,76                        | 7,04%                | **4.611.704**                | -23%                 |
|                | 2026    | 0,55%                | 6,79                        | 7,05%                | **4.572.342**                | -0,85%               |
| **Base**       | 2025    | 3,26%                | 5,50                        | 4,79%                | **6.299.951**                | +5%                  |
|                | 2026    | 3,30%                | 5,53                        | 4,80%                | **6.260.589**                | -0,63%               |
| **Otimista**   | 2025    | 6,01%                | 4,24                        | 2,53%                | **7.988.199**                | +33%                 |
|                | 2026    | 6,05%                | 4,27                        | 2,54%                | **7.948.837**                | -0,49%               |

### Benchmarks e Referências de Mercado (2025-2026)
| **Indicador**                               | **Ano** | **Estimativa / Valores**                                           | **Fonte / Observação**                                              |
| ------------------------------------------- | ------- | ------------------------------------------------------------------ | ------------------------------------------------------------------- |
| **Inflação anual (Brasil)**                 | 2025    | ≈ 5,10 % (mercado – *latinnews.com*)                               | Expectativa média do mercado para 2025                              |
|                                             | 2025    | ≈ 5,2 % (*IMF*)                                                    | Projeção do Fundo Monetário Internacional                           |
|                                             | 2026    | ≈ 4,45 % (mercado – *latinnews.com*)                               | Revisão para baixo na projeção do mercado                           |
|                                             | 2026    | ≈ 5,0 % (*OECD*)                                                   | Projeção da Organização para Cooperação e Desenvolvimento Econômico |
| **Taxa de câmbio (USD/BRL)**                | 2025    | ≈ 5,82 (set/2025) – *Taxas de Câmbio Reino Unido*                  | Estimativa para final de setembro de 2025                           |
|                                             | 2026    | ≈ 5,40–5,48 (meados de 2026) – *gov.capital*                       | Projeção média para meados de 2026                                  |
| **Vendas / Remessas de notebooks (global)** | 2025    | Crescimento estimado **+2,2 % YoY** (*TrendForce*)                 | Recuperação moderada do mercado global                              |
|                                             | 2026    | Crescimento estimado **CAGR ≈ 3 % (2025–2030)** (*DIGITIMES Asia*) | Tendência de crescimento sustentado                                 |

**Comparativo com modelo interno:**
| As projeções do modelo ARIMA (base e cenários) estão alinhadas com o ritmo do crescimento global (≈ 2–3 % a.a.), reforçando a coerência macroeconômica das estimativas - especialmente sob o cenário base e otimista.

---

### Sobre

Este projeto foi desenvolvido como parte de um case técnico para a posição de Analista de BI Pleto, cujo desafio era responder à seguinte pergunta:

| **"Quantos notebooks serão vendidos no Brasil em 2026?"**

Para construir a solução, optei por uma abordagem baseada em **modelagem estatística e análise de variáveis macroeconômicas,** explorando como indicadores como **PIB, inflação, câmbio e taxa Selic** impactam o volume de vendas de notebooks ao longo do tempo.
O objetivo foi aplicar técnicas de previsão de demanda (demand forecasting) e transformar dados econômicos em **insighs estratégicos e quantitativos**

---

### Metodologia
* Coleta de séries históricas (IBGE, Banco Central e fontes do setor)
* Tratamento e integração dos dados
* Análise Exploratória para identificar correlações, defasagens(lags), rupturas e quedas
* Modelagem com ARIMA (1,1,0) para previsão de vendas
* Criação de cenários econômico (base, otimista e pessimista)

---

## Estrutura Analítica do Projeto
Antes da modelagem, foi definida uma abordagem em três níveis, para explicar o porquê de cada caminho analítico e construir uma visão coerente entre economia, setor e mercado.

---

### Nível 1 - Ambiente Macroeconômico
O ponto de partida foi entender como o contexto econômico afeta o consumo de bens duráveis, como notebooks.
* PIB Real e PIB Per Capita: crescimento econômico tende a impulsionar o consumo.
* Renda Média das Famílias e Taxa de Desemprego: maior renda e menor desemprego aumentam a propensão à compra.
* Câmbio e Preços: notebooks possuem forte dependência de importação e sensibilidade ao preçodo dólar.
* População: o crescimento de jovens e profissionais economicamente ativos impulsiona a demanda.
**Objetivo:** converter o impacto econômico em demanda por eletrônicos, estimando elasticidades e avaliando cenários estratégicos (ex: crescimento econômico, choques de oferta).
  Esses indicadores funcioam como variáveis causais, expicando o comportamento do consumo de notebooks.

---

### Nível 2 - Setor de Tecnologia e Eletrônioos
Neste nível, o macroeconômico é traduzido para o setor de tecnologia de consumo - quanto o crescimento do PIB se reflete no setor.
* Gastos das Famílias com Eletrônicos: proporção do consumo total dedicada à tecnologia.
* Elasticidade-Renda Setorial: mede a resposta das vendas de notebooks ao crescimento econômico:

  | Para cada +1% no PIB, as vendas de notebooks crescem, em média, +1,5%.*

* Investimento em infaestrutura Digital: ampliação do acesso à internet e banda larga aumenta a penetração de notebooks no mercado.
  **Objetivo:** criar uma ponte entre a economia e o setor, qualidade e sensibilidade do consumo de tecnologia a variações macroeconômicas.

---

### Nível 3 - Mercado de Notebooks
Com base nos dois primeiros níveis, o modelo desce até a projeção de vendas totais de notebooks, unindo indicadores macroeconomicos e setoriais.
**Equação conceitual simplificada:**
*Vendast​=α+βi​⋅Xi​+εt​*
onde:
* α: intercepto (nível base do mercado)
* βᵢ: sensibilidade estimada de cada variável (via regressão)
* εₜ: termo de erro aleatório
Os modelos foram testados com dados anuais de 2010 a 2024, relacionando vendas reais com indicadores econômicos selecionados.

---

# Identificação de Correlações e Seleção de Vaiáveis
Para definir que variáveis macroeconômicas e setoriais seriam incluídas no modelo, utilizamos o gráfico de correlação de Pearson, avaliando a força e direção da relação entre cada indicador e as vendas de notebooks.

| Variável                                       | Correlação    | Interpretação                                                                                                                                                       |
| ---------------------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **taxa_de_cambio**                             | -0,76         | 📉 Forte correlação negativa. Quando o dólar sobe, as vendas de notebooks caem — consistente com o fato de notebooks serem produtos importados.                     |
| **pip_per_capita** / **pib_real_variacao_yoy** | -0,18 / -0,17 | 📉 Correlação leve. O PIB real tem impacto, mas não é um fator direto e forte no consumo de notebooks.                                                              |
| **inflação**                                   | -0,15          | 📈 Correlação negativa fraca. Pode refletir períodos de maior demanda, mas a relação é limitada.                                                                    |

### Interpretação do PIB vs Vendas de Notebooks
<img width="1304" height="609" alt="image" src="https://github.com/user-attachments/assets/57870dc1-7761-4fbe-bf93-8bc2019cf96d" />
<img width="1289" height="598" alt="image" src="https://github.com/user-attachments/assets/f5262b93-9a53-4dfd-ae75-9e9e106d4a13" />

O gráfico de correlação entre PIB real anual e vendas de notebooks apresentou -0,17, indicando correlação fraca e negativa.

**Observações**
* Quando o PIB cresce, as vendas de notebooks tendem a cair levemente, mas a relação é muito fraca.
* Na prática, não há evidência de uma relação linear consistente entre crescimento econômico e vendas de notebooks.

**Contextualização**
Apesar do PIB ser um indicador macroeconômico relevante, o consumo de notebooks depende mais de fatores microeconômicos e tecnológicos, como:
 * Troca de equipamentos pelas empresas
 * Novos lançamentos e estratégias de preço
 * Impactos de eventos extraordinários (ex: pandemia e home office)
 * Programas de incentivo governamentais
   
 **Conclusão:** O PIB sozinho não explica bem o comportamento das vendas de notebooks, sendo necessário incluir outras variáveis para capturar os efeitos reais sobre o mercado.

### Interpretação de Taxa de Câmbio vs Vendas de Notebooks
<img width="1296" height="620" alt="image" src="https://github.com/user-attachments/assets/52f7c96b-14c0-414f-94b0-f471ad1fc11d" />

O gráfico de correlação entre taxa de câmbio (R$/USD) e vendas de notebooks apresentou -0,76, indicando forte correlação negativa
* Interpretação Econômica
A relação observada faz total sentido do ponto de vista econômico:
1. Notebooks são produtos importados
* Mesmo os montados no Brasil dependem de componentes importados (placas, chips, telas).
* Quando o dólar sobe, o custo de importação aumenta, elevando o preço final no varejo.
2. Aumento de preços -> queda na demanda
* Com o produto mais caro, as vendas caem, especialmente em períodos de menor poder de compra
3. Efeito macroeconômico combinado
Altos valores do câmbio costumam vir acompanhados de:
* Inflação de eletrônicos
* Taxas de juros mais altas
* Redução do consumo das famílias
Tudo isso reforça a queda nas vendas notebooks

* Observação dos Dados Históricos
  
| Ano       | Câmbio (R$) | Vendas de Notebooks | Observação                                         |
| --------- | ----------- | ------------------- | -------------------------------------------------- |
| 2012–2014 | 1,95 → 2,35 | Ainda boas          | Subida leve no câmbio, vendas ainda fortes         |
| 2015–2016 | 3,33 → 3,49 | Caem                | Câmbio dispara, vendas começam a cair              |
| 2020–2024 | 5,15 → 5,39 | Muito baixas        | Câmbio alto e sustentado, impacto forte nas vendas |

* Conclusão
  A taxa de câmbio é, até agora, o fator macroeconômico mais relevante para explicar a demanda por notebooks.
  Correlação -0,76 confirma relação linear forte e negativa.
  O comportamento é econômica e empiricamente consistente, indicando que o câmbio é um dos principais drivers de elasticidade de preço do setor.

---

### Leitura Análitica das Séries Temporais Macroeconômicas

<img width="1600" height="979" alt="image" src="https://github.com/user-attachments/assets/2b873286-eaed-4da5-8bdb-0df30963a968" />
<img width="1544" height="840" alt="image" src="https://github.com/user-attachments/assets/2acf3776-7c59-4f06-b360-c5dd6213eece" />

### Avaliação de Modelo - Taxa de Câmbio vc Vendas de Notebooks
Após identificar a forte correlação negativa (-0,76) entre o câmbio e as vendas de notebooks, foi ajustado um modelo univariado de previsão, utilizando a taxa de câmbio como variável explicativa principal

---

<img width="1600" height="867" alt="image" src="https://github.com/user-attachments/assets/b78b2850-3cc8-4b12-b7a9-78c7fd24bc16" />

**Desempenho do Modelo**

| Métrica                                  | Valor                         | Interpretação                                                                                                                                                                                 |
| ---------------------------------------- | ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **R² Ajustado**                          | **0,542**                     | O modelo explica cerca de **54% da variação nas vendas de notebooks**. Considerando o tamanho reduzido da amostra e o uso de apenas uma variável, esse resultado é satisfatório.              |
| **MAE (Erro Absoluto Médio)**            | **≈ 1,03 milhão de unidades** | Em média, o modelo erra em aproximadamente **1 milhão de unidades** vendidas. Exemplo: se o valor real foi 10 milhões, a previsão tenderia a ficar entre 9 e 11 milhões.                      |
| **RMSE (Raiz do Erro Quadrático Médio)** | **≈ 1,38 milhão de unidades** | Indica que há alguns anos com **erros mais altos**, já que o RMSE penaliza desvios grandes. Ainda assim, está na mesma ordem de grandeza do MAE, sugerindo ausência de **outliers extremos**. |

**Resumo da Regressão Linear (OLS)**
| Métrica                           |              Valor |
| :-------------------------------- | -----------------: |
| **Variável Dependente**           | unidades_notebooks |
| **Método**                        |      Least Squares |
| **R²**                            |              0.581 |
| **R² Ajustado**                   |              0.542 |
| **Estatística F**                 |              15.23 |
| **Prob (F-statistic)**            |            0.00247 |
| **Número de Observações**         |                 13 |
| **Graus de Liberdade (Modelo)**   |                  1 |
| **Graus de Liberdade (Resíduos)** |                 11 |
| **Log-Likelihood**                |            -202.22 |
| **AIC**                           |              408.4 |
| **BIC**                           |              409.6 |
| **Covariance Type**               |          nonrobust |

**Diagnósticos Estatísticos**
| Teste                | Valor |
| :------------------- | ----: |
| **Omnibus**          | 6.987 |
| **Prob (Omnibus)**   | 0.030 |
| **Jarque-Bera (JB)** | 3.284 |
| **Prob (JB)**        | 0.194 |
| **Skew**             | 1.050 |
| **Kurtosis**         | 4.288 |
| **Durbin-Watson**    | 2.292 |
| **Cond. No.**        |  14.3 |

Coeficientes do Modelo

|Variável|Coeficiente|Erro Padrão|t|P>t|IC 95% Inferior|IC 95% Superior|
|--------|-----------|-----------|-|---|---------------|---------------|
|const| 13.660.000|1.339.000|9.84|0.000|10.600.000|16.700.000|
|taxa_de_cambio|-1.339.000|343.000|-3.90|0.002|-2.090.000|-584.000|


### Análise dos Resíduos - Modelo com Taxa de Câmbio
Após o ajuste do modelo, foi analisada a distribuição dos resíduos (diferença entre valores reais e previstos) para avaliar a qualidade do ajuste e possíveis vieses.

<img width="1836" height="996" alt="image" src="https://github.com/user-attachments/assets/3c37cd38-1967-40d4-99f7-e9aaca9a9560" />

**Resíduos vs Valores Previstos**

O gráfico Résiduos vs Previsto apresentou o seguinte comportamento:
* Distribuição aleatória em torno de 0:
  Sinal de que o modelo capturou bem a tendência central das vendas
* Amplitude dos resíduos entre -1 e +1 milhão:
  Os erros são pequenos e consistentes, indicando previsões estáveis
* Apenas dos pontos fora do padrão:
  Anos atípicos, choque econômico e pandemia)
* Durbin-Watson:
  Resultado indica ausência de autocorrelação, reforçando que os erros não estão correlacionados no tempo.

### Análise de Sensibilidade - Impacto da Taxa de Câmbio
Para entender o quanto as variações do dólar afetam as vendas de notebooks, foi feita uma análise de sensibilidade a partir do coneficiente do modelo linear.

<img width="1856" height="1016" alt="image" src="https://github.com/user-attachments/assets/aaf3b1e9-071a-4c95-8c47-228b1b089877" />

* **Resultado**
  **Para cada aumento de R$ 1,00 na taxa de câmbio**, as vendas de notebooks diminuem, em média, 1,36 milhão de unidades.

Essa elasticidade negativa reforça a forte dependência do setor de tecnologia ao câmbio, já que notebooks são produtos com alto conteúdo importado.

---

### Projeções das Variáveis Macroeconômicas

**PIB Real (YoY) & Intervalo de Confiança em 95%**
<img width="2280" height="1248" alt="image" src="https://github.com/user-attachments/assets/49a1cb14-a80e-4d5e-bdd4-617dd39f2e10" />
<img width="2324" height="1476" alt="image" src="https://github.com/user-attachments/assets/639270fc-1076-489a-b932-2f6fb0d9743f" />

---

**Taxa de Câmbio  & Intervalo de Confiança em 95%**
<img width="2384" height="1264" alt="image" src="https://github.com/user-attachments/assets/28db5035-baaa-4f20-94ee-5437227f7a8f" />
<img width="2244" height="1504" alt="image" src="https://github.com/user-attachments/assets/7315a3e2-e6b5-4fde-b48d-95ae03311f72" />

---

**Inflação & Intervalo de Confiança em 95%**
<img width="2288" height="1256" alt="image" src="https://github.com/user-attachments/assets/8548d563-e6ab-42f5-8251-f89cdaaf386c" />
<img width="2372" height="1508" alt="image" src="https://github.com/user-attachments/assets/04893bff-fd3b-4df1-901b-20e7dff83f09" />




