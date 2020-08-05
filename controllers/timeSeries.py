# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

import pandas as pd
from os.path import dirname, join
import plotly.express as px
import plotly.graph_objs as go


# ---- Data ----
def load_data(filename):
    data = pd.read_csv(filename)
    data['Datetime_x'] = pd.to_datetime(data['Datetime_x'])
    data['Datetime_y'] = pd.to_datetime(data['Datetime_y'])
    data['Time'] = pd.to_datetime(data['Time'])

    cols = data.columns.tolist()
    dictionary = {}
    for elem in cols:
        dictionary[elem] = data[elem]

    dates = ['Datetime_x', 'Time', 'Datetime_y']
    categories = ['Day', 'Backtracking']
    features = [e for e in dictionary if (e not in dates) and (e not in categories)]

    # return dictionary, dates, categories, features
    return data, dates, categories, features


filename1 = join(dirname(__file__), 'IR-1_INV1_combined.csv')
filename2 = join(dirname(__file__), 'String_data.csv')
df, dates, categories, features = load_data(filename1)


# ---- Pages ----
def index():
    response.flash = T("Time series analysis")
    if request.vars.time:
        time = request.vars.time
    else:
        time = "Time"
    if request.vars.serie:
        serie = (str(request.vars.serie)).split(",")
    else:
        serie = ['Elevation_Panel_Plane', 'Panel_Angle', 'Sun_Elevation']
    serie = serie[:12] if len(serie) > 12 else serie  # Just the first twelve!
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
            tickfont=dict(color=data[0]['marker']['color'], size=10),
            gridwidth=0.5,
            gridcolor="#333",
            zerolinecolor="#333"
        ),
        legend=dict(x=0, y=1.2,
                    orientation='h', font=dict(color='#e6e6e6')),
        plot_bgcolor='#282828',
        paper_bgcolor='#222222',
        margin=dict(l=50, r=50, t=30, b=10)
    )
    figure = go.Figure(data=data, layout=layout)
    figure['layout']['xaxis']['domain'] = [0, max(0.0, 1 - (len(serie) - 2) * 0.04)] if len(serie) > 2 else [0, 1]
    for i in range(1, len(serie)):
        figure['data'][i]['yaxis'] = 'y' + str(i + 1)
        figure['layout']['yaxis' + str(i + 1)] = dict(
            tickfont=dict(color=figure['data'][i]['marker']['color'], size=10),
            overlaying='y', side='right', anchor='free', gridwidth=0.5,
            gridcolor="#333", zerolinecolor="#333", position=max(0.0, 1 - (i - 1) * 0.04))
    return dict(message=T('Time series analysis'), figure=figure.to_json(),
                features=features, dates=dates, time=time, serie=serie)


# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
