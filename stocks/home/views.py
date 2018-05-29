from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

# Create your views here.
def index(request):
    template = loader.get_template('home/orange/index.html')
    context = {}
    return HttpResponse(template.render(context, request ))