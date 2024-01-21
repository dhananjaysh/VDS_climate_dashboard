# Install necessary libraries

import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Load the Dataset
df = pd.read_csv('climate_change_data.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div([
    html.H1("Climate Change Data Dashboard"),

    # Visualization 1: Line chart for Temperature over time
    dcc.Graph(id='temperature-line-chart'),

    # Visualization 2: Scatter plot for CO2 Emissions vs Temperature
    dcc.Graph(id='co2-temperature-scatter'),

    # Visualization 3: Bar chart for Average Precipitation by Location
    dcc.Graph(id='precipitation-bar-chart'),

    # Visualization 4: Box plot for Humidity
    dcc.Graph(id='humidity-box-plot'),
])

# Define callback functions to update charts based on user interactions
@app.callback(
    Output('temperature-line-chart', 'figure'),
    Input('location-dropdown', 'value')
)
def update_temperature_line_chart(selected_location):
    filtered_df = df[df['Location'] == selected_location]
    fig = px.line(filtered_df, x='Date', y='Temperature', title=f'Temperature Trends for {selected_location}')
    return fig

@app.callback(
    Output('co2-temperature-scatter', 'figure'),
    Input('location-dropdown', 'value')
)
def update_co2_temperature_scatter(selected_location):
    filtered_df = df[df['Location'] == selected_location]
    fig = px.scatter(filtered_df, x='CO2 Emissions', y='Temperature', color='Location',
                     title=f'CO2 Emissions vs Temperature for {selected_location}')
    return fig

@app.callback(
    Output('precipitation-bar-chart', 'figure'),
    Input('location-dropdown', 'value')
)
def update_precipitation_bar_chart(selected_location):
    filtered_df = df[df['Location'] == selected_location]
    fig = px.bar(filtered_df, x='Location', y='Precipitation', title=f'Average Precipitation for {selected_location}')
    return fig

@app.callback(
    Output('humidity-box-plot', 'figure'),
    Input('location-dropdown', 'value')
)
def update_humidity_box_plot(selected_location):
    filtered_df = df[df['Location'] == selected_location]
    fig = px.box(filtered_df, x='Location', y='Humidity', title=f'Humidity Distribution for {selected_location}')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
