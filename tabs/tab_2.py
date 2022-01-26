import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

myheading1='Enter the ID and press submit:'
initial_value='150658'
initial_value2='2'
longtext='''
        _Hint: Copy and Paste the ID Number:_
        '''

tab_2_layout = html.Div(children=[
    html.H1(myheading1),
    html.H6('Enter the Board Game ID:'),
    dcc.Input(id='my-id', value=initial_value, type='text'),
    html.H6('How Many Players:'),
    dcc.Input(id='my-id2', value=initial_value, type='text'),
    # dcc.Slider(
    #     id='my-id2',
    #     min=1,
    #     max=10,
    #     step=1,
    #     marks={i:str(i) for i in range(1, 11)},
    #     value=5,
    # ),
    html.Br(),
    html.Button('Submit', id='submit-val2', n_clicks=0),
    html.Br(),
    html.Div(id='my-div')]
)
