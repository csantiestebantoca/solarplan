import plotly.graph_objs as go
import numpy as np
import plotly.express as px
import pandas as pd
from os.path import dirname, join


def index():
    msg = "Farms control"
    response.flash = T(msg)
    return dict(message=msg)
