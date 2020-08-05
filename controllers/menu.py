import pyodbc

cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=87.200.229.44;'  # Public
                      # 'Server=192.168.10.111;'  # Local Network
                      'Database=BOUJDOUR;'
                      'UID=development;PWD=g]9XM5&=5^3PznA')
cursor = cnxn.cursor()


def index():
    return dict()


def children():
    cursor.execute("exec SP_MenuChildrenSheet 1, 1")
    data = [dict(zip([column[0] for column in cursor.description], row)) for row in cursor.fetchall()]
    return response.json(data)


def instances():
    sql = "exec SP_MenuInstancesBYSheet {}, {}"
    if len(request.args) == 3: sql += ", {}"
    cursor.execute(sql.format(*request.args))
    data = [dict(zip([column[0] for column in cursor.description], row)) for row in cursor.fetchall()]
    return response.json(data)


def variables():
    cursor.execute("exec SP_MenuVariablesBYSheet {}".format(*request.args))
    rows = cursor.fetchall()
    data = []
    for row in rows:
        data.append(row[0])
    return response.json(data)
