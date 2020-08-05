import plotly.graph_objs as go
import subprocess


def index():
    process1 = subprocess.Popen(['python', 'C://Users//L03070625//Google Drive//Campus Toluca//Work//Dubai//Project//'
                                           'WEP2PY//Cosme2//Aruna-Apps//applications//solarplants//views//Dash//'
                                           'exSumDash.py'])
    res_dict = execSummary()
    return res_dict


def execSummary():
    headerColor = 'royalblue'
    rowEvenColor = 'lightblue'
    rowOddColor = 'white'

    fig = go.Figure(data=[go.Table(
        columnwidth=[2, 1],
        header=dict(
            values=['<b>EXECUTIVE SUMMARY</b>', '<b>Values</b>'],
            line_color='darkslategray',
            fill_color=headerColor,
            align=['left', 'center'],
            font=dict(color='white', size=14)
        ),
        cells=dict(
            values=[
                ['Total Actual Generation Inverter Level', 'Total Actual Generation Meter Level',
                 'Total Actual Irradiation', 'Total Actual Plant Losses', 'Total Expected Plant Losses',
                 '<b>PERFORMANCE RATIO</b>'],
                ['347.1 MWh', '343.3 MWh', '4328.2 kWh/m2', '69.7 MWh', '70.2 MWh', '76.7']],
            line_color='darkslategray',
            # 2-D list of colors for alternating rows
            fill_color=[[rowOddColor, rowEvenColor] * 6],
            align=['left', 'center'],
            font=dict(color='darkslategray', size=13),
        ))],
        layout=go.Layout(
            paper_bgcolor='#222222',
            margin=dict(l=40, r=40, t=50, b=50)
        )
    )
    return dict(message=T('Executive Summary'), figure=fig.to_json())
