import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

import src.exploration as exp
import src.transformation as trs
import src.visualization as viz

if __name__ == "__main__":
    df = sns.load_dataset("titanic")
    exp.describir_dataset (df)

    df_1 = trs.transformar_edad_sexo (df)
    df_2 = trs.limpieza_df (df_1)
    df_3 = trs.fill_na_age (df_2)

    viz.histograma_edad (df_3)
    viz.survival_plot (df_3)

    df_3.to_csv("data/mi_primerito_pipeline.csv", index=False)