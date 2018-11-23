# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_table as dt

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df = pd.read_csv('world-university-rankings/timesData.csv')
time_df = df.iloc[:100, :]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash Sample: World University Ranking.
    '''),
    dt.DataTable(
        id='table',
        columns=[{'name': i, 'id': i} for i in df.columns],
        data=time_df.to_dict('rows'),
        n_fixed_rows=1,
        filtering=True,
        sorting=True,
        sorting_type='multi',
        style_table={
            'overflowX': 'scroll',
            'maxHeight': '500',
            'overflowY': 'scroll'
            },
        style_header={
            'backgroundColor': 'white',
            'fontWeight': 'bold'
        }
    ),
    dcc.Graph(
        id='work-ranking',
        figure={
            'data': [
                {'x': time_df.world_rank, 'y': time_df.citations, 'type': 'lines', 'name': 'citations', 'text': time_df.university_name},
                {'x': time_df.world_rank, 'y': time_df.teaching, 'type': 'lines+markers', 'name': 'teaching', 'text': time_df.university_name},
            ],
            'layout': {
                'title': 'World Ranking'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)