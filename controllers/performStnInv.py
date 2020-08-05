import pandas as pd
from os.path import dirname, join
import plotly.express as px
import plotly.graph_objs as go
import numpy as np


# ---- Data ----
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

def load_data_SQL(block, day, inv, ws):
    import pyodbc
    cnxn = pyodbc.connect('Driver={SQL Server};'
                          'Server=192.168.1.104;'
                          'Database=BOUJDOUR;'
                          'UID=development;PWD=g]9XM5&=5^3PznC')
    cursor = cnxn.cursor()
    cursor.execute("exec SP_Stn_Inv_Performance 1, '2018-10-04', 'INV1', 2 ") #+ block + ", " + day + ", " + inv + ", " + ws)
    data = cursor.fetchall()
    #data = pd.read_sql(cursor,cnxn)
    data = [[value for value in row] for row in data]
    cols = ['timestamp','hours','IR_INVACT_PWR_VAL0','WMSTILT_RADIATION_VAL0']
    data = pd.DataFrame(data = data, columns=cols)
    dictionary = {}
    for d in cols:
        dictionary[d] = data[d]
        

    dates = ['timestamp']
    
    features = [e for e in dictionary if (e not in dates)]

    return data, dates, features


filename1 = join(dirname(__file__), 'Stn01Inv01.csv')
df, dates, features = load_data(filename1)


def index():
    response.flash = T("Transformer analysis")
    ws = 2
    station = 1
    inverter = 'INV1'
    date_str = '2018-10-04'
    if request.vars.ws:
        ws = int(request.vars.ws)
    if request.vars.station:
        station = int(request.vars.station)
    if request.vars.inverter:
        inverter = request.vars.inverter

    df_SQL, dates_SQL, features_SQL = load_data_SQL(str(station), date_str, inverter, str(ws))

    res_dict = dict(station=station, inverter=inverter)
    res_dict.update(powerComparison())
    res_dict.update(correlation(df_SQL, dates_SQL, features_SQL, station, date_str, inverter, ws))
    res_dict.update(scat3D())

    losses = powerComparison(['Thermal_Losses(%)', 'Inverter_Losses(%)'], 'Losses (%)')
    res_dict.update(dict(msgLoss='Specific Power Losses', figLoss=losses['figPowComp']))

    res_dict.update(bar())
    res_dict.update(dailySummary())
    return res_dict


def powerComparison(serie=None, ytitle=None):
    time = "Time"
    serie = ['Specific_ACPower', 'Specific_DCPower', 'Expected_Specific_DCPower',
             'Expected_Specific_DCPower'] if serie is None else serie
            # IR_INVACT_PWR_VAL0, IR_INVDC_PWR_VAL0, pending, pending
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
            title='Specific Power (kW/kWp)' if ytitle is None else ytitle,
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
    return dict(msgPowComp=T('Specific Power Comparison'), figPowComp=figure.to_json())


