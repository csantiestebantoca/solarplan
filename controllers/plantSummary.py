import numpy as np
import pandas as pd
from os.path import dirname, join
import plotly.express as px
import plotly.graph_objs as go
from sklearn.linear_model import LinearRegression as Reg


def load_data(filename):
    data = pd.read_csv(filename)
    data['Time'] = pd.to_datetime(data['Time'])

    cols = data.columns.tolist()
    dictionary = {}
    for elem in cols:
        dictionary[elem] = data[elem]

    dates = ['Time']
    features = [e for e in dictionary if (e not in dates)]

    return data, dates, features


filename1 = join(dirname(__file__), 'Stn01Inv01.csv')
df, dates, features = load_data(filename1)


def index():
    response.flash = T("Plant Summary")
    res_dict = dict(message="Plant Summary")
    res_dict.update(powerComparison())
    res_dict.update(correlation())
    res_dict.update(correlationRegression())
    res_dict.update(barInv())
    res_dict.update(bar())
    res_dict.update(bar2())
    res_dict.update(dailySummary())
    return res_dict


def powerComparison():
    time = "Time"
    serie = ['Expected_Specific_DCPower', 'Specific_DCPower']
    colors = px.colors.qualitative.Plotly
    data = [go.Scatter(x=df[time], y=df[e], mode='lines', opacity=0.8, name=e, line={'width': 2},
                       marker={'color': colors[serie.index(e) % len(colors)]}) for e in serie]
    layout = go.Layout(
        xaxis=dict(
            tickfont=dict(size=10),
            color='#e6e6e6',
            gridwidth=0.5,
            gridcolor="#333",
            zerolinecolor="#333"
        ),
        yaxis=dict(
            title='Total Plant Power (kW)',
            titlefont=dict(size=10),
            tickfont=dict(size=10),
            tickangle=270,
            color='#e6e6e6',
            gridwidth=0.5,
            gridcolor="#333",
            zerolinecolor="#333"
        ),
        legend=dict(orientation='h', x=0, y=1.2, font=dict(color='#e6e6e6', size=9)),
        plot_bgcolor='#282828',
        paper_bgcolor='#222222',
        margin=dict(l=5, r=5, t=80, b=50)
    )
    figure = go.Figure(data=data, layout=layout)
    return dict(msgPow=T('Plant Power'), figPow=figure.to_json())


def correlation():
    times = [round(float(e.hour), 2) for e in df[dates[0]]]
    scatddx = "POA_Irradiance"
    scatddy = "Specific_ACPower"
    data = go.Scatter(
        x=df[scatddx],
        y=df[scatddy],
        mode='markers',
        opacity=0.8,
        marker={
            'size': 4,
            'color': times,  # set color equal to a variable
            'colorscale': 'Rainbow',  # one of plotly colorscales
            'showscale': True,
            'colorbar': dict(thickness=15, tickfont=dict(size=8, color='#e6e6e6'),
                             title=dict(text='Hour', font=dict(size=9, color='#e6e6e6'))),
        }
    )
    layout = go.Layout(
        xaxis=dict(
            title=scatddx,
            titlefont=dict(size=10),
            tickfont=dict(size=10),
            color='#e6e6e6',
            gridwidth=0.5,
            gridcolor="#333",
            zerolinecolor="#333"
        ),
        yaxis=dict(
            title=scatddy,
            titlefont=dict(size=10),
            tickfont=dict(size=10),
            color='#e6e6e6',
            gridwidth=0.5,
            gridcolor="#333",
            zerolinecolor="#333"
        ),
        plot_bgcolor='#282828',
        paper_bgcolor='#222222',
        margin=dict(l=5, r=5, t=50, b=50),
    )
    figure = go.Figure(data=data, layout=layout)
    return dict(msgCorr=T('Correlation analysis'), figCorr=figure.to_json())


def correlationRegression():
    scatddx = "POA_Irradiance"
    scatddy = "Specific_ACPower"
    reg = Reg()
    reg.fit_intercept = False
    reg.fit(np.vstack(df[scatddx]), df[scatddy])
    pred = reg.predict(np.vstack(df[scatddx]))

    data = go.Scatter(
        x=df[scatddx],
        y=df[scatddy],
        mode='markers',
        opacity=0.8,
        marker={'size': 4},
        showlegend=False
    )
    layout = go.Layout(
        xaxis=dict(
            title=scatddx,
            titlefont=dict(size=10),
            tickfont=dict(size=10),
            color='#e6e6e6',
            gridwidth=0.5,
            gridcolor="#333",
            zerolinecolor="#333"
        ),
        yaxis=dict(
            title=scatddy,
            titlefont=dict(size=10),
            tickfont=dict(size=10),
            color='#e6e6e6',
            gridwidth=0.5,
            gridcolor="#333",
            zerolinecolor="#333"
        ),
        plot_bgcolor='#282828',
        paper_bgcolor='#222222',
        margin=dict(l=5, r=5, t=50, b=50),
    )
    figure = go.Figure(data=data, layout=layout)
    figure.add_trace(go.Scatter(
        x=df[scatddx],
        y=pred,
        mode='lines',
        opacity=0.8,
        line={'width': 2},
        showlegend=False
    ))
    return dict(msgCorrReg=T('Correlation and Regression'), figCorrReg=figure.to_json())


