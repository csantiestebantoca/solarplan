from plotly import subplots
import plotly.graph_objs as go


def index():
    response.flash = T("Transformer analysis")

    return dict(message=T('Transformer analysis'))

