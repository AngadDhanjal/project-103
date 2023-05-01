import pandas as pd 
import plotly.express as px 
df = pd.read_csv("Covid.csv")

fig = px.line(df, x = "Date", y = "Cases", color = "Country")
fig.show()