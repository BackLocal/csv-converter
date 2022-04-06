import pandas as pd
import regex as re

# Primary feed
primary = pd.read_csv ('Downloads/9353-edit-products.csv')
primary.columns.values
primary = primary[['Internal ID(Do Not Change)', 'Product Title', 'Availability(web/store/both)','sku', 'Manufacturer Product Id', 'Price']]
primary = primary.rename(columns={"Internal ID(Do Not Change)": "id", "Product Title" : "title", "Availability(web/store/both)":"availability", "Price" : "price", "Manufacturer Product Id":"gtin"})

# Clones 'title' information into a new 'description column'
primary['description'] = primary['title']

# Creates emtpy columns for link and image_link urls
primary['link'] = ''
primary['image_link'] = ''

# Gets rid of = and "" for the 'id', 'sku', and 'gtin' columns
primary['id']=primary['id'].apply(lambda x: re.sub(r'=*"','', x))
primary['sku']=primary['sku'].apply(lambda x: re.sub(r'=*"','', x))
primary['gtin']=primary['gtin'].apply(lambda x: re.sub(r'=*"','', x))

primary['availability'] = ['yes' if (x=='both' or x=='store') else 'no' for x in primary['availability']]
primary.to_csv('mending_shed_primary_feed.csv')

# If you want to search if there are other products listed that are only avaible online use this command:
# primary[(primary['availability']!='both') & (primary['availability']!='store')]

# Local feed
local = pd.read_csv('mending_shed_primary_feed.csv')
del local["Unnamed: 0"]
local = local[['id', 'price']]
local["store_code"] = ""
local["quantity"] = "4"
local.to_csv('paper_store_local_feed.csv')