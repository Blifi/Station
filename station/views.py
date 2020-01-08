from django.shortcuts import render
from station.forms import StationForm 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from station.models import Station

@api_view(['GET', 'POST'])
def station(request):
    
    if request.method == "POST":
        form = StationForm(request.data)
        form.is_valid()
        form = StationForm(request.data)
        #breakpoint()
        if form.is_valid:
            try:  
                form.save()
                return redirect('/show')  
            except:  
                pass
    else:  
        form = StationForm()  
    return render(request,'index.html',{'form':form})  
    
def data(request):  
  station = Station.objects.order_by('-id')  
  return render(request,"data.html",{'station':station})  
  
def datashow(request):
    station = Station.objects.last()
    return render(request,"datashow.html",{'station':station})  