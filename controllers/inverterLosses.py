import numpy as np
import pandas as pd
from os.path import dirname, join
from plotly import subplots
import plotly.graph_objs as go
import plotly.express as px


# ---- Data ----
def load_data(filename):
    data = pd.read_csv(filename)
    # data['Time'] = pd.to_datetime(data['Time'])

    cols = data.columns.tolist()
    dictionary = {}
    for elem in cols:
        dictionary[elem] = data[elem]

    dates = []  # ['Time']
    features = [e for e in dictionary if (e not in dates)]

    return data, dates, features


filename1 = join(dirname(__file__), 'Inverter Loses.csv')
df, dates, features = load_data(filename1)


def index():
    response.flash = T("Inverter Losses")
    res_dict = dict(title='Inverter Losses')

    cols = ['Availability', 'IAM Loses', 'Inverter Loses', 'Limiting Loses',
            'Low Light Loses', 'Ohmic Loses', 'Power Threshold Losses', 'Thermal Losses']

    for i in range(len(cols)):
        dict_e = heatmap(cols[i])
        res_dict.update({'msg'+str(i+1): dict_e['message'], 'fig'+str(i+1): dict_e['figure']})

    res_dict.update(violin())
    return res_dict


def violin():
    cols = ['IAM Loses', 'Inverter Loses', 'Limiting Loses', 'Low Light Loses',
            'Ohmic Loses', 'Power Threshold Losses', 'Thermal Losses']
    data = [go.Violin(y=df[e], name=e, box_visible=True, meanline_visible=True) for e in cols]
    layout = go.Layout(
        xaxis=dict(
            tickfont=dict(size=11),
            color='#e6e6e6',
            gridwidth=0.5,
            gridcolor="#333",
            zerolinecolor="#333"
        ),
        yaxis=dict(
            title='Loss Amount (%)',
            titlefont=dict(size=11),
            tickfont=dict(size=11),
            color='#e6e6e6',
            gridwidth=0.5,
            gridcolor="#333",
            zerolinecolor="#333"
        ),
        legend=dict(x=0, y=1.2, orientation='h', font=dict(size=12, color='#e6e6e6')),
        plot_bgcolor='#282828',
        paper_bgcolor='#222222',
        margin=dict(l=50, r=20, t=80, b=20)
    )
    figure = go.Figure(data=data, layout=layout)
    return dict(msgViolin='Loss Variations By Type (%)', figViolin=figure.to_json())


def heatmap(col):
    filename2 = join(dirname(__file__), 'Inverter Loses.csv')
    df1 = pd.read_csv(filename2)
    RdYlGn = px.colors.diverging.RdYlGn[:]
    my_colors = [[0.0, RdYlGn[1]], [0.2, RdYlGn[1]],
                 [0.2, RdYlGn[3]], [0.4, RdYlGn[3]],
                 [0.4, RdYlGn[5]], [0.6, RdYlGn[5]],
                 [0.6, RdYlGn[7]], [0.8, RdYlGn[7]],
                 [0.8, RdYlGn[9]], [1.0, RdYlGn[9]]]
    color_vals = np.round(np.linspace(np.min(df1[col]), np.max(df1[col]), 6), 4)
    data = [go.Heatmap(x=df1['Station'],
                       y=df1['Inverter1'],
                       z=df1[col],
                       opacity=0.8,
                       colorscale=my_colors,
                       colorbar=dict(thickness=15, tickfont=dict(size=12, color='#e6e6e6'), tickvals=color_vals),
                       xgap=1,
                       ygap=1,
                       hoverongaps=False,
                       zmin=np.round(np.min(df1[col]), 4),
                       zmax=np.round(np.max(df1[col]), 4)
                       )]
    layout = go.Layout(
        xaxis=dict(
            title=dict(text="Block", font=dict(color='#e6e6e6')),
            tickfont=dict(color='#e6e6e6'),
            showgrid=False
        ),
        yaxis=dict(
            title=dict(text="Inverter", font=dict(color='#e6e6e6')),
            tickfont=dict(color='#e6e6e6'),
            showgrid=False
        ),
        margin=dict(l=50, r=50, t=60, b=40),
        plot_bgcolor='#282828',
        paper_bgcolor='#222222',
    )
    fig = go.Figure(data=data, layout=layout)
    return dict(message=T(col), figure=fig.to_json())
