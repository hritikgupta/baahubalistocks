from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import searchResults.process as sp

# Create your views here.
def index(request):
    template = loader.get_template('top3/company.html')
    context = {
        'allData': zip(allData, moreData, stockcode),
    }
    #print(context)
    return HttpResponse(template.render(context))