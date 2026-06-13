import pandas as pd

inventory = pd.read_csv(
    "data/inventory.csv"
)

low_stock = inventory[
    inventory["On Hand"]
    <= inventory["Minimum"]
]

order_sheet = low_stock[
    ["Serial","Item","Reorder Qty"]
]

order_sheet.to_csv(
    "docs/order_sheet.csv",
    index=False
)

order_sheet.to_json(
    "docs/orders.json",
    orient="records"
)
