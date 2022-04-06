import pandas as pd

# Primary feed
df = pd.read_csv('Downloads/10223-edit-products.csv')
df.columns.values
df = df[['Internal ID(Do Not Change)', 'Product Title', 'Price','Availability(web/store/both)', 'upc']]
df = df.dropna(subset = ['Product Title']).reset_index(drop=True)
df = df.dropna(subset = ['upc']).reset_index(drop=True)
df = df.rename(columns={"Product Title" : "title", "Internal ID(Do Not Change)" : "id", "Price" : "price", "upc":"gtin", "Availability(web/store/both)":"availability"})
df['availability'] = ['yes' if (x=='both' or x=='store') else 'no' for x in primary['availability']]
df["title"] = df["title"].apply(lambda x: x.title())
df['description'] = df['title']
df['link'] = ''
df['image_link'] = ''
df.to_csv('heindselmans_primary_feed.csv')

# Local feed
local = pd.read_csv('heindselmans_primary_feed.csv')
del local["Unnamed: 0"]
local = local[['id', 'price']]
local["store_code"] = ""
local["quantity"] = "4"
local.to_csv('heindselmans_local_feed.csv')