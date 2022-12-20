from django.shortcuts import render,HttpResponse
from .models import AccessRecord
from .models import Webpage


# Create your views here.
def index(request):
    return render(request,'index_1.html')


def home(request):
    return render(request,'home.html')

def contact(request):
    dict1={'name':'John','age':45}
    return render(request,'contact.html',context=dict1)


def webpage(request):
    webpage_list=AccessRecord.objects.order_by('date')
    dict1={'access_record':webpage_list}
    return render(request,'webpage.html',context=dict1)



def url(request):
    website=Webpage.objects.order_by('url')
    dict2={'website':website}
    return render(request,'url.html',context=dict2)





