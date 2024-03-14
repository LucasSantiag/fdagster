from dagster import Definitions
from data.smart_cities.asset import old_asset


defs = Definitions(assets=[old_asset])
