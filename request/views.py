from django.shortcuts import render

# Create your views here.
def requestView(request,pk):

    return render(request,'request.html')