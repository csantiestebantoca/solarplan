import pandas as pd
from os.path import dirname, join
import plotly.express as px
import plotly.graph_objs as go
import numpy as np


# ---- Data ----
def load_data(filename):
    data = pd.read_csv(filename)
    #data['Startup Time'] = pd.to_datetime(data['Startup Time'])
    #data['Shutdown Time'] = pd.to_datetime(data['Shutdown Time'])

    cols = data.columns.tolist()
    dictionary = {}
    for elem in cols:
        dictionary[elem] = data[elem]

    dates = []  # ['Startup Time', 'Shutdown Time']
    features = [e for e in dictionary if (e not in dates)]

    return data, dates, features


filename1 = join(dirname(__file__), 'StartupShutdown.csv')
df, dates, features = load_data(filename1)


def index():
    response.flash = T("Shutdown and Startup")
    res_Dict = dict(message="Shutdown and Startup")
    res_Dict.update(bar1())
    res_Dict.update(bar2())
    return res_Dict


def bar1():
    values = df['Startup Time'].value_counts()
    data = [go.Bar(x=list(values.index),
                   y=list(values.values),
                   opacity=0.8,
                   width=np.ones(len(values)) * 0.6,
                   marker={
                       'color': list(values.values),
                       'colorscale': px.colors.sequential.matter[4:7][::-1],
                       'line': dict(width=0),
                   },
                   ), ]
    layout = go.Layout(
        xaxis=dict(
            categoryorder='category ascending',
            tickfont=dict(size=10),
            tickangle=0,
            color='#e6e6e6',
            gridwidth=0.5,
            gridcolor="#333",
            zerolinecolor="#333"
        ),
        yaxis=dict(
            title='Number of Inverters',
            titlefont=dict(size=10),
            tickfont=dict(size=10),
            color='#e6e6e6',
            gridwidth=0.5,
            gridcolor="#333",
            zerolinecolor="#333"
        ),
        plot_bgcolor='#282828',
        paper_bgcolor='#222222',
        margin=dict(l=50, r=30, t=40, b=40),
    )
    figure = go.Figure(data=data, layout=layout)
    return dict(msgBar1=T('Inverter Startup Times'), figBar1=figure.to_json())


def bar2():
    values = df['Shutdown Time'].value_counts()
    data = [go.Bar(x=list(values.index),
                   y=list(values.values),
                   opacity=0.8,
                   width=np.ones(len(values))*0.6,
                   marker={
                       'color': list(values.values),
                       'colorscale': px.colors.sequential.haline[5:8],
                       'line': dict(width=0),
                   },
                   ), ]
    layout = go.Layout(
        xaxis=dict(
            categoryorder='category ascending',
            tickfont=dict(size=10),
            tickangle=0,
            color='#e6e6e6',
            gridwidth=0.5,
            gridcolor="#333",
            zerolinecolor="#333"
        ),
        yaxis=dict(
            title='Number of Inverters',
            titlefont=dict(size=10),
            tickfont=dict(size=10),
            color='#e6e6e6',
            gridwidth=0.5,
            gridcolor="#333",
            zerolinecolor="#333"
        ),
        plot_bgcolor='#282828',
        paper_bgcolor='#222222',
        margin=dict(l=50, r=30, t=40, b=40),
    )
    figure = go.Figure(data=data, layout=layout)
    return dict(msgBar2=T('Inverter Shutdown Times'), figBar2=figure.to_json())
