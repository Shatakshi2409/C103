import pandas as pd
import plotly.express as px
df=pd.read_csv('data.csv')
print(df)
fig=px.scatter(df,x='Population',y='Per capita',color='Country',title='Per capita income',size_max=40, size='Percentage')
fig.show()