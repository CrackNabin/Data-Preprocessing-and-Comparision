#pip install pandas
#pip install pandas_profiling

import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_csv('mtsamples.csv')

print(df)

profile = ProfileReport(df)

profile.to_file(output_file='simulation.html')
