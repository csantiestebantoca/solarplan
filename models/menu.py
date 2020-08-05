# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    (T('Dashboard'), False, URL('default', 'index'), [])
]

# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. you can remove everything below in production
# ----------------------------------------------------------------------------------------------------------------------

if not configuration.get('app.production'):
    _app = request.application
    response.menu += [
        (T('Performance analysis'), False, '', [
            (T('Mega reporte'), False, URL('default', 'megaReporte'))
        ]),
        (T('Alarm management'), False, '', [
            (T('Alarms'), False, URL('default', 'category')),
            (T('Pareto diagram'), False, URL('default', 'pareto'))
        ]),
        (T('String performance analysis'), False, URL('default', 'heatmap')),
        (T('Tracker analysis'), False, '', [
            (T('Time series'), False, URL('timeSeries', 'index')),
            (T('Heatmap 1..4'), False, URL('default', 'heatmap')),
            (T('Table'), False, URL('default', 'table')),
        ]),
        (T('Real time values'), False, '', [
            (T('Timer'), False, URL('default', 'category')),
            (T('Heatmap'), False, URL('default', 'histogram')),
        ]),
        (T('Reports'), False, '', [
            (T('Upload data'), False, URL('default', 'category')),
        ]),
        (T('Field analysis'), False, '', [
            (T('Transformer analysis'), False, URL('default', 'fielData')),
            (T('IV Tracing analysis'), False, URL('default', 'histogram')),
        ]),
        (T('Advanced analysis'), False, '', [
            (T('Time series'), False, URL('timeSeries', 'index')),
            (T('Correlation analysis'), False, URL('default', 'correlation')),
            (T('Category analysis'), False, URL('default', 'category')),
            (T('Histogram analysis'), False, URL('default', 'histogram')),
            (T('Heatmap analysis'), False, URL('default', 'heatmap')),
            (T('Field data analysis'), False, URL('default', 'fielData'))
        ]),
    ]
