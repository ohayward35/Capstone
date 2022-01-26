import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

list_of_options=['God Emperor of Dune', 'The Foundryside', 'Network Effect']
list_of_images=['GEoD.jfif', 'Foundryside.jpg', 'NetworkEffect.jpg']

tab_1_layout = html.Div([
    html.H1(id='container-button-basic',
             children='Enter a keyword and press submit:'),
    html.Div(dcc.Input(id='input-on-submit', type='text')),
    html.Br(),
    html.Button('Submit', id='submit-val', n_clicks=0),
    dcc.Graph(id='figure-1')
    ])
