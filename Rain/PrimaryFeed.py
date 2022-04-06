import pandas as pd

df = pd.read_csv('Downloads/10223-edit-products (2).csv')

df.columns.values
df[['Product Title','Short Description', 'Availability(web/store/both)','upc', 'Price', 'Options','Assigned option values','Manufacturer']]

df = df.dropna(subset = ['Product Title']).reset_index(drop=True)


df = df.rename(columns={"Product Title" : "title", "upc" : "id", "Price" : "price"})

df["title"] = df["title"].apply(lambda x: x.title())

df.to_csv('test.csv')

# run jupyter-lab to start in browser