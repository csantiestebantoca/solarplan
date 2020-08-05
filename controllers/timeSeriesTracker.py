import pandas as pd
from os.path import dirname, join
import plotly.express as px
import plotly.graph_objs as go


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


filename1 = join(dirname(__file__), 'tracker_data.csv')
df, dates, features = load_data(filename1)


# ---- Pages ----
def index():
    response.flash = T("Angle Distribution")
    time = "Time"
    serie = features
    colors = px.colors.qualitative.Plotly
    data = [go.Scatter(x=df[time], y=df[e], mode='lines', opacity=0.8, name=e, line={'width': 2},
                       marker={'color': colors[serie.index(e) % len(colors)]}) for e in serie]
    layout = go.Layout(
        xaxis=dict(
            titlefont=dict(size=12),
            color='#e6e6e6',
            gridwidth=0.5,
            gridcolor="#333",
            zerolinecolor="#333"
        ),
        yaxis=dict(
            title='Tracker Angle',
            titlefont=dict(size=12),
            color='#e6e6e6',
            gridwidth=0.5,
            gridcolor="#333",
            zerolinecolor="#333"
        ),
        legend=dict(font=dict(color='#e6e6e6')),
        plot_bgcolor='#282828',
        paper_bgcolor='#222222',
        margin=dict(l=50, r=50, t=30, b=10)
    )
    figure = go.Figure(data=data, layout=layout)

    return dict(msgTStrack=T('Tracker Angle Distribution'), figTStrack=figure.to_json())


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