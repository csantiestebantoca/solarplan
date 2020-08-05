import pandas as pd

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
    
    #return dictionary, dates, categories, features
    return data, dates, categories, features
