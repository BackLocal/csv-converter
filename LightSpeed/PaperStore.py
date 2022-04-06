import pandas as pd

# Primary feed
primary = pd.read_csv ('Downloads/item_listings_quick_edit_items.csv')
primary.columns.values
primary = primary[['UPC','Qty.', 'Manufact. SKU', 'Description', 'Price']]
primary = primary.rename(columns={"UPC":"id","Qty.":"availability", "Price" : "price", "Manufact. SKU":"gtin", "Description":"description"})
primary = primary.dropna(subset = ['gtin']).reset_index(drop=True)
primary["description"] = primary["description"].apply(lambda x: x.title())
primary["title"] = primary["description"]
primary["link"] = ""
primary["image_link"] = ""
primary.to_csv('paper_store_primary_feed.csv')

# Local feed
local = pd.read_csv('paper_store_primary_feed.csv')
del local["Unnamed: 0"]
local = local[['id', 'price']]
local["store_code"] = ""
local["quantity"] = "4"
local.to_csv('paper_store_local_feed.csv')