from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Cat
from .forms import CatForm

def index(request):
    cats = Cat.objects.all()
    form = CatForm()
    print('current user is', request.user)
    return render(request, 'index.html', {'cats': cats, 'form': form, 'user_loggedin': not request.user.is_anonymous})

def show(request, cat_id):
    cat = None
    try:
        cat = Cat.objects.get(id=cat_id)
    except:
        pass

    return render(request, 'show.html', {'cat': cat})

def post_cat(request):
    form = CatForm(request.POST)
    if form.is_valid() and request.user:
        cat = form.save(commit = False)
        cat.user = request.user
        cat.save()
    else:
        print('FORM WAS NOT VALID!')

    return HttpResponseRedirect('/')
