import pandas as pd

df = pd.read_json('../static/election21.json')

# print(df.shape)

print(df.to_json())