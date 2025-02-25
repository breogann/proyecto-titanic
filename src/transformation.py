import pandas as pd

def transformar_edad_sexo (df):
    df["age_group"] = pd.cut(df["age"],
                            bins=[0, 12, 18, 35, 60, 100],
                            labels=["Kid", "Teenager", "otra cosa", "otra más", "el último"])
    df["sex_num"] = df["sex"].map({"male": 0, "female":1})
    return df

def limpieza_df (df):
    df.drop(["deck",	"embark_town"], axis=1, inplace=True)
    return df

def fill_na_age (df):
    df["age_new"] = df["age"].fillna(df["age"].mean())
    return df