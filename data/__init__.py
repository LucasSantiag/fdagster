from dagster import Definitions
from data.banking.load import load_dataset
from data.banking.asset import model


defs = Definitions(assets=[load_dataset, model])
