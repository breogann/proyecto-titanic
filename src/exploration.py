def describir_dataset (df):
    print(f"Este df tiene estas columnas y filas: {df.shape}")
    print(df.isna().sum())