from django.http import HttpResponse
from django.shortcuts import render
from django  import template

# def index(request):
#     return render(request, "home/index.html")
    # return HttpResponse("Hello, User!")
    

# def index(request, name):
#     now= datetime.datetime.now()
#     return render(request, "home/index.html", {
#         "name": name.capitalize(),
#         "date": now.month == 8 and now.day == 9,
#     })

loop_times = range(1, 8)
z=["z","zz","sss","ddd","f","f","f","f","f","f","f"]

a=zip(loop_times, z)
a=loop_times


def index(request):

    return render(request, "home/ContentUnitConvertion.html")

def index1(request):

    return render(request, "home/ContentHome.html", { "loop_times" : loop_times, "z" : z, "a" : a  })

def index2(request):
    
    return render(request, "home/reusable.html")