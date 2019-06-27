

import os
import pandas

csv_filepath = os.path.join(os.path.dirname(__file__), "data", "products.csv")
print(os.path.isfile(csv_filepath))

df = pandas.read_csv(csv_filepath)
print(type(df))
print(df.head())
