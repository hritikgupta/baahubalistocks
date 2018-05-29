from mysql.connector import MySQLConnection, Error
import result.connect as connect
import datetime
# import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

def days_between(d1, d2):
    d1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

def graphOfChosenStockOverTime():
    conn = connect.connector()
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM abbdaily")
    
    row = cursor.fetchone()

    dates = []
    values  = []
    while row is not None:
        dates.append(row[0].strftime('%Y-%m-%d'))
        values.append(row[1])
        row = cursor.fetchone()
    # print (values)
    plt.plot(dates, values)
    plt.xticks([], [])
    plt.show()


def searchTag(searchedTag):
    conn = connect.connector()
    
    # daily analysis restricted to 7 days
    cursor = conn.cursor()
    daily = searchedTag + "daily"
    monthly =  searchedTag + "monthly"
    cursor.execute("SELECT * FROM " + daily + " order by recordtime desc limit 7")
    
    row = cursor.fetchone()
    dates_dail = []
    values_dail  = []
    while row is not None:
        dates_dail.append(row[0].strftime('%Y-%m-%d'))
        values_dail.append(row[1])
        row = cursor.fetchone()
    
    # monthly analysis
    cursor.execute("SELECT * FROM " +  monthly)
    fig=Figure()
    ax=fig.add_subplot(111)
    row = cursor.fetchone()
    dates_mon = []
    values_mon  = []
    while row is not None:
        dates_mon.append(row[0].strftime('%Y-%m-%d'))
        values_mon.append(row[1])
        row = cursor.fetchone()
    
    ax.plot(dates_mon, values_mon)
    #print (values) 
    # print ((dates))
    fig.autofmt_xdate()
    canvas=FigureCanvas(fig)
    # plt.show()


    # prediction part----------

    cursor.execute("SELECT * FROM " + daily)
    
    row = cursor.fetchone()

    dates = []
    values  = []
    while row is not None:
        dates.append(row[0].strftime('%Y-%m-%d'))
        values.append(row[1])
        row = cursor.fetchone()

    X = []
    for i in dates:
        X.append(days_between(i, dates[0]))
    
    model = linregress(X,values) #x and y are arrays or lists.
    slope, intercept = model.slope, model.intercept
    
    new_x = [143, 144, 145, 146, 147]
    
    
    predictions = []
    for i in new_x:      
        predictions.append(slope*i + intercept)

    return dates_dail, values_dail, canvas, predictions