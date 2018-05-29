from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import grapher.hritik as hk
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

# Create your views here.
def gp(request):
    canvas = hk.graph2()
    response=HttpResponse(content_type='image/png')
    canvas.print_png(response)
    #print(response)
    #return response
    return response

def index(request):
    template = loader.get_template('grapher/company.html')
    return HttpResponse(template.render())