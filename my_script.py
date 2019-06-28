


import os
import pandas
from IPython import embed # b/c breakpoint() isn't available in 3.6

csv_filepath = os.path.join(os.path.dirname(__file__), "products.csv")
print(os.path.isfile(csv_filepath))

print("-------------")
print("READING THE CSV FILE...")
df = pandas.read_csv(csv_filepath, low_memory=True, chunksize=10)
#print(type(df))
#print(df.head())
#print(df.columns)

#print("-------------")
#print("LOOPING THROUGH COLUMNS...")
#for col in df.columns:
#    print(col)
#
#print("-------------")
#print("DESCRIBE COLUMNS...")
#print(df.describe())

#chunk = list(df)[0]
#print(chunk.head())
#print(chunk.dtypes)









for chunk in df:
    print("------------------------------")
    print(chunk.head())
    #print("COLUMNS...")
    #print(list(chunk.columns))
    print("DTYPES...")
    print(dict(chunk.dtypes))

    #print("INFO...")
    #print(chunk.info())
    embed()

exit()






print("-------------")
print("FILTER COLUMNS...")

slim_df = df.filter(items=["id", "name", "price"])
print(slim_df.head())
print("COLUMNS:", slim_df.columns)
print("DATATYPES:")
print(slim_df.dtypes)


out_filepath = os.path.join(os.path.dirname(__file__), "slim_products.csv")

slim_df.to_csv(out_filepath)


#embed()

#breakpoint()
