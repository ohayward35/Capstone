import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from tabs import tab_1
from tabs import tab_2
from dash.dependencies import Input, Output, State
from collections import deque, Counter
import requests
import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np

########### Define your variables ######
myheading1 = '🎲 Buy the Perfect Game 🎲'
tabtitle = 'boardgame'
sourceurl = 'https://www.grammarly.com/blog/16-surprisingly-funny-palindromes/'
githublink = 'XXXX'
image='image2.png'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle
app.config['suppress_callback_exceptions'] = True


########### Set up the layout

app.layout = html.Div([
    html.H1(myheading1, style={'text-align':'center'}),
    html.Img(src=app.get_asset_url(image), style={'width': 'auto', 'height': '50%'}),
    dcc.Tabs(id="tabs-example", value='tab-1-example',
            children=[
                dcc.Tab(label="Find Your Perfect Game's ID", value='tab-1-example'),
                dcc.Tab(label="Is it a Match?", value='tab-2-example'),
    ]),
    html.Div([
        html.Div(id='tabs-content-example'),
    ], className='twelve columns',
        style={'marginBottom': 50, 'marginTop': 25}),
    html.Div([
        html.A('Code on Github', href=githublink),
        html.Br(),
        html.A("Data Source", href=sourceurl),
    ], className='twelve columns',
        style={'textAlign':'right',
                'fontColor':'#58488c',
                'backgroundColor':'#D3D3D3',})
])

@app.callback(Output('tabs-content-example', 'children'),
              [Input('tabs-example', 'value')])
def render_content(tab):
    if tab == 'tab-1-example':
        return tab_1.tab_1_layout
    elif tab == 'tab-2-example':
        return tab_2.tab_2_layout

#tab 1 callback

@app.callback(
    Output('figure-1', 'figure'),
    Input('submit-val', 'n_clicks'),
    State('input-on-submit', 'value')
)
def update_output(n_clicks, value):
    if n_clicks==0:
        return base_fig()
    else:
        return scrape_bbg(value)

def scrape_bbg(value):
    game_id_list = []
    game_title_list = []
    game_year_list = []
    search = str(value)
    r = requests.get('https://api.geekdo.com/xmlapi2/search?query='+ search.lower()+ '&type=boardgame')
    root = ET.fromstring(r.content)

    while root.attrib['total'] == "0":
        return error_fig()
        r = requests.get('https://api.geekdo.com/xmlapi2/search?query='+ search.lower()+ '&type=boardgame')
        root = ET.fromstring(r.content)
    else:
        for title in root.iter('name'):
            game_title_list.append(title.attrib['value'])
        for ident in root.iter('item'):
            game_id_list.append(ident.attrib['id'])
    games_df = pd.DataFrame({"Title":game_title_list, "ID":game_id_list})
    data=go.Table(columnwidth = [200,200],
                    header=dict(values=games_df.columns, align=['left']),
                    cells=dict(align=['left'],
                               values=games_df.T.values)
                 )
    fig = go.Figure([data])
    return fig

def base_fig():
    data=go.Table(columnwidth = [200,200],
                    header=dict(values=['Title', 'ID'], align=['left']),
                    cells=dict(align=['left'],
                               values=[['waiting for data'],[1]])
                 )
    fig = go.Figure([data])
    return fig
def error_fig():
    data=go.Table(columnwidth = [200,200],
                    header=dict(values=['Title', 'ID'], align=['left']),
                    cells=dict(align=['left'],
                               values=[['No Results Found'],
                                       ['No Results Found']])
                 )
    fig = go.Figure([data])
    return fig

# tab 2 callback

def id_players(value):
    search = str(value)
    r = requests.get('https://api.geekdo.com/xmlapi2/thing?id='+ search.lower()+ '&marketplace=1')
    root = ET.fromstring(r.content)
    description = root[0][8].text
    return description

def my_function(value):
    search = str(value)
    r = requests.get('https://api.geekdo.com/xmlapi2/thing?id='+ search.lower()+ '&marketplace=1')
    root = ET.fromstring(r.content)
    #return "Description: " + root[0][8].text
    return "This game can be played with between " + root[0][10].attrib['value'] + " and " + root[0][11].attrib['value'] + " players!"

@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='submit-val2', component_property='n_clicks')],
    State('my-id', 'value')
)

def update_output_div(n_clicks,input_value):
    if n_clicks == 0:
        return "Waiting for Input"
    else:
        search = str(input_value)
        r = requests.get('https://api.geekdo.com/xmlapi2/thing?id='+ search.lower()+ '&marketplace=1')
        root = ET.fromstring(r.content)
        return "This game can be played with between " + root[0][10].attrib['value'] + " and " + root[0][11].attrib['value'] + " players!"
        return root[0][8].text



############ Deploy
if __name__ == '__main__':
    app.run_server(debug=True)
