import searchResults.connectorSetup as connect
import datetime

conn = connect.connect()

def stockDailyData():
    cursor = conn.cursor()
    tableQuery = "SELECT * FROM tickerdata"
    cursor.execute(tableQuery)
    data = cursor.fetchall()
    #abc = [str(data[0]), str(data[1])]
    #print(data)
    #stockcode=[]
    #for d in data:
     #   stockcode.append(str(d[1]))
    return data

def getStockData():
    stocks = stockDailyData()
    cursor = conn.cursor()
    stockQuery = "SELECT value from %s WHERE recordtime = %s "
    today = datetime.datetime.today()
    today = today - datetime.timedelta(5)
    yesterday = today - datetime.timedelta(1)
    yesterday = yesterday.strftime('%Y-%m-%d')
    today = today.strftime('%Y-%m-%d')
    data = []

    for stock in stocks:
        queryData1 = (str(stock[1])+"daily", today)
        queryData2 = (str(stock[1])+"daily", yesterday)
        q1 = "SELECT value from " + (str(stock[1]) + "daily") + " WHERE recordtime = '{}'".format(today)
        q2 = "SELECT value from " + (str(stock[1]) + "daily") + " WHERE recordtime = '{}'".format(yesterday)
        #print(q1)
        cursor.execute(q1)
        val1 = cursor.fetchone()
        cursor.execute(q2)
        val2 = cursor.fetchone()
        val3 = 0
        if val2 and val1 :
            if float(val2[0]) > 0 and float(val1[0]):
                val3 = ((float(val1[0])-float(val2[0]))/float(val2[0]))*100
                val3 = val3 * 1.00
        abc = [val1, val2, val3]
        data.append(abc)
    return data