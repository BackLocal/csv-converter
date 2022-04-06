# csv-converter
Converts inventory .csv files to a format Google Merchant will except for local feed uploads. This includes deleting unecesasry column attributes, getting rid of null values, and renaming column attributes according to [Google standards](https://support.google.com/merchants/answer/7052112?visit_id=637841690100276276-3785271917&rd=1#zippy=) This will help make the manual process of regularly uploading client's inventory to the local product listing a little easier. Until the creation of a connection with each client's POS system through an API, you will still have to manually go to the POS system and download the inventory as a .csv file, then run this script to reformat the file, then manually go into Google Merchant Center and upload the feed as a supplemental feed to the local product lisitng.

# Installation
To create more Python scripts to run on future client's .csv inventory files, first you need to install pandas and jupyterlab by running these commands on your local machines terminal.

`pip install pandas`
`pip install jupyterlab`

Then run `jupyter-lab` to start JupyterLab in your browser. A new window will open where you can begin to edit code.

### What is JupyterLab?
JupyterLAb is a web-based interactive development environemnt. It is great to use with Python! The coolest thing about Jupyter is you can run Python scripts on a web browser, but all the code is saved on your local machine.

### What is Pandas?
It is a powerful Python library that can:
1. Read and write data between in-memory data structures and different formats: CSV files, Microsoft Excel, and SQL databases
2. Resahpe and pivote data sets
3. Slice, index, and create subsets of large data sets
4. Columns can be inserted and deleted from data structures for size mutability
5. Merge and join data sets
