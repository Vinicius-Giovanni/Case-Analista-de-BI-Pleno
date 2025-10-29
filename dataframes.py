import pandas as pd
import numpy as np
from pathlib import Path

"""
EDA - Explory Data Analysis (Análise Exploratória de Dados)
Etapa de investigação, compreensão e visualização dos dados antes de aplicar em modelos prediivos
"""

def creating_dataframe(cols: list ) -> pd.DataFrame:
    
    data_path = Path("C:/Users/2960006959/Desktop/project/Case-Analista-de-BI-Pleno/database/case_analista_de_bi_pleno.xlsx")

    df = pd.read_excel(
        data_path,
        usecols=cols
        )
    
    print(df.info())
    print(50*"-")
    print(df.head(100))

    return df
