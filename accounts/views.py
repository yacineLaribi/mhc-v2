from django.shortcuts import render ,get_object_or_404
from core.models import CustomUser
# Create your views here.

def accounts(request,pk):
    user=get_object_or_404 (CustomUser,pk=pk)
    return render(request,'account.html',{
        'user':user,
    })