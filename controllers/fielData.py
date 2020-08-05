from plotly import subplots
import plotly.graph_objs as go


def index():
    response.flash = T("Transformer analysis")
    if request.vars.transformer:
        transformer = int(request.vars.transformer)
    else:
        transformer = 1
    date_str = "06/04/2020"

    resDict = fielData1(transformer, date_str)
    resDict.update(Triang4(date_str))
    resDict.update(Triang5(date_str))
    return resDict


def fielData1(transformer, date_str):
    trace1 = go.Scatterternary(name='Duval Triangle',
                               uid="a1a8b8",
                               a=[98, 1, 98],
                               b=[0, 0, 2],
                               c=[2, 0, 0],
                               fill="toself",
                               line={"color": "#444"},
                               mode="lines",
                               fillcolor="#3dd3c7",
                               text="PD",
                               hoverinfo='text')
    trace2 = go.Scatterternary(name='Duval Triangle1',
                               uid="c72344",
                               a=[0, 0, 64, 87],
                               b=[1, 77, 13, 13],
                               c=[0, 23, 23, 0],
                               fill="toself",
                               line={"color": "#444"},
                               mode="lines",
                               fillcolor="#8dd3c7",
                               text="D1",
                               hoverinfo='text')
    trace3 = go.Scatterternary(name='Duval Triangle2',
                               uid="3eab74",
                               a=[0, 0, 31, 47, 64],
                               b=[77, 29, 29, 13, 13],
                               c=[23, 71, 40, 40, 23],
                               fill="toself",
                               line={"color": "#444"},
                               mode="lines",
                               fillcolor="#bebada",
                               text="D2",
                               hoverinfo='text')
    trace4 = go.Scatterternary(name='Duval Triangle4',
                               uid="3eab74",
                               a=[1, 0, 35, 46, 96, 87, 47, 31],
                               b=[29, 15, 15, 4, 4, 13, 13, 29],
                               c=[71, 85, 50, 50, 0, 0, 40, 40],
                               fill="toself",
                               line={"color": "#444"},
                               mode="lines",
                               fillcolor="#fb8072",
                               text="DT",
                               hoverinfo='text')
    trace5 = go.Scatterternary(name='Duval Triangle5',
                               uid="381ad2",
                               a=[76, 80, 98, 98, 96],
                               b=[4, 0, 0, 2, 4],
                               c=[20, 20, 2, 0, 0],
                               fill="toself",
                               line={"color": "#444"},
                               mode="lines",
                               fillcolor="#80b1d3",
                               text="T1",
                               hoverinfo='text')
    trace6 = go.Scatterternary(name='Duval Triangle5',
                               uid="8cc163",
                               a=[46, 50, 80, 76],
                               b=[4, 0, 0, 4],
                               c=[50, 50, 20, 20],
                               fill="toself",
                               line={"color": "#444"},
                               mode="lines",
                               fillcolor="#90d133",
                               text="T2",
                               hoverinfo='text')
    trace7 = go.Scatterternary(name='Duval Triangle5',
                               uid="6f33dc",
                               a=[0, 0, 50, 35],
                               b=[15, 0, 0, 15],
                               c=[85, 1, 50, 50],
                               fill="toself",
                               line={"color": "#444"},
                               mode="lines",
                               fillcolor="#40f1d3",
                               text="T3",
                               hoverinfo='text')
    trace8 = go.Scatterternary(name='Duval Triangle5',
                               uid="6f33dc",
                               a=[32, 30, 34, 35],  # Pasar vector de datos historicos
                               b=[43, 50, 34, 54],  # Pasar vector de datos historicos
                               c=[25, 20, 32, 11],  # Pasar vector de datos historicos
                               mode="markers+lines",
                               marker={"size": 10, "color": "black", "symbol": 4}
                               )
    hover_value = [
        date_str + '<br>CH4: ' + '{}%'.format(trace8['a'][k]) + '<br>C2H2: ' + '{}%'.format(trace8['b'][k]) +
        '<br>C2H4: ' + '{}%'.format(trace8['c'][k]) for k in range(len(trace8['a']))]
    trace8['text'] = hover_value
    trace8['hoverinfo'] = 'text'

    figure = go.Figure()
    # Duval Triangle 1
    figure.add_trace(trace1)
    figure.add_trace(trace2)
    figure.add_trace(trace3)
    figure.add_trace(trace4)
    figure.add_trace(trace5)
    figure.add_trace(trace6)
    figure.add_trace(trace7)
    figure.add_trace(trace8)

    layoutT = go.Layout(ternary={
        "sum": 100,
        "aaxis": {
            "min": 0.01,
            "ticks": "outside",
            "title": "CH4",  # "(Methane)",
            "linewidth": 2,
            "ticksuffix": "%",
            "color": '#e6e6e6'
        },
        "baxis": {
            "min": 0.01,
            "ticks": "outside",
            "title": "C2H2",  # "(Acetylene)",
            "linewidth": 2,
            "ticksuffix": "%",
            "color": '#e6e6e6'
        },
        "caxis": {
            "min": 0.01,
            "ticks": "outside",
            "title": "C2H4",  # "(Ethylene)",
            "linewidth": 2,
            "ticksuffix": "%",
            "color": '#e6e6e6'
        }
    },
        showlegend=False,
        plot_bgcolor='#282828',
        paper_bgcolor='#222222',
        margin=dict(l=50, r=50, t=40, b=40)
    )
    figure['layout'].update(layoutT)
    figure.update_xaxes(tickfont=dict(color='#e6e6e6'))
    figure.update_yaxes(tickfont=dict(color='#e6e6e6'))
    for annotation in figure['layout']['annotations']:
        annotation['font'] = dict(color='#e6e6e6')
    return dict(message=T('Transformer analysis'), transformer=transformer, figure=figure.to_json())


