import pandas as pd
df_rain = pd.read_csv("Covid 19.csv")
x=df_rain[df_rain.New_deaths==510]
print(x)
