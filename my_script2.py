


import os
import pandas
from IPython import embed # b/c breakpoint() isn't available in 3.6

csv_filepath = os.path.join(os.path.dirname(__file__), "products.csv")
print(os.path.isfile(csv_filepath))

print("-------------")
print("READING THE CSV FILE...")
df = pandas.read_csv(csv_filepath, low_memory=True, chunksize=10)

for chunk in df:
    print("------------------------------")
    print(chunk.head())
    #print("COLUMNS...")
    #print(list(chunk.columns))
    print("DTYPES...")
    print(dict(chunk.dtypes))

    #print("INFO...")
    #print(chunk.info())
    #embed()
