from django.shortcuts import render

# Create your views here.
def index(request):
    #items = Item.objects.filter(is_sold=False)
    #categories = Category.objects.all()
    return render(request, 'core/index.html')
