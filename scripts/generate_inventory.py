import pandas as pd

inventory = pd.read_csv(
    "data/inventory.csv"
)

inventory.to_json(
    "docs/inventory.json",
    orient="records"
)
