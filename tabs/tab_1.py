import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

tab_1_layout = html.Div(children=[
    html.Div([
        html.Div([
            html.H1(id='container-button-basic',children='Search for a Board Game:'),
            html.Div(dcc.Input(id='input-on-submit', type='text')),
            html.Br(),
            html.Button('Submit', id='submit-val', n_clicks=0)
        ],className='three columns'),
    html.Div([
        dcc.Graph(id='figure-1')
        ],className='nine columns'),
    ],className='twelve columns'),
    ]
)
