import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

# Read the formatted sales data
data = pd.read_csv(r'C:\Users\Lenovo\quantium-starter-repo\data\formatted_sales_data.csv')

app = Dash(__name__)

price_increase_date = '2021-01-15'

def update_chart(_):
    fig = px.line(data, x='date', y='sales', title="Sales Over Time",
                  labels={'date': 'Date', 'sales': 'Sales ($)'})

    # Add a vertical line to indicate the price increase date
    fig.add_vline(x=price_increase_date, line_width=2, line_dash="dash", line_color="red")

    # Annotate the vertical line
    fig.add_annotation(
        x=price_increase_date, y=max(data['sales']),
        text="Price Increase", showarrow=True, arrowhead=2
    )

    return fig

app.layout = html.Div([
    html.H1('Sales Data Visualization'),
    dcc.Graph(id='sales-chart', figure=update_chart(None))
])

if __name__ == '__main__':
    app.run_server(debug=True)