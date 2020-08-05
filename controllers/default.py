# -*- coding: utf-8 -*-

# import math
# import numpy as np
# import pandas as pd
# from os.path import dirname, join
# from plotly import subplots
# import plotly.express as px
# import plotly.graph_objs as go
# import operator
#
#
# # ---- Data ----
# def load_data(filename):
#     data = pd.read_csv(filename)
#     data['Datetime_x'] = pd.to_datetime(data['Datetime_x'])
#     data['Datetime_y'] = pd.to_datetime(data['Datetime_y'])
#     data['Time'] = pd.to_datetime(data['Time'])
#
#     cols = data.columns.tolist()
#     dictionary = {}
#     for elem in cols:
#         dictionary[elem] = data[elem]
#
#     dates = ['Datetime_x', 'Time', 'Datetime_y']
#     categories = ['Day', 'Backtracking']
#     features = [e for e in dictionary if (e not in dates) and (e not in categories)]
#
#     # return dictionary, dates, categories, features
#     return data, dates, categories, features
#
#
# filename1 = join(dirname(__file__), 'IR-1_INV1_combined.csv')
# filename2 = join(dirname(__file__), 'String_data.csv')
# df, dates, categories, features = load_data(filename1)


# ---- Pages ----
def index():
    response.flash = T("Dashboard")
    return dict(message=T('Dashboard'))
