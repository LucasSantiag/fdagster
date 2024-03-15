from dagster import asset, AssetExecutionContext

import zipfile
import pandas as pd


@asset(group_name="Banking", compute_kind="Pandas")
def load_dataset(context: AssetExecutionContext):
    with zipfile.ZipFile(
        "dataset/Machine+Learning+A-Z+(Codes+and+Datasets).zip", "r"
    ) as zip_ref:
        zip_ref.extractall("output")

    df = pd.read_csv(
        "output/Machine Learning A-Z (Codes and Datasets)/Part 8 - Deep Learning/Section 39 - Artificial Neural Networks (ANN)/Python/Churn_Modelling.csv"
    )

    context.log.info(df.head())

    return df
