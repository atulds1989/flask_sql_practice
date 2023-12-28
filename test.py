import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
new_row = pd.Series({'A': 7, 'B': 8})

print(df)

df = df.append(new_row, ignore_index=True) 
print(df)