#
#
# def vacia():
#     msg = request.args(0)
#     response.flash = T(msg)
#     return dict(message=T(msg))
#
#
# def correlation():
#     response.flash = T("Correlation analysis")
#     times = [round(float(e.hour), 2) for e in df[dates[0]]]
#     if request.vars.scatddx:
#         scatddx = request.vars.scatddx
#     else:
#         scatddx = "Irradiance"
#     if request.vars.scatddy:
#         scatddy = request.vars.scatddy
#     else:
#         scatddy = "ACPower"
#     data = go.Scatter(
#         x=df[scatddx],
#         y=df[scatddy],
#         mode='markers',
#         opacity=0.8,
#         marker={
#             'size': 5,
#             'color': times,  # set color equal to a variable
#             'colorscale': 'Rainbow',  # one of plotly colorscales
#             'showscale': True,
#             'colorbar': dict(thickness=20, tickfont=dict(color='#e6e6e6'),
#                              title=dict(text='Hour', font=dict(color='#e6e6e6'))),
#         }
#     )
#     layout = go.Layout(
#         xaxis=dict(
#             title=scatddx,
#             titlefont=dict(
#                 size=12
#             ),
#             color='#e6e6e6',
#             gridwidth=0.5,
#             gridcolor="#333",
#             zerolinecolor="#333"
#         ),
#         yaxis=dict(
#             title=scatddy,
#             titlefont=dict(
#                 size=12
#             ),
#             color='#e6e6e6',
#             gridwidth=0.5,
#             gridcolor="#333",
#             zerolinecolor="#333"
#         ),
#         plot_bgcolor='#282828',
#         paper_bgcolor='#222222',
#         margin=dict(l=50, r=50, t=50, b=50),
#     )
#     figure = go.Figure(data=data, layout=layout)
#     return dict(message=T('Correlation analysis'), features=features, scatddx=scatddx, scatddy=scatddy,
#                 figure=figure.to_json())
#
#
# def category():
#     response.flash = T("Category frequency analysis")
#     if request.vars.selected_category:
#         selected_category = request.vars.selected_category
#     else:
#         selected_category = "Backtracking"
#     values = df[selected_category].value_counts()
#     # colors = px.colors.sequential.PuBuGn[4:7][::-1]
#     colors = px.colors.sequential.Viridis[2:8]
#     data = [go.Bar(x=list(values.index),
#                    y=list(values.values),
#                    opacity=0.8,
#                    width=np.ones(len(values)) * 0.4,
#                    marker={
#                        'color': list(values.values),
#                        'colorscale': colors,
#                        'line': dict(width=0),
#                    },
#                    ), ]
#     layout = go.Layout(
#         xaxis=dict(
#             categoryorder='category ascending',
#             title=selected_category,
#             titlefont=dict(
#                 size=12
#             ),
#             color='#e6e6e6',
#             gridwidth=0.5,
#             gridcolor="#333",
#             zerolinecolor="#333"
#         ),
#         yaxis=dict(
#             title='Count',
#             titlefont=dict(size=12),
#             color='#e6e6e6',
#             gridwidth=0.5,
#             gridcolor="#333",
#             zerolinecolor="#333"
#         ),
#         plot_bgcolor='#282828',
#         paper_bgcolor='#222222',
#         margin=dict(l=50, r=50, t=50, b=50),
#     )
#     figure = go.Figure(data=data, layout=layout)
#     return dict(message=T('Category frequency analysis'), categories=categories, selected_category=selected_category,
#                 figure=figure.to_json())
#
#
# def histogram():
#     response.flash = T("Histogram analysis")
#     if request.vars.hist:
#         hist = request.vars.hist
#     else:
#         hist = "GHI"
#     if request.vars.slide:
#         slide = int(request.vars.slide)
#     else:
#         slide = 5
#     size = slide * 0.01 * (max(df[hist]) - min(df[hist]))
#     intervals = [i * size for i in range(math.ceil((max(df[hist]) - min(df[hist])) / size) + 1)]
#     intervals.append(max(df[hist]))
#     counts = []
#     for i in range(len(intervals) - 1):
#         count = 0
#         for e in df[hist]:
#             if intervals[i] <= e < intervals[i + 1]:
#                 count += 1
#         counts.append(count)
#     counts[-1] += 1
#     data = [go.Bar(x=intervals[0:len(intervals)],
#                    y=counts,
#                    type='bar',
#                    opacity=0.8,
#                    marker={
#                        'color': counts,
#                        'colorscale': px.colors.sequential.Plasma[1:-1],
#                        'colorbar': dict(thickness=20, tickfont=dict(color='#e6e6e6'),
#                                         title=dict(text='Count', font=dict(color='#e6e6e6'))),
#                        'showscale': True,
#                        'line': dict(
#                            width=0
#                        ),
#                    },
#                    ), ]
#     layout = go.Layout(
#         xaxis=dict(
#             title=hist,
#             titlefont=dict(
#                 size=12
#             ),
#             color='#e6e6e6',
#             gridwidth=0.5,
#             gridcolor="#333",
#             zerolinecolor="#333"
#         ),
#         yaxis=dict(
#             title='Count',
#             titlefont=dict(
#                 size=12,
#             ),
#             color='#e6e6e6',
#             gridwidth=0.5,
#             gridcolor="#333",
#             zerolinecolor="#333"
#         ),
#         plot_bgcolor='#282828',
#         paper_bgcolor='#222222',
#         margin=dict(l=50, r=50, t=50, b=50),
#     )
#     figure = go.Figure(data=data, layout=layout)
#     return dict(message=T('Frequency Distribution Analysis'), features=features,
#                 hist=hist, slide=slide, figure=figure.to_json())
#
#
# def heatmap():
#     response.flash = T("Heatmap analysis")
#     if request.vars.station:
#         station = int(request.vars.station)
#     else:
#         station = 1
#     df1 = pd.read_csv(filename2)
#     xdf = [df1[df1['Station Number'] == station][df1['Inverter Number'] == i] for i in range(1, 5)]
#     figure = subplots.make_subplots(1, 4, subplot_titles=['INV ' + str(i) for i in range(1, 5)])
#     RdYlGn = px.colors.diverging.RdYlGn[:]
#     my_colors = [[0.0, RdYlGn[1]], [0.2, RdYlGn[1]],
#                  [0.2, RdYlGn[3]], [0.4, RdYlGn[3]],
#                  [0.4, RdYlGn[5]], [0.6, RdYlGn[5]],
#                  [0.6, RdYlGn[7]], [0.8, RdYlGn[7]],
#                  [0.8, RdYlGn[9]], [1.0, RdYlGn[9]]]
#     color_vals = np.round(np.linspace(np.min(df1['STD']), np.max(df1['STD']), 6), 2)
#     traces = [go.Heatmap(x=e['Combiner Number'],
#                          y=e['String Number'],
#                          z=e['STD'],
#                          opacity=0.8,
#                          colorscale=my_colors,
#                          colorbar=dict(thickness=15, tickfont=dict(size=12, color='#e6e6e6'),
#                                        title=dict(text='STD', font=dict(color='#e6e6e6')),
#                                        tickvals=color_vals),
#                          showscale=False,
#                          zmin=np.round(np.min(df1['STD']), 2),
#                          zmax=np.round(np.max(df1['STD']), 2)
#                          )
#               for e in xdf]
#     traces[-1]['showscale'] = True
#     figure.append_trace(traces[0], 1, 1)
#     figure.append_trace(traces[1], 1, 2)
#     figure.append_trace(traces[2], 1, 3)
#     figure.append_trace(traces[3], 1, 4)
#     layout = go.Layout(
#         title={'text': 'Station ' + str(station),
#                'font': {'color': '#e6e6e6'},
#                'y': 0.95,
#                'x': 0.5,
#                'xanchor': 'center',
#                'yanchor': 'top'
#                },
#         margin=dict(l=70, r=70, t=60, b=50),
#         plot_bgcolor='#282828',
#         paper_bgcolor='#222222',
#     )
#     figure['layout'].update(layout)
#     figure.update_xaxes(tickfont=dict(color='#e6e6e6'), showgrid=False)
#     figure.update_yaxes(tickfont=dict(color='#e6e6e6'), showgrid=False,
#                         tickvals=np.linspace(min(traces[0]['y']) + 1, max(traces[0]['y']), 8))
#     figure.update_yaxes(title=dict(text="Strings", font=dict(color='#e6e6e6')), row=1, col=1)
#     figure.add_annotation(dict(text="Combiner", xref="paper", yref="paper",
#                                showarrow=False, x=0.5, y=-0.13))
#     for annotation in figure['layout']['annotations']:
#         annotation['font'] = dict(color='#e6e6e6')
#     return dict(message=T('Heatmap analysis'), station=station, figure=figure.to_json())
#
#
# # ---- API (example) -----
# @auth.requires_login()
# def api_get_user_email():
#     if not request.env.request_method == 'GET': raise HTTP(403)
#     return response.json({'status': 'success', 'email': auth.user.email})
#
#
# # ---- Smart Grid (example) -----
# @auth.requires_membership('admin')  # can only be accessed by members of admin groupd
# def grid():
#     response.view = 'generic.html'  # use a generic view
#     tablename = request.args(0)
#     if not tablename in db.tables: raise HTTP(403)
#     grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
#     return dict(grid=grid)
#
#
# # ---- Embedded wiki (example) ----
# def wiki():
#     auth.wikimenu()  # add the wiki to the menu
#     return auth.wiki()
#
#
# # ---- Action for login/register/etc (required for auth) -----
# def user():
#     """
#     exposes:
#     http://..../[app]/default/user/login
#     http://..../[app]/default/user/logout
#     http://..../[app]/default/user/register
#     http://..../[app]/default/user/profile
#     http://..../[app]/default/user/retrieve_password
#     http://..../[app]/default/user/change_password
#     http://..../[app]/default/user/bulk_register
#     use @auth.requires_login()
#         @auth.requires_membership('group name')
#         @auth.requires_permission('read','table name',record_id)
#     to decorate functions that need access control
#     also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
#     """
#     return dict(form=auth())
#
#
# # ---- action to server uploaded static content (required) ---
# @cache.action()
# def download():
#     """
#     allows downloading of uploaded files
#     http://..../[app]/default/download/[filename]
#     """
#     return response.download(request, db)
