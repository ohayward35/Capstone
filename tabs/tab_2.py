import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

myheading1='Enter the ID and Select Players:'
initial_value='150658'
initial_value2='2'

tab_2_layout = html.Div(children=[
    html.Div([
        html.Div([
            html.H6('Enter the Board Game ID:'),
            dcc.Input(id='my-id', value=initial_value, type='text'),
            html.H6('How Many Players:'),
            dcc.Slider(
                id='my-id2',
                min=1,
                max=10,
                step=1,
                marks={i:str(i) for i in range(1, 11)},
                value=5,
            ),
            html.Br(),
            html.Button('Submit', id='submit-val2', n_clicks=0)
        ],className='three columns'),
    html.Div([
        html.Div(id='my-div'),
        ],className='nine columns'),
    ],className='twelve columns'),
    ]
)
