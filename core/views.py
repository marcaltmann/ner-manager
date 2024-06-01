import json
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render

from core.forms import UploadFileForm


def index(request):
    return render(request, "core/index.html")


def upload(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            content_str = file.read()
            content = json.loads(content_str)
            return JsonResponse(content)
            # return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
    else:
        form = UploadFileForm()
        context = {"form": form}
        return render(request, "core/upload.html", context)
