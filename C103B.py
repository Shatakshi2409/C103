import pandas as pd
import plotly.express as px
df=pd.read_csv('data.csv')
print(df)
fig=px.bar(df,x='Country',y='InternetUsers',title='Internet Users per country',color='Country')
fig.show()