import pandas as pd
import numpy as np


df = pd.read_excel('SEX-ED.xlsx', sheet_name='Data')
df.reset_index(inplace=True, drop=True)

for i in df['Intent']:
    q = df[df['Intent'] == i]['Questions']
    print('## intent:' + i)
    print('- '+str(q))

# print(df)