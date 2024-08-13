import random
import string

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import URLForm
from .models import Url_model


def main_app(request):
    if request.method == "POST":
        urlform = URLForm(request.POST)
        if urlform.is_valid():
            domain = request.META["HTTP_HOST"]
            short_url = read_db(urlform.cleaned_data["input_url"])
            short_url = f"{domain}/{short_url}"
            return render(request, 'main_app/main_app.html', {"urlform": urlform, "short_url": short_url})
    else:
        urlform = URLForm()
        return render(request, 'main_app/main_app.html', {"urlform": urlform})


def create_db(input_url):
    characters = string.ascii_letters + string.digits
    while True:
        short_url = ''.join(random.choice(characters) for _ in range(6))
        short_url = f"{short_url}"
        if not Url_model.objects.filter(short_url = short_url).exists():
            break
        
    url_model = Url_model()
    url_model.long_url = input_url
    url_model.short_url = short_url
    url_model.save()
    
    return short_url
    

def read_db(input_url):
    record = Url_model.objects.filter(long_url = input_url).exists()
    if record:
        short_url = Url_model.objects.filter(long_url = input_url).first().short_url
    else:
        short_url = create_db(input_url)
    
    return short_url


def redirection(request, short_url):
    long_url = Url_model.objects.filter(short_url = short_url).all()
    if len(long_url) != 0:
        return redirect(long_url.first().long_url)
    else:
        return redirect("main_app")