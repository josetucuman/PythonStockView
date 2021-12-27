# Dash Framework - stock price visualization Demo

import pandas_datareader.data as web 
import dash
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Input, Output
import datetime



# Build Layout 
app = dash.Dash()

app.title = "Stock VIsualizations"

app.layout = html.Div(children=[
        html.H1('Stock Visualization Dashboard'),
        html.H4('Please enter stock name')
        dcc.Input(id="input", value='', type="text")
])
