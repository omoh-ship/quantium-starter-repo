from dash import dcc, Dash, html
from dash.dependencies import Input, Output
from plotly.express import line
from datetime import date
import pandas as pd


def create_visualisation(data_frame):
    line_plot = line(data_frame, x='Date', y='Sales($)', color='Region')
    line_plot.update_layout(
        plot_bgcolor=COLORS['background'],
        paper_bgcolor=COLORS['miscellaneous'],
        font_color=COLORS['text']
    )
    return line_plot


COLORS = {
    'background': "#171717",
    'miscellaneous': "#444444",
    'text': "#EDEDED",
}


external_stylesheets = [
    {
        "rel": "stylesheet",
    },
]

app = Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Pinky"

header = html.H1(children='Pink Morsel Sales Visualization',
                 className='header')
description = html.Div(children='A visualization of the sales of the pink morsel',
                       className='description')
radio_options = dcc.RadioItems(id='region', options=['north', 'south', 'east', 'west', 'all'], value='all',
                               className='radio')
date_range = dcc.DatePickerRange(
            id='my-date-picker',
            min_date_allowed=date(2018, 2, 6),
            max_date_allowed=date(2022, 2, 14),
            start_date=date(2021, 1, 1),
            end_date=date(2021, 2, 28),
            display_format='YYYY-MM-DD')

graph = dcc.Graph(id='graph', figure={})

app.layout = html.Div(style={'backgroundColor': COLORS['background']}, children=[
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
    return create_visualisation(date_query)


if __name__ == '__main__':
    app.run_server(debug=True)

