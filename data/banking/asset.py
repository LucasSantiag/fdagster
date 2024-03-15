from dagster import asset, AssetExecutionContext

import numpy as np
import pandas as pd
import tensorflow as tf


@asset(group_name="Banking", compute_kind="Tensorflow")
def model(context: AssetExecutionContext, load_dataset: pd.DataFrame):
    
