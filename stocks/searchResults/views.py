from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import searchResults.process as sp

# Create your views here.
def index(request):
    allData = sp.stockDailyData()
    moreData = sp.getStockData()
    #print(moreData)
    template = loader.get_template('searchResults/company.html')
    stockcode = []
    for data, vals in allData:
        #print(vals)
        stockcode.append(str(vals))
    print(stockcode)
    context = {
        'allData': zip(allData, moreData, stockcode),
    }
    #print(context)
    return HttpResponse(template.render(context, request))

def gp(request, stockcode):
    canvas = hk.graph2(stockcode)
    response=HttpResponse(content_type='image/png')
    canvas.print_png(response)
    #print(response)
    #return response
    return response

def i2(request, stockcode):
    print("amrendra")
    context={
        'stockcode':str(stockcode),
    }
    print('stock: '+stockcode)
    template = loader.get_template('searchresults/company2.html')
    return HttpResponse(template.render(context))