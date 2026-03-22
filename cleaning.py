import pandas as pd

# Load the orders file
orders_df = pd.read_csv('dataset/olist_orders_dataset.csv')
print(orders_df.head())

# info() prints directly to the console
print(orders_df.info())


