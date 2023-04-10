from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def myfunctioncall(request):
    return HttpResponse("Hello World")

def myfunctionabout(request):
    return HttpResponse("About Response")

def add(request,a,b):
    return HttpResponse(a+b)

def intro(request,name,age):
    mydictionary = {
        "name" : name,
        "age" : age
        }
    return JsonResponse(mydictionary)

def page(request):
    return render(request,'index.html')

def second(request):
    return render(request,'second.html')

def third(request):
    var = "hello world"
    greeting = "Hey! How are you"
    fruits = ["apple","Mango","Banana"]
    num1 , num2 = 10 , 7
    ans = num1 > num2
    print(ans)
    mydictionary = {
        "var" : var,
        "msg" : greeting,
        "myfruits" : fruits,
        "num1" : num1,
        "num2" : num2,
        "ans" : ans
    }
    return render(request,'third.html',context=mydictionary)

def myimagepage(request):
    return render(request,'imagepage.html')
