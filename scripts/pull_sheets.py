import gspread
import pandas as pd
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets.readonly"
]

creds = Credentials.from_service_account_file(
    "service_account.json",
    scopes=SCOPES
)

gc = gspread.authorize(creds)

sheet = gc.open("ConcessionInventory")

inventory = sheet.worksheet("Inventory")
orders = sheet.worksheet("Orders")

pd.DataFrame(
    inventory.get_all_records()
).to_csv(
    "data/inventory.csv",
    index=False
)

pd.DataFrame(
    orders.get_all_records()
).to_csv(
    "data/orders.csv",
    index=False
)
