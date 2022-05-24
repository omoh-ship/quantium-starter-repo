from dash import dcc, Dash, html
from dash.dependencies import Input, Output
from plotly.express import line
from datetime import date
import pandas as pd

app = Dash(__name__)


colors = {
    'background': "#D9FAFF",
    'text': "#00204A",
}

header = html.H1(children='Pink Morsel Sales Visualization', style={
                'textAlign': 'center',
                'color': colors['text']
            })
description = html.Div(children='A visualization of the sales of the pink morsel', style={
                    'textAlign': 'center',
                    'color': colors['text']
                })
radio_options = dcc.RadioItems(id='region', options=['north', 'south', 'east', 'west', 'all'], value='all',
                               style={'color': colors['text']})
date_range = dcc.DatePickerRange(
            id='my-date-picker',
            min_date_allowed=date(2018, 2, 6),
            max_date_allowed=date(2022, 2, 14),
            start_date=date(2021, 1, 1),
            end_date=date(2021, 2, 28),
            display_format='YYYY-MM-DD')
graph = dcc.Graph(id='graph', figure={})

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    header,
    description,
    radio_options,
    date_range,
    graph
])


@app.callback(
    Output('graph', 'figure'),
    Input('region', 'value'),
    Input('my-date-picker', 'start_date'),
    Input('my-date-picker', 'end_date'))
def update_output(region, start_date, end_date):
    df = pd.read_pickle('data/combined.pkl')
    if region != 'all':
        area_df = df[df['Region'] == region]
    else:
        area_df = df
    date_query = area_df[area_df['Date'].between(start_date, end_date)]
    return line(date_query, x='Date', y='Sales($)', color='Region')


if __name__ == '__main__':
    app.run_server(debug=True)

