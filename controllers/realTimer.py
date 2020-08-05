import plotly.graph_objs as go
import numpy as np
import plotly.express as px
import pandas as pd
from os.path import dirname, join


def index():
    response.flash = T("Real Times")
    res_dict = timers()
    res_dict.update(timers2())
    return res_dict


RdYlGn = px.colors.diverging.RdYlGn[:]


def timers():
    titles = ['Total AC Power', 'POA AVG Irradiance', 'Panel Temp', 'Custom']
             # CHECK_METERCHECKMETER_TOTAL_ACTIVE_POWER_EXPORT_VAL0, WMSTILT_RADIATION_VAL0, WMSMODULE_TEMP_VAL0
             # Custom -> Menú Lino
    fig = go.Figure()
    for i in range(4):
        clock_template = go.Indicator(
            domain={'row': 0, 'column': i},
            value=np.random.randint(200, 500),
            mode="gauge+number+delta",
            title={'text': titles[i], 'font': {'color': '#e6e6e6', 'size': 18}},
            delta={'reference': 380, 'increasing': {'color': RdYlGn[1]}, 'decreasing': {'color': RdYlGn[1]}},
            gauge={'axis': {'range': [None, 500], 'tickcolor': "#e6e6e6", 'tickfont': {'color': '#e6e6e6'}},
                   'bar': {'color': RdYlGn[9]},
                   'steps': [
                       {'range': [0, 250], 'color': "#e6e6e6"},
                       {'range': [250, 400], 'color': "#a6a6a6"}],
                   'threshold': {'line': {'color': RdYlGn[1], 'width': 4}, 'thickness': 0.75, 'value': 490}}
            )
        fig.add_trace(clock_template)

    fig.update_layout(
        grid={'rows': 1, 'columns': 4, 'pattern': "independent", 'xgap': 0.25},
        font={'color': "#e6e6e6"},
        plot_bgcolor='#282828',
        paper_bgcolor='#222222',
        margin=dict(l=30, r=30, t=0, b=0)
    )

    return dict(msgReal='Real Times', figReal=fig.to_json())


def timers2():
    df = pd.read_csv(join(dirname(__file__), 'Inverter Real Time.csv'))
    Station = df['Station']
    Inverter = df['Inverter']
    ACPower = df['AC Power']

    my_colors = [[0.0, RdYlGn[1]], [0.2, RdYlGn[1]],
                 [0.2, RdYlGn[3]], [0.4, RdYlGn[3]],
                 [0.4, RdYlGn[5]], [0.6, RdYlGn[5]],
                 [0.6, RdYlGn[7]], [0.8, RdYlGn[7]],
                 [0.8, RdYlGn[9]], [1.0, RdYlGn[9]]]

    my_ACPower = np.array(list(filter(lambda power: power != ' None', ACPower)), dtype=float)

    fig = go.Figure(data=go.Heatmap(
        x=Inverter,
        y=Station,
        z=ACPower,
        colorscale=my_colors,
        # colorscale='RdYlGn',
        colorbar=dict(thickness=20, tickfont=dict(size=10, color='#e6e6e6'),
                      tickvals=np.linspace(np.min(my_ACPower), np.max(my_ACPower), 6)),
        xgap=2,
        ygap=2,
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

    return dict(msgReal2='Inverter Real Times', figReal2=fig.to_json())
