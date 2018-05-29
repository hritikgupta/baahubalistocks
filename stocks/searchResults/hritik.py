from mysql.connector import MySQLConnection, Error
# from python_mysql_dbconfig import read_db_config
import grapher.connect as connect
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter
 
# plots graph for stock of company over time
def graphOfChosenStockOverTime():
    # try:
    conn = connect.connector()
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM abbdaily")
    
    row = cursor.fetchone()

    # take time duration and return highest/lowest growth
    # top 10 stocks on a date 
    
    dates = []
    values  = []
    while row is not None:
        dates.append(row[0].strftime('%Y-%m-%d'))
        values.append(row[1])
        row = cursor.fetchone()
    #print (values)
    # print ((dates))
    plt.plot(dates, values)
    plt.xticks(['dfd'], [])
    #plt.show()
    canvas=FigureCanvas(plt)
    response=django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response

def graph2():
    conn = connect.connector()

    fig=Figure()
    ax=fig.add_subplot(111)

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM abbdaily")
    row = cursor.fetchone()
    dates = []
    values  = []
    while row is not None:
        dates.append(row[0].strftime('%Y-%m-%d'))
        values.append(row[1])
        row = cursor.fetchone()
    ax.plot(dates, values)
    #print (values) 
    # print ((dates))
    fig.autofmt_xdate()
    canvas=FigureCanvas(fig)
    
    return canvas

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

def printTop10(qu, allTables):
    date = input("Enter a date : ")
    date = datetime.strptime(date, "%Y-%m-%d").date() # <--- error here...how to convert string to datetime object???
    # date = datetime.strptime(date, '%Y-%m-%d')
    print (date)
    # qu += "where recordtime = " + date + ";"
    conn = connect.connector()
    cursor = conn.cursor()
    cursor.execute(qu)
    row = cursor.fetchone()
    print (row)
    # allTables = []
    # while row is not None:
        # allTables.append(row[0])
        # row = cursor.fetchone()
    # return allTables

 
if __name__ == '__main__':
    # graphOfChosenStockOverTime()
    
    allTables = retTableList()
    stmt = ""
    count = 0 #count is the index of stockName in the allTables list
    for i in allTables:
        stmt += "select recordtime, value, " + str(count) + " as `index`  from " + i + " union "
        count+=1

    stmt = stmt.rsplit(' ', 1)[0]
    stmt = stmt.rsplit(' ', 1)[0]

    stmt+= " order by value asc limit 10;"
    # print (stmt)
    # querTest(stmt, allTables)
    printTop10(stmt, allTables)