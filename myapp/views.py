from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .forms import *

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

def myimagepage2(request):
    return render(request,'imagepage2.html')

def myimagepage3(request):
    return render(request,'imagepage3.html')

def myimagepage4(request):
    return render(request,'imagepage4.html')

def myimagepage5(request,imagename):
    myimagename = str(imagename);
    myimagename = myimagename.lower();
    print(myimagename)
    if myimagename == "django":
        var=True
    elif myimagename == "python":
        var=False
    mydictionary ={
        "var":var
    }
    return render(request,'imagepage5.html',context=mydictionary)

def myform(request):
    return render(request,'myform.html')

def submitmyform(request):
    mydictionary ={
        "var1" : request.POST['mytext'],
        "var2" : request.POST['mytextarea'],
        "method" : request.method
    }
    return JsonResponse(mydictionary)

def myform2(request):
    if request.method == "POST":
        form = feedbackForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            subject = request.POST['subject']
            email = request.POST['email'] 
            mydictionary = {
                "form" : feedbackForm()
            }
            errorflag = False
            Errors = []
            if title != title.upper():
                errorflag = True
                errormsg = "Title should be Capital"
                Errors.append(errormsg)
            import re
            regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
            if not re.search(regex,email):
                errorflag = True
                errormsg = "Not a valid Email address"
                Errors.append(errormsg)
            if errorflag != True:
                mydictionary["success"] = True
                mydictionary["successmsg"] = "Form Submitted"
            mydictionary["error"] = errorflag
            mydictionary["errors"] = Errors
            print(mydictionary)
            return render(request,'myform2.html',context=mydictionary)
            #print(title)
            #print(subject)
            #var = ("form Submitted " + str(request.method))
            #return HttpResponse(var)
        else:
            mydictionary = {
                "form" : form
            }
            return render(request,'myform2.html',context=mydictionary)      
    elif request.method == "GET":
        form = feedbackForm() # FeedbackForm(None)
        mydictionary = {
           "form" : form 
        }
        return render(request,'myform2.html',context=mydictionary)