from openpyxl import load_workbook
from matplotlib import pyplot

wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data']

def getvalue(x): return x.value

list_x = list(map(getvalue, sheet['A'][1:]))
list_y = list(map(getvalue, sheet['C'][1:]))
list_z = list(map(getvalue, sheet['D'][1:]))

pyplot.plot(list_x, list_y, label="Tempreature")
pyplot.plot(list_x, list_z, label="Tempreature")
pyplot.show()