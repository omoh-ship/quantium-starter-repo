from dash import dcc, Dash, html
from dash.dependencies import Input, Output
import plotly.express as px
from datetime import date
import pandas as pd
import glob
import os

app = Dash(__name__)

#
# df = pd.read_csv('data/processed_sales_0.csv')
# query = df[df['Date'].between('2018-02-06', '2018-02-28')]
# print(query)


app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales Visualization'),
    html.Div(children='A visualization of the sales of the pink morsel'),
    dcc.Dropdown(id='area', options=['north', 'south', 'east', 'west'],
                 multi=True, value=['north', 'south']),

    dcc.DatePickerRange(
            id='my-date-picker',
            min_date_allowed=date(2018, 2, 6),
            max_date_allowed=date(2022, 2, 14),
            start_date=date(2021, 1, 1),
            end_date=date(2021, 2, 28),
            display_format='YYYY-MM-DD'
        ),
    dcc.Graph(id='graph', figure={})
])


@app.callback(
    Output('graph', 'figure'),
    Input('area', 'value'),
    Input('my-date-picker', 'start_date'),
    Input('my-date-picker', 'end_date'))
def update_output(area: list, start_date, end_date):
    df = pd.read_pickle('data/combined.pkl')
    area_df = df[df['Region'].isin(area)]
    query = area_df[area_df['Date'].between(start_date, end_date)]
    return px.line(query, x='Date', y='Sales($)', color='Region')


if __name__ == '__main__':
    app.run_server(debug=True)

