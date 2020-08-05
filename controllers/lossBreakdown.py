import plotly.graph_objs as go
import plotly.express as px
import operator
import pandas as pd
from os.path import dirname, join


def index():
    res_dict = lossBreakdown()
    res_dict.update(waterFall())
    return res_dict


def lossBreakdown():
    filename = join(dirname(__file__), 'Losses.csv')
    df = pd.read_csv(filename)
    fig = px.sunburst(df, path=['Losses', 'Type', 'Name'], values='values')
    fig.update_layout(paper_bgcolor='#222222', margin=dict(t=5, b=5))
    fig.update_traces(
        marker=dict(
            line=dict(color='#e6e6e6', width=0.3),
            colors=px.colors.qualitative.D3
        ),
        opacity=0.8,
        textfont=dict(color='white'),
        hoverlabel=dict(font=dict(color='white')),
        insidetextorientation='radial'
    )
    return dict(message=T('Loss Breakdown'), figure=fig.to_json())


def pie2():
    labels = ['Temperature', 'Reflection', 'Irradiance', 'DC Ohmic', 'Inv Efficiency', 'Power Threshold',
              'AC Ohmic and Transformer', 'Night Consumption', 'Aggregate']
    values = [27.769, 3.202, 1.679, 7.629, 8.858, 0.107, 6.396, 0.002, 44.357]
    losses = list(zip(labels, values))
    losses.sort(key=operator.itemgetter(1), reverse=True)
    data = [go.Pie(labels=[e[0] for e in losses],
                   values=[e[1] for e in losses],
                   opacity=0.8,
                   textinfo='label+percent',
                   insidetextorientation='radial',
                   marker=dict(colors=px.colors.qualitative.G10),
                   textfont=dict(color='#e6e6e6', size=9),
                   showlegend=False
                   )
            ]
    layout = go.Layout(
        paper_bgcolor='#222222',
        margin=dict(l=0, r=0, t=0, b=0)
    )
    fig = go.Figure(data=data, layout=layout)
    return dict(msgPie2=T('Loss Breakdown'), figPie2=fig.to_json())

def waterFall():
    df2 = pd.read_csv(join(dirname(__file__), 'waterfall.csv'))

    GTI = 9561.7  # To get from database for that day
    DC_Capacity = 19501  # To get from database for that day
    Actual_Energy = 143100000  # To get from database for that day

    Total_solar_Energy = GTI * DC_Capacity
    y1 = [Total_solar_Energy]
    y2 = df2['Loss Value'] * (Total_solar_Energy / 100)
    y3 = y2.to_list()
    y4 = y1 + y3 + [0] + [0] + [Actual_Energy * -1]

    y5 = sum(y4) * -1
    y6 = y1 + y3 + [0] + [y5] + [Actual_Energy]

    fig = go.Figure(go.Waterfall(
        name="Expected", orientation="v",
        measure=["relative", "relative", "relative", "relative", "relative", "relative", "relative", "relative",
                 "relative", "relative", "relative", "relative", "relative",
                 "total", "relative", "total", "relative", "total"],
        x=['Energy hitting Panels'] + df2['Loss Mode'].to_list() + ['Expected Energy'] + ['Incidental Loses'] + [
            'Actual Energy'],
        textposition="outside",
        y=y6,
        connector={"line": {"color": "rgb(63, 63, 63)"}},
    ))
    axis = dict(
            tickfont=dict(size=10),
            color='#e6e6e6',
            gridwidth=0.5,
            gridcolor="#333",
            zerolinecolor="#333"
        )
    fig.update_layout(
        xaxis=axis,
        yaxis=axis,
        title=dict(text="Energy losses waterfall analysis", font=dict(color='#e6e6e6')),
        showlegend=True,
        legend=dict(font=dict(color='#e6e6e6')),
        plot_bgcolor='#282828',
        paper_bgcolor='#222222',
        margin=dict(l=50, r=50, t=50, b=0)
    )

    return dict(msgWaterF=T('Waterfall'), figWaterF=fig.to_json())