def Triang4(date_str):
    # Duval Triangle 4
    trace9 = go.Scatterternary(name='Duval Triangle',
                               uid="a1a8b8",
                               a=[0, 9, 9, 0],
                               b=[1, 91, 30, 30],
                               c=[0, 0, 61, 70],
                               fill="toself",
                               line={"color": "#444"},
                               mode="lines",
                               fillcolor="#3dd3c7",
                               text="O",
                               hoverinfo='text')
    trace10 = go.Scatterternary(name='Duval Triangle1',
                                uid="c72344",
                                a=[9, 55, 9],
                                b=[91, 45, 45],
                                c=[0, 0, 46],
                                fill="toself",
                                line={"color": "#444"},
                                mode="lines",
                                fillcolor="#8dd3c7",
                                text="I",
                                hoverinfo='text')
    trace11 = go.Scatterternary(name='Duval Triangle2',
                                uid="3eab74",
                                a=[55, 1, 98, 97, 84, 85, 64, 40, 15, 15, 9, 9],
                                b=[45, 0, 0, 1, 1, 0, 0, 24, 24, 30, 30, 45],
                                c=[0, 0, 2, 2, 15, 15, 36, 36, 61, 55, 61, 46],
                                fill="toself",
                                line={"color": "#444"},
                                mode="lines",
                                fillcolor="#bebada",
                                text="S",
                                hoverinfo='text')
    trace12 = go.Scatterternary(name='Duval Triangle4',
                                uid="3eab74",
                                a=[98, 97, 84, 85],
                                b=[0, 1, 1, 0],
                                c=[2, 2, 15, 15],
                                fill="toself",
                                line={"color": "#444"},
                                mode="lines",
                                fillcolor="#fb8072",
                                text="PD",
                                hoverinfo='text')
    trace13 = go.Scatterternary(name='Duval Triangle5',
                                uid="381ad2",
                                a=[0, 0, 15, 15, 40, 64],
                                b=[0, 30, 30, 24, 24, 0],
                                c=[1, 70, 55, 61, 36, 36],
                                fill="toself",
                                line={"color": "#444"},
                                mode="lines",
                                fillcolor="#80b1d3",
                                text="C",
                                hoverinfo='text')
    trace14 = go.Scatterternary(name='Duval Triangle5',
                                uid="6f33dc",
                                a=[32, 30, 34, 35],  # Pasar vector de datos historicos
                                b=[43, 50, 34, 54],  # Pasar vector de datos historicos
                                c=[25, 20, 32, 11],  # Pasar vector de datos historicos
                                mode="markers+lines",
                                marker={"size": 10, "color": "black", "symbol": 4}
                                )
    hover_value = [
        date_str + '<br>H2: ' + '{}%'.format(trace14['a'][k]) + '<br>C2H6: ' + '{}%'.format(trace14['b'][k]) +
        '<br>CH4: ' + '{}%'.format(trace14['c'][k]) for k in range(len(trace14['a']))]
    trace14['text'] = hover_value
    trace14['hoverinfo'] = 'text'
    # Duval Triangle 4
    figure = go.Figure()
    figure.add_trace(trace9)
    figure.add_trace(trace10)
    figure.add_trace(trace11)
    figure.add_trace(trace12)
    figure.add_trace(trace13)
    figure.add_trace(trace14)
    # Layout
    layoutT = go.Layout(ternary={
        "sum": 100,
        "aaxis": {
            "min": 0.01,
            "ticks": "outside",
            "title": "H2",  # "(Methane)",
            "linewidth": 2,
            "ticksuffix": "%",
            "color": '#e6e6e6'
        },
        "baxis": {
            "min": 0.01,
            "ticks": "outside",
            "title": "C2H6",  # "(Acetylene)",
            "linewidth": 2,
            "ticksuffix": "%",
            "color": '#e6e6e6'
        },
        "caxis": {
            "min": 0.01,
            "ticks": "outside",
            "title": "CH4",  # "(Ethylene)",
            "linewidth": 2,
            "ticksuffix": "%",
            "color": '#e6e6e6'
        }},
        showlegend=False,
        plot_bgcolor='#282828',
        paper_bgcolor='#222222',
        margin=dict(l=50, r=50, t=50, b=50)
    )
    figure['layout'].update(layoutT)
    figure.update_xaxes(tickfont=dict(color='#e6e6e6'))
    figure.update_yaxes(tickfont=dict(color='#e6e6e6'))
    for annotation in figure['layout']['annotations']:
        annotation['font'] = dict(color='#e6e6e6')
    return dict(msgTriang4=T('Triangle 4'), figTriang4=figure.to_json())


