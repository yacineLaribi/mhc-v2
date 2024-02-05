from django.shortcuts import render , redirect 
from .forms import NewItemForm , EditItemForm ,ItemSearchForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render ,get_object_or_404
from .models import Item , Category



# Create your views here.
def internships(request):
    categories=Category.objects.all()
    global_items=Item.objects.filter(is_active=True)
    items=Item.objects.filter(is_active=True)[0:12]
    search_form = ItemSearchForm(request.GET)
    if search_form.is_valid():
        search_query = search_form.cleaned_data['search_query']
        items = Item.objects.filter(is_active=True).filter(name__icontains=search_query)[0:12]


    return render(request,'internships.html',{
        'global_items':global_items,
        'items':items,
        'search_form': search_form ,
        'categories': categories ,
    })
    

@login_required
def new(request):

    if request.method=='POST':
        form = NewItemForm(request.POST,request.FILES)

        if form.is_valid():
            item=form.save(commit=False)
            item.created_by=request.user
            item.save()


            return redirect('browse')
    else:   

        form = NewItemForm()

    return render(request,'form.html',{
        'form':form,
        'title':'Add Internship',
    })



def delete(request,pk):
    item=get_object_or_404(Item,pk=pk,created_by=request.user)
    item.delete()

    return redirect('browse')




@login_required
def edit(request,pk):
    item=get_object_or_404(Item,pk=pk,created_by=request.user)

    if request.method=='POST':
        form = EditItemForm(request.POST,request.FILES,instance=item)

        if form.is_valid():
            form.save()          
            return redirect('profile')
    else:   
        form = EditItemForm(instance=item)


    return render(request,'form.html',{
        'form':form,
        'title':'Edit Internship',
    })

