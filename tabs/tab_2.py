import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

myheading1='Enter the ID and press submit:'
initial_value='150658'
longtext='''
        _Hint: Copy and Paste the ID Number:_
        '''

tab_2_layout = html.Div(children=[
    html.H1(myheading1),
    html.Div(children=[dcc.Markdown(longtext)]),
    dcc.Input(id='my-id', value=initial_value, type='text'),
    html.Button('Submit', id='submit-val2', n_clicks=0),
    html.Div(id='my-div')]
)
