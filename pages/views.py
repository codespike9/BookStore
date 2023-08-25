from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("<h1>Hello world</h1>")
    return render(request, 'pages/index.html')
def aboutus(request):
    name="Dharmaraj"
    student={1:"Dharmaraj",2:"Jane",3:"blake",4:"kriti"}
    results={
        1: {"name":"John","cgpa":[9.2,9.8,9,7]},
        2: {"name":"Jane","cgpa":[9.2,9.8,9,7]},
        3: {"name":"Sam","cgpa":[9.2,9.8,9,7]},
        4: {"name":"Will","cgpa":[9.2,9.8,9,7]}
    }
    context={
        "name":"DJ",
        "age":19,
        "num1":8,
        "num2":10,
        "list1":[1,2,3,4],
        "students":student,
        "results":results
    }
    return render(request, 'pages/aboutus.html',context)