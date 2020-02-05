from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'home.html')

def home(request):
    string = u"wabawaba labda"
    TutorialList =  ["HTML", "CSS", "jQuery", "Python", "Django"]
    info_dict = {'site': u"病蟲害checkItOut", 'content': u"yyy"}
    numbers = map(str, range(100))
    return render(request, 'home.html',
                                 {'string':string,
                                  'TutorialList':TutorialList,
                                  'info_dict':info_dict,
                                  'numbers':numbers})



    
