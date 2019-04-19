from django.shortcuts import redirect, render
from django.http import HttpResponse 
from lists.models import Item

def home_page(request):
    if request.method == 'POST':
        return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text', ''),
        })

    return render(request, 'home.html')

# def home_page(request):
#     if request.method == 'POST':
#         Item.objects.create(text=request.POST['item_text']) 
#         return redirect('/')

#     items = Item.objects.all()

#     return render(request, 'home.html', {'items': items})

