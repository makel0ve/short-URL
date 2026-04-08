import random
import string

from django.shortcuts import render, redirect

from .forms import URLForm
from .models import Url_model


def main_app(request):
    if request.method == "POST":
        urlform = URLForm(request.POST)
        if urlform.is_valid():
            domain = request.META["HTTP_HOST"]
            short_url = get_or_create_short_url(urlform.cleaned_data["input_url"])
            short_url = f"{domain}/{short_url}"
            return render(request, 'main_app/main_app.html', {"urlform": urlform, "short_url": short_url})
    else:
        urlform = URLForm()

    return render(request, 'main_app/main_app.html', {"urlform": urlform})


def create_short_url(input_url):
    characters = string.ascii_letters + string.digits
    while True:
        short_url = ''.join(random.choice(characters) for _ in range(6))
        if not Url_model.objects.filter(short_url=short_url).exists():
            break

    url_model = Url_model(long_url=input_url, short_url=short_url)
    url_model.save()

    return short_url


def get_or_create_short_url(input_url):
    record = Url_model.objects.filter(long_url=input_url).first()
    if record:
        return record.short_url

    return create_short_url(input_url)


def redirection(request, short_url):
    record = Url_model.objects.filter(short_url=short_url).first()
    if record:
        return redirect(record.long_url)

    return redirect("main_app")