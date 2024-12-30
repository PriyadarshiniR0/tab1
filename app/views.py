from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.
def insert_topic(request):
    tn=input('Enter topic name')
    Tod=Topic.objects.get_or_create(topic_name=tn)
    if Tod[1]:
      LTO=Topic.objects.all()
      d={'LTO':LTO}
      return render(request,'display_topics.html',d)

    else:
       return HttpResponse("Given Topic is already present")
    
def insert_Webpage(request):
   tn=input("Enter topicname")
   n=input("Enter name")
   url=input("Enter url")
   email=input("Enter the email")
   LTO=Topic.objects.filter(topic_name=tn)
   if LTO:
      WTOD=Webpage.objects.get_or_create(topic_name=LTO[0],name=n,url=url,email=email)
      if WTOD[1]:
         WTO=Webpage.objects.all()
         d={'WTO':WTO}
         return render(request,'display_Webpage.html',d)
      else:
         return HttpResponse('Webpage is present')
   else:
       return HttpResponse('Give parent topic table data is not present in db ')
   
def insert_AccessRecord(request):
      
      pk=int(input('enter pk of webpage'))
      author=input('enter author')
      date=input('enter date')
      LWO=Webpage.objects.filter(pk=pk)
      if LWO:
         WO=LWO[0]
         ATDO=AccessRecord.objects.get_or_create(name=WO,author=author,date=date)

         if ATDO[1]:
            ATO=AccessRecord.objects.all()
            d={'ATO':ATO}
            return render(request,'display_AccessRecord.html',d)
         else:
            return HttpResponse('with Given Details Access is Already Present')
      else:
         return HttpResponse('Given parent webpage table data is not present in database')
def display_topics(request):
   LTO=Topic.objects.all()
   d={'LTO':LTO}
   return render(request,'display_topics.html',d)

def display_Webpage(request):
   WTO=Webpage.objects.all()
   d={'WTO':WTO}
   return render(request,'display_Webpage.html',d)

def display_AccessRecord(request):
   ATO=AccessRecord.objects.all()
   d={'ATO':ATO}
   return render(request,'display_AccessRecord.html',d)
