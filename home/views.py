from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#     return render(request, "home/index.html")
    # return HttpResponse("Hello, User!")
    

# def index(request, name):
#     now= datetime.datetime.now()
#     return render(request, "home/index.html", {
#         "name": name.capitalize(),
#         "date": now.month == 8 and now.day == 9,
#     })

def index(request):

    return render(request, "home/index.html")

def index1(request):
    
    return render(request, "home/reusable.html")