<<<<<<< HEAD
def correlation(df_SQL, dates_SQL, features_SQL, station, date_str, inverter, ws):
    scatddx = "WMSTILT_RADIATION_VAL0"
    scatddy = "IR_INVACT_PWR_VAL0"
    data = go.Scatter(
        x=df_SQL[scatddx],
        y=df_SQL[scatddy],
=======
def correlation():
    times = [round(float(e.hour), 2) for e in df[dates[0]]]
    scatddx = "POA_Irradiance"                                  # WMSTILT_RADIATION_VAL0 si Block 1 y 2 -> WS2 else WS 4
    scatddy = "Specific_ACPower"                                # IR_INVACT_PWR_VAL0
    data = go.Scatter(                                          # Especificar fecha (1 día)
        x=df[scatddx],
        y=df[scatddy],
>>>>>>> feature/cosme
        mode='markers',
        opacity=0.8,
        marker={
            'size': 4,
            'color': df_SQL['hours'],  # set color equal to a variable
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


def scat3D():                                   # Inverter efficiency
    A1 = 70.55686E-7                            # Parámetros constantes para cada planta [pending]
    A2 = 0.98023
    x0 = 45.82587
    p = 5.23251

    A12 = -4.05224E-7
    A22 = 0.98042
    x02 = 45.47717
    p2 = 4.8067

    A13 = -4.05224E-7
    A23 = 0.98042
    x03 = 45.47717
    p3 = 4.806

    x = []
    z1 = []
    z2 = []
    z3 = []
    for i in range(0, 1165, 5):
        x.append(i)
        z1.append(A2 + (A1 - A2) / (1 + (i / x0) ** p))
        z2.append(A22 + (A12 - A22) / (1 + (i / x02) ** p2))
        z3.append(A23 + (A13 - A23) / (1 + (i / x03) ** p3))

    fig = go.Figure(go.Surface(
        x=x,
        y=[600, 610, 675, 740, 800],
        z=[z1, z2, z3, z3, z3],
        opacity=0.15,
        colorscale=px.colors.sequential.YlGnBu[::-1],  # px.colors.sequential.Viridis[4:10],
        showscale=False
    ))

    #fig = go.Figure()

    df2 = pd.read_csv(join(dirname(__file__), 'IR-1_INV1_combined.csv'))
    df2['Efficiency'] = np.where(df2['INV1-DCP'] > 0, df2['INV1-ACP'] / df2['INV1-DCP'], 0)
    X = df2['INV1-DCP']                                 # IR_INVDC_PWR_VAL0
    Y = df2['INV1-DCV']                                 # IR_INVDC_VOLT_VAL0
    Z = df2['Efficiency']                               # Calculado IR_INVACT_PWR_VAL0 / IR_INVDC_PWR_VAL0

    fig.add_scatter3d(x=X[:609], y=Y[:609], z=Z[:609], mode='markers',
                      marker=dict(opacity=0.8,
                                  size=4,
                                  color=df['Module_Temperature'],
                                  colorscale=px.colors.sequential.Plasma[3:8],
                                  colorbar=dict(thickness=15, tickfont=dict(size=8, color='#e6e6e6'),
                                                lenmode='fraction', len=0.8,
                                                title=dict(text='Temp', font=dict(size=9, color='#e6e6e6'))),
                                  showscale=True,
                                  line=dict(width=0),
                                  )
                      )

    fig.update_layout(
        scene=dict(
            xaxis=dict(
                nticks=20,
                title='Specific DCPower',
                backgroundcolor='#222222',
                titlefont=dict(size=9),
                tickfont=dict(size=9),
                color='#e6e6e6',
                gridwidth=0.5,
                gridcolor="#555555",
                linecolor="#555555",
                zerolinecolor="#555555",
                showbackground=True,
            ),
            yaxis=dict(
                title='DC Voltage (V)',
                backgroundcolor='#222222',
                titlefont=dict(size=9),
                tickfont=dict(size=9),
                color='#e6e6e6',
                gridwidth=0.5,
                gridcolor="#555555",
                linecolor="#555555",
                zerolinecolor="#555555",
                showbackground=True,
            ),
            zaxis=dict(
                nticks=4,
                title='Inverter Efficiency',
                backgroundcolor='#222222',
                titlefont=dict(size=9),
                tickfont=dict(size=9),
                color='#e6e6e6',
                gridwidth=0.5,
                gridcolor="#555555",
                linecolor="#555555",
                zerolinecolor="#555555",
                showbackground=True,
            ),
            camera_eye={"x": 0, "y": -1, "z": 2},
            aspectratio={"x": 1, "y": 1, "z": 1}
        ),
        plot_bgcolor='#282828',
        paper_bgcolor='#222222',
        margin=dict(l=0, r=0, b=0, t=0)
    )

    return dict(msgEff=T('Inverter Efficiency'), figEff=fig.to_json())


def bar():
    x = ['Thermal_Losses(%)', 'Inverter_Losses(%)']
    y = [np.average(df[x[0]]), np.average(df[x[1]])]
    colors = px.colors.sequential.Viridis[2:8]
    data = [go.Bar(x=x,
                   y=y,
                   opacity=0.8,
                   width=np.ones(len(y)) * 0.4,
                   marker={
                       'color': y,
                       'colorscale': colors,
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
            title='Losses (%)',
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
    return dict(msgBar=T('Total Daily Losses'), figBar=figure.to_json())


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
    return dict(message=T('Station Inverter Performance'), msgDaySum=T('Daily Summary'), figDaySum=fig.to_json())
