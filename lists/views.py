from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from lists.models import Item

def home_page(request):
    if request.method=='POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)
        return HttpResponseRedirect(redirect_to='/lists/the-only-list-in-the-world/')
    return render(request,'home.html')

def view_list(request):
    items = Item.objects.all()
    return render(request,'list.html',{'items':items}) 