def Triang5(date_str):
    # Duval Triangle 5
    trace15 = go.Scatterternary(name='Duval Triangle',
                                uid="a1a8b8",
                                a=[0, 46, 36, 0],
                                b=[1, 54, 54, 90],
                                c=[0, 0, 10, 10],
                                fill="toself",
                                line={"color": "#444"},
                                mode="lines",
                                fillcolor="#3dd3c7",
                                text="O",
                                hoverinfo='text')
    trace16 = go.Scatterternary(name='Duval Triangle1',
                                uid="c72344",
                                a=[46, 85, 75, 36],
                                b=[54, 15, 15, 54],
                                c=[0, 0, 10, 10],
                                fill="toself",
                                line={"color": "#444"},
                                mode="lines",
                                fillcolor="#8dd3c7",
                                text="S",
                                hoverinfo='text')
    trace17 = go.Scatterternary(name='Duval Triangle2',
                                uid="3eab74",
                                a=[85, 98, 96, 83],
                                b=[15, 2, 2, 15],
                                c=[0, 0, 2, 2],
                                fill="toself",
                                line={"color": "#444"},
                                mode="lines",
                                fillcolor="#bebada",
                                text="PD",
                                hoverinfo='text')
    trace18 = go.Scatterternary(name='Duval Triangle4',
                                uid="3eab74",
                                a=[83, 96, 98, 1, 90, 75],
                                b=[15, 2, 2, 0, 0, 15],
                                c=[2, 2, 0, 0, 10, 10],
                                fill="toself",
                                line={"color": "#444"},
                                mode="lines",
                                fillcolor="#fb8877",
                                text="DT",
                                hoverinfo='text')
    trace19 = go.Scatterternary(name='Duval Triangle5',
                                uid="381ad2",
                                a=[0, 60, 35, 0],
                                b=[90, 30, 30, 65],
                                c=[10, 10, 35, 35],
                                fill="toself",
                                line={"color": "#444"},
                                mode="lines",
                                fillcolor="#40b7d3",
                                text="I",
                                hoverinfo='text')
    trace20 = go.Scatterternary(name='Duval Triangle5',
                                uid="8cc163",
                                a=[78, 90, 65, 53],
                                b=[12, 0, 0, 12],
                                c=[10, 10, 35, 35],
                                fill="toself",
                                line={"color": "#444"},
                                mode="lines",
                                fillcolor="#90d133",
                                text="T2",
                                hoverinfo='text')
    trace21 = go.Scatterternary(name='Duval Triangle5',
                                uid="6f33dc",
                                a=[0, 35, 0, 16, 36, 38, 53, 65, 0],
                                b=[65, 30, 30, 14, 14, 12, 12, 0, 0],
                                c=[35, 35, 70, 70, 50, 50, 35, 35, 1],
                                fill="toself",
                                line={"color": "#444"},
                                mode="lines",
                                fillcolor="#40f1d3",
                                text="T3",
                                hoverinfo='text')
    trace22 = go.Scatterternary(name='Duval Triangle5',
                                uid="6f33dc",
                                a=[0, 60, 78, 38, 36, 16],
                                b=[30, 30, 12, 12, 14, 14],
                                c=[70, 10, 10, 50, 50, 70],
                                fill="toself",
                                line={"color": "#444"},
                                mode="lines",
                                fillcolor="#40f1d3",
                                text="T3",
                                hoverinfo='text')
    trace23 = go.Scatterternary(name='Duval Triangle5',
                                uid="6f33dc",
                                a=[32, 30, 34, 35],  # Pasar vector de datos historicos
                                b=[43, 50, 34, 54],  # Pasar vector de datos historicos
                                c=[25, 20, 32, 11],  # Pasar vector de datos historicos
                                mode="markers+lines",
                                marker={"size": 10, "color": "black", "symbol": 4}
                                )

    hover_value = [
        date_str + '<br>CH4: ' + '{}%'.format(trace23['a'][k]) + '<br>C2H6: ' + '{}%'.format(trace23['b'][k]) +
        '<br>C2H4: ' + '{}%'.format(trace23['c'][k]) for k in range(len(trace23['a']))]
    trace23['text'] = hover_value
    trace23['hoverinfo'] = 'text'
    figure = go.Figure()
    # Duval Triangle 5
    figure.add_trace(trace15)
    figure.add_trace(trace16)
    figure.add_trace(trace17)
    figure.add_trace(trace18)
    figure.add_trace(trace19)
    figure.add_trace(trace20)
    figure.add_trace(trace21)
    figure.add_trace(trace22)
    figure.add_trace(trace23)
    # Layout
    layoutT = go.Layout(ternary={
        "sum": 100,
        "aaxis": {
            "min": 0.01,
            "ticks": "outside",
            "title": "CH4",  # "(Methane)",
            "linewidth": 2,
            "ticksuffix": "%",
            "color": '#e6e6e6'
        },
        "baxis": {
            "min": 0.01,
            "ticks": "outside",
            "title": "C2H6",  # "(Acetylene)",
            "linewidth": 2,
            "ticksuffix": "%",
            "color": '#e6e6e6'
        },
        "caxis": {
            "min": 0.01,
            "ticks": "outside",
            "title": "C2H4",  # "(Ethylene)",
            "linewidth": 2,
            "ticksuffix": "%",
            "color": '#e6e6e6'
        }},
        showlegend=False,
        plot_bgcolor='#282828',
        paper_bgcolor='#222222',
        margin=dict(l=50, r=50, t=50, b=50)
    )
    figure['layout'].update(layoutT)
    figure.update_xaxes(tickfont=dict(color='#e6e6e6'))
    figure.update_yaxes(tickfont=dict(color='#e6e6e6'))
    for annotation in figure['layout']['annotations']:
        annotation['font'] = dict(color='#e6e6e6')
    return dict(msgTriang5=T('Triangle 5'), figTriang5=figure.to_json())
