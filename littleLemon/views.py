from django.shortcuts import render, redirect




from .models import MenuItems

from .forms import MenuItemForm



def home(request):

    items = MenuItems.objects.all()

    context = {
        'title': 'Our Menu',
        'items': items,
    }

    return render(request, 'littlelemon/home.html', context=context)



def menu_detail(request, id):

    item = MenuItems.objects.get(id=id)
    context = {
        'title': 'Menu Details ',
        'item': item
    }
    return render(request, 'littlelemon/menu_detail.html', context=context)

def add_item(request):

    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('home')
            except:
                pass
    else:
        form = MenuItemForm()
    return render(request, 'littlelemon/add_item.html', {'form':form})
    

# Update a menu item 
def item_update(request, id):  
    item = MenuItems.objects.get(id=id)
    form = MenuItemForm(initial={'item': item.item, 'description': item.description, 'category': item.category})
    if request.method == "POST":  
        form = MenuItemForm(request.POST, instance=item)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('home')  
            except Exception as e: 
                pass    
    return render(request,'littlelemon/item_update.html',{'form':form})  
