from mysql.connector import MySQLConnection, Error
import connect
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def retTableList():
    conn = connect.connector()
    cursor = conn.cursor()
    cursor.execute("show tables")
    row = cursor.fetchone()
    allTables = []
    while row is not None:
        allTables.append(row[0])
        row = cursor.fetchone()
    return allTables

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

# plots graph for stock of company over time
def graphOfChosenStockOverTime():
    # try:
    conn = connect.connector()
    
    cursor = conn.cursor()

    names = retTableList()
    for nam in names:    
        cursor.execute("SELECT * FROM " + nam)
        
        row = cursor.fetchone()

        dates = []
        values  = []
        while row is not None:
            dates.append(row[0].strftime('%Y-%m-%d'))
            values.append(row[1])
            row = cursor.fetchone()

        # dates = dates.loc[:, 3].apply(lambda x: x.toordinal())

        X = []
        for i in dates:
            X.append(days_between(i, dates[0]))
        
        model = linregress(X,values) #x and y are arrays or lists.
        slope, intercept = model.slope, model.intercept
        
        print ("\nPredictions for upcoming 5 days for " + nam +":" )
        new_x = [143, 144, 145, 146, 147]
        predictions = []
        for i in new_x:      
            predict = slope*i + intercept
            predictions.append(predict)
        return predictions

if __name__ == '__main__':
    graphOfChosenStockOverTime()
    