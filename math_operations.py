# Let’s start with a simple function to test:
def add(a,b):
    if a is None or b is None:
        return None
    return a + b

def subtract(a,b):
    if a is None or b is None:
        return None
    return a - b

print(add(10,10))

################# read csv file ##########################
import pandas as pd
df = pd.read_csv("data/sample.csv")
print(df.head(5))

def calculate_range(dataframe):
    dataframe['range'] = dataframe['high'] - dataframe['low']
    return dataframe

print(calculate_range(df))

