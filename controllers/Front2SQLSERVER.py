# antes de todo instalar el driver ocon SQL server pip install pyodbc
# los datos de autenticación so ejemplos. 
import pyodbc 
cnxn = pyodbc.connect('Driver={SQL Server};'
                                            'Server=WIN-D5UQ87OOFGJ;'
                                            'Database=BOUJDOUR;'
                                            'UID=Aruna;PWD=!mAH5H?kA7')
                      #'Trusted_Connection=yes;')
cursor = cnxn.cursor()
cursor.execute("exec SP_TestConexion 3, 3, 1")
con = cursor.fetchall()
# si el pedido tiene una sola tabla, se trabaja como una matriz como este ejemplo abajo 
# si el pedido tiene un arreglo de matrizes, entocnes llevará el tratamiento de que por cada nodo, se tiene el escenario del ejemplo
for d in con:
	print('timestamp = {} and [IR1_INV3ACT_PWR_VAL0]  = {}'.format(d[3],d[4]))