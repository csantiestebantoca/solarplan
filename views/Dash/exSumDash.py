import flask
import dash
import dash_table
import pandas as pd
import dash_html_components as html


server = flask.Flask(__name__)


def dashTable():
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')
    dt = dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        row_selectable="multi",
        row_deletable=True,
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        style_header={'backgroundColor': 'rgb(30, 30, 30)'},
        style_cell={
            'backgroundColor': 'rgb(50, 50, 50)',
            'color': 'white'
        },
    )
    div = html.Div(
        [dt]
    )
    return div


@server.route('/')
def index():
    return 'Dash App'


app = dash.Dash(
    __name__,
    server=server,
    routes_pathname_prefix='/dash/exSumDash/'
)


app.layout = dashTable()


if __name__ == '__main__':
    app.run_server(debug=False)

