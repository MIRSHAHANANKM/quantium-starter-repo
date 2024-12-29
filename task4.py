import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
# Load data
data = pd.read_csv(r'C:\Users\Lenovo\quantium-starter-repo\data\daily_sales_data_0.csv',r'C:\Users\Lenovo\quantium-starter-repo\data\daily_sales_data_1.csv',r'C:\Users\Lenovo\quantium-starter-repo\data\daily_sales_data_2.csv')

# Ensure the 'date' column is in datetime format
data['date'] = pd.to_datetime(data['date'])

# Sort by date
data = data.sort_values(by='date')
# Initialize Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div([
    # Header
    html.H1("Region-Specific Sales Analysis", style={'textAlign': 'center', 'color': '#4CAF50'}),

    # Radio buttons for region selection
    html.Div([
        html.Label("Select a Region:", style={'fontSize': '18px'}),
        dcc.RadioItems(
    id='region-filter',
    options=[
        {'label': 'North', 'value': 'north'},
        {'label': 'East', 'value': 'east'},
        {'label': 'South', 'value': 'south'},
        {'label': 'West', 'value': 'west'},
        {'label': 'All', 'value': 'all'}
    ],
        value='all',
            style={'marginBottom': '20px'}
        )
    ], style={'width': '50%', 'margin': '0 auto', 'textAlign': 'center'}),

    # Line chart
    dcc.Graph(id='region-sales-line-chart'),

    # Footer
    html.Div("Filter sales by region to understand trends in Pink Morsel sales.",
             style={'textAlign': 'center', 'marginTop': '20px', 'color': '#555'})
], style={'fontFamily': 'Arial, sans-serif', 'backgroundColor': '#f9f9f9', 'padding': '20px'})
@app.callback(
    Output('region-sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_chart(selected_region):
    # Filter data based on selected region
    filtered_data = data if selected_region == 'all' else data[data['region'] == selected_region]

    # Create line chart
    fig = px.line(filtered_data, x='date', y='sales', title=f"Sales Trends for Region: {selected_region.capitalize()}",
                  labels={'date': 'Date', 'sales': 'Sales ($)'})
    
    fig.update_layout(
        title={'x': 0.5, 'xanchor': 'center', 'yanchor': 'top', 'font': {'size': 24}},
        plot_bgcolor='#ffffff',
        paper_bgcolor='#f9f9f9',
        font=dict(color='#333'),
        xaxis=dict(showgrid=True, gridcolor='lightgray'),
        yaxis=dict(showgrid=True, gridcolor='lightgray')
    )
    return fig
if __name__ == '__main__':
    app.run_server(debug=True)
