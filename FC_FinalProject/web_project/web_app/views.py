from django.shortcuts import render
from django.http.response import HttpResponse
from .models import User


def form(request):
    if request.method == "GET":
        return render(request, 'modernform.html')
    if request.method == "POST":
        name = request.POST['name']
        address = request.POST['address']
        phonenumber = request.POST['phonenumber']
        introducer = request.POST['introducer']
        age = request.POST['age']
        birthdate = request.POST['birthdate']
        height = request.POST['height']
        weight = request.POST['weight']
        explain = request.POST['explain']
        drug = request.POST['drug']
        visitdate = request.POST['visitdate']
        testresult = request.POST['testresult']
        prescription = request.POST['prescription']
        primarydiagnose = request.POST['primarydiagnose']
        needmorevisitdate = request.POST['needmorevisitdate']
        a = User.objects.create(name=name, address=address, phonenumber=phonenumber, introducer=introducer, age=age, birthdate=birthdate, height=height, weight=weight,
                                explain=explain, drug=drug, visitdate=visitdate, testresult=testresult, prescription=prescription, primarydiagnose=primarydiagnose, needmorevisitdate=needmorevisitdate)
        my_list = {'data': a}
        return render(request, 'modernform.html', context=my_list)


def form_2(request):
    b = User.objects.all()
    new_list = {'save_data': b}
    return render(request, 'result.html', context=new_list)

def home(request):
    return render(request , 'index.html')

def about(request):
    return render(request , '1.html')

def search(request):
    if request.method=="GET":
        return render(request , 'search.html')
    if request.method=="POST":
        name = request.POST['search']
        c=User.objects.filter(name__icontains=name)
        output={'search_data' : c}
        return render (request ,'find.html' , context=output)