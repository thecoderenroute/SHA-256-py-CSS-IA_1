from django.shortcuts import render
from django.http import HttpResponse

from .forms import textForm

from.hash.hash import sha256


def index(request):

    if request.method == 'POST':

        form = textForm(request.POST)

        if form.is_valid():

            data = form.cleaned_data['text']

            result = sha256(data)

            print(f"data: {data}")

            return render(request, "index.html", {"form": form, "result": result, "data": data})

    temp_form = textForm()
    return render(request, "index.html", {"form": temp_form, "result": ""})
