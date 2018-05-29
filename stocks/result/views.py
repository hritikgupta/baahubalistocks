from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import result.search as rs
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

# Create your views here.
def index(request):
    tag = request.POST.get('tag')
    dates_dail, values_dail,canvas,  prediction = rs.searchTag(tag)
    
    #print(dates_dail)
    print("values")
    #print(values_dail)
    abc=[]
    temp = len(dates_dail)
    # for i in range(temp):
    #     abc.append(dates_dail[i], values_dail[i])

    for i in zip(dates_dail, values_dail):
        abc.append(i)
    

    template = loader.get_template('result/company.html')
    context = {
        'values': abc,
        'tag': tag,
        'prediction':  prediction,
    }
    #print(context)
    return HttpResponse(template.render(context))

def gr(request):
    tag = request.GET.get('tag')
    dates_dail, values_dail, canvas, pred = rs.searchTag(tag)
    print(tag)
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response
