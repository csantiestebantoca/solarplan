import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from os.path import dirname, join


df = pd.read_excel(join(dirname(__file__), 'mean_angle_difference.xlsx'))
df1 = pd.read_excel(join(dirname(__file__), 'maximum_angle_difference.xlsx'))
df2 = pd.read_excel(join(dirname(__file__), 'Time_of_Max_Angle.xlsx'))


def index():
    response.flash = T("Heatmaps")
    res_dict = dict(message="Heatmaps")
    res_dict.update(heatmap1())
    res_dict.update(heatmap2())
    res_dict.update(heatmap3())
    return res_dict


def heatmap1():
    NCU = df['NCU']
    MCU = df['MCU']
    Mean_Ang = df['Mean Angle Difference']
    fig = go.Figure(data=go.Heatmap(
        x=MCU,
        y=NCU,
        z=Mean_Ang,
        colorscale='Viridis',
        colorbar=dict(thickness=20, tickfont=dict(size=10, color='#e6e6e6')),
        xgap=1,
        ygap=1,
        hoverongaps=False))
    layout = go.Layout(
        xaxis=dict(
            tickfont=dict(color='#e6e6e6'),
            gridwidth=0.5,
            gridcolor="#333",
            zerolinecolor="#333"
        ),
        yaxis=dict(
            tickfont=dict(color='#e6e6e6'),
            gridwidth=0.5,
            gridcolor="#333",
            zerolinecolor="#333"
        ),
        plot_bgcolor='#282828',
        paper_bgcolor='#222222',
        margin=dict(t=40, b=20)
    )
    fig.update_layout(layout)
    return dict(msgHm1="Mean Angle Deviation", figHm1=fig.to_json())


def heatmap2():
    NCU = df1['NCU']
    MCU = df1['MCU']
    Mean_Ang = df1['Value']
    fig = go.Figure(data=go.Heatmap(
        x=MCU,
        y=NCU,
        z=Mean_Ang,
        colorscale='Viridis',
        colorbar=dict(thickness=20, tickfont=dict(size=10, color='#e6e6e6')),
        xgap=1,
        ygap=1,
        hoverongaps=False))
    layout = go.Layout(
        xaxis=dict(
            tickfont=dict(color='#e6e6e6'),
            gridwidth=0.5,
            gridcolor="#333",
            zerolinecolor="#333"
        ),
        yaxis=dict(
            tickfont=dict(color='#e6e6e6'),
            gridwidth=0.5,
            gridcolor="#333",
            zerolinecolor="#333"
        ),
        plot_bgcolor='#282828',
        paper_bgcolor='#222222',
        margin=dict(t=40, b=20)
    )
    fig.update_layout(layout)
    return dict(msgHm2="Maximum Angle Deviation", figHm2=fig.to_json())


def heatmap3():
    NCU = df2['NCU']
    MCU = df2['MCU']
    Mean_Ang = [None if pd.isna(e) else int(e[:2]) for e in df2['Value'].values]
    fig = go.Figure(data=go.Heatmap(
        x=MCU,
        y=NCU,
        z=Mean_Ang,
        colorscale='Viridis',
        colorbar=dict(thickness=20, tickfont=dict(size=10, color='#e6e6e6')),
        xgap=1,
        ygap=1,
        hoverongaps=False))
    layout = go.Layout(
        xaxis=dict(
            tickfont=dict(color='#e6e6e6'),
            gridwidth=0.5,
            gridcolor="#333",
            zerolinecolor="#333"
        ),
        yaxis=dict(
            tickfont=dict(color='#e6e6e6'),
            gridwidth=0.5,
            gridcolor="#333",
            zerolinecolor="#333"
        ),
        plot_bgcolor='#282828',
        paper_bgcolor='#222222',
        margin=dict(t=40, b=20)
    )
    fig.update_layout(layout)
    return dict(msgHm3="Time Maximum Deviation", figHm3=fig.to_json())
