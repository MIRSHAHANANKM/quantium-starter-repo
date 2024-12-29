import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

df1 = pd.read_csv(r'C:\Users\Lenovo\quantium-starter-repo\data\daily_sales_data_0.csv')
df2 = pd.read_csv(r'C:\Users\Lenovo\quantium-starter-repo\data\daily_sales_data_1.csv')
df3 = pd.read_csv(r'C:\Users\Lenovo\quantium-starter-repo\data\daily_sales_data_2.csv')
df = pd.concat([df1, df2, df3])

app = dash.Dash(__name__)

fig = px.histogram(df, x='product', title='sample data visualization')
app.layout = html.Div([
    html.H1('Data preparation and customer analytics'),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)