def barInv():
    inv = [[1, 2, 3, 4] for _ in range(4)]
    inv = [e for items in inv for e in items]
    ir = [[i, i, i, i] for i in range(1, 5)]
    ir = [e for items in ir for e in items]
    x = list(zip(ir, inv))
    x = ['IR-'+str(e[0])+'_INV'+str(e[1]) for e in x]
    y = np.random.uniform(size=4*4) / 2 + 4.5

    colors = px.colors.qualitative.Prism
    colors = [colors[7]] + [colors[8]] + [colors[3]] + [colors[2]]
    colors = [colors for _ in range(4)]
    colors = [e for items in colors for e in items]

    x.insert(4, 'IR-1_INV5')
    y = list(y)
    y.insert(4, np.random.uniform() / 2 + 4.5)
    colors.insert(4, px.colors.qualitative.Prism[0])

    data = [go.Bar(x=x,
                   y=y,
                   opacity=0.9,
                   marker_color=colors,
                   marker={'line': dict(width=0)},
                   ), ]
    layout = go.Layout(
        xaxis=dict(
            tickfont=dict(size=10),
            tickangle=-45,
            color='#e6e6e6',
            gridwidth=0.5,
            gridcolor="#333",
            zerolinecolor="#333"
        ),
        yaxis=dict(
            title='Daily Specific Production (kWh/kWp/day)',
            titlefont=dict(size=10),
            tickfont=dict(size=10),
            color='#e6e6e6',
            gridwidth=0.5,
            gridcolor="#333",
            zerolinecolor="#333"
        ),
        plot_bgcolor='#282828',
        paper_bgcolor='#222222',
        margin=dict(l=10, r=10, t=40, b=10),
    )
    figure = go.Figure(data=data, layout=layout)
    return dict(msgBarInv=T('Inverter Daily Specific Production'), figBarInv=figure.to_json())


def bar():
    x = ['Expected', 'Actual', 'PVSyst']
    y = [141000, 142000, 140000]
    plotly_color = px.colors.qualitative.Plotly
    colors = [plotly_color[1]] + [plotly_color[4]] + [plotly_color[2]]
    data = [go.Bar(x=x,
                   y=y,
                   opacity=0.8,
                   marker={
                       'color': colors,
                       'line': dict(width=0),
                   },
                   ), ]
    layout = go.Layout(
        xaxis=dict(
            tickfont=dict(size=10),
            tickangle=0,
            color='#e6e6e6',
            gridwidth=0.5,
            gridcolor="#333",
            zerolinecolor="#333"
        ),
        yaxis=dict(
            title='Energy (kWh)',
            titlefont=dict(size=10),
            tickfont=dict(size=10),
            color='#e6e6e6',
            gridwidth=0.5,
            gridcolor="#333",
            zerolinecolor="#333"
        ),
        plot_bgcolor='#282828',
        paper_bgcolor='#222222',
        margin=dict(l=10, r=10, t=40, b=10),
    )
    figure = go.Figure(data=data, layout=layout)
    return dict(msgBar=T('Daily Production'), figBar=figure.to_json())


def bar2():
    x = ['Expected', 'Actual', 'PVSyst']
    y = [76.7, 75.6, 76.3]
    plotly_color = px.colors.qualitative.Plotly
    colors = [plotly_color[1]] + [plotly_color[4]] + [plotly_color[2]]
    data = [go.Bar(x=x,
                   y=y,
                   opacity=0.8,
                   marker={
                       'color': colors,
                       'line': dict(width=0),
                   },
                   ), ]
    layout = go.Layout(
        xaxis=dict(
            tickfont=dict(size=10),
            tickangle=0,
            color='#e6e6e6',
            gridwidth=0.5,
            gridcolor="#333",
            zerolinecolor="#333"
        ),
        yaxis=dict(
            title='PR (%)',
            titlefont=dict(size=10),
            tickfont=dict(size=10),
            color='#e6e6e6',
            gridwidth=0.5,
            gridcolor="#333",
            zerolinecolor="#333"
        ),
        plot_bgcolor='#282828',
        paper_bgcolor='#222222',
        margin=dict(l=10, r=10, t=40, b=10),
    )
    figure = go.Figure(data=data, layout=layout)
    return dict(msgBar2=T('Daily PR'), figBar2=figure.to_json())



def dailySummary():
    headerColor = 'royalblue'
    rowEvenColor = 'lightblue'
    rowOddColor = 'white'

    fig = go.Figure(data=[go.Table(
        columnwidth=[3, 2],
        header=dict(
            values=['<b>DAILY SUMMARY</b>', '<b>Values</b>'],
            line_color='darkslategray',
            fill_color=headerColor,
            align=['left', 'center'],
            font=dict(color='white', size=10)
        ),
        cells=dict(
            values=[
                ['Total AC Specific Production', 'Total AC Production',
                 'Total DC Specific Production', 'Total DC Production',
                 '<b>Availability</b>'],
                ['4.908 kWh/kWp', '6252.487 kWh', '4.982 kWh/kWp', '6347.622 kWh', '100%']],
            line_color='darkslategray',
            # 2-D list of colors for alternating rows
            fill_color=[[rowOddColor, rowEvenColor] * 6],
            align=['left', 'center'],
            font=dict(color='darkslategray', size=9),
        ))],
        layout=go.Layout(
            paper_bgcolor='#222222',
            margin=dict(l=0, r=0)
        )
    )
    return dict(msgSum=T('Daily Summary'), figSum=fig.to_json())