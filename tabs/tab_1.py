import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

list_of_options=['God Emperor of Dune', 'The Foundryside', 'Network Effect']
list_of_images=['GEoD.jfif', 'Foundryside.jpg', 'NetworkEffect.jpg']

tab_1_layout = html.Div([
    html.H1('Science Fiction Corner'),
    html.Div([
        html.Div([
            html.H6('Select a Book'),
            dcc.Dropdown(
                id='page-1-dropdown',
                options=[
                {'label':list_of_options[0], 'value':list_of_images[0]},
                {'label':list_of_options[1], 'value':list_of_images[1]},
                {'label':list_of_options[2], 'value':list_of_images[2]}
                ],
        value=list_of_images[0],
                style = dict(
                            width = '70%',
                            display = 'inline-block',
                            verticalAlign = "middle"
                            ),
            ),
        ], className='four columns'),
        html.Div([
            html.H6(id='page-1-content')
        ], className='eight columns'),
    ], className='twelve columns'),
], className='twelve columns')
