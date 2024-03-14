from dagster import asset


@asset
def old_asset():
    print("oi")
