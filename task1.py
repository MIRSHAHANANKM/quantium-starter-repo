import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv(r'C:\Users\Lenovo\quantium-starter-repo\quantium-starter-repo\data\daily_sales_data_0.csv')

# Visualize 'product' column (replace with your column of interest)
fig = px.histogram(df, x='product', title='Product Data Visualization')

# Initialize Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1('Quantium Data Visualization Project'),
    dcc.Graph(figure=fig)
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
