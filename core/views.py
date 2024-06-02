import json
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.urls import reverse

from core.forms import UploadFileForm
from core.models import InputFile, NamedEntity

import json
import time
import spacy


def do_ner(input_file: InputFile, transcript: list):
    nlp = spacy.load("de_core_news_lg")

    entities = list()
    for segment in transcript:
        doc = nlp(segment['text'])
        for ent in doc.ents:
            entity = NamedEntity(
                label=ent.label_,
                name=ent.text,
                timecode=segment['start'],
                segment=segment['text'],
                input_file=input_file,
            )
            entities.append(entity)

    NamedEntity.objects.bulk_create(entities)


def index(request):
    return render(request, "core/index.html")


def upload(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            content_str = file.read()
            content = json.loads(content_str)
            input_file = InputFile(name=file.name)
            input_file.save()
            do_ner(input_file, content)
            path = reverse('file_detail', args=[input_file.id])
            return HttpResponseRedirect(path)
        else:
            return HttpResponseRedirect('/')
    else:
        form = UploadFileForm()
        context = {"form": form}
        return render(request, "core/upload.html", context)


def file_index(request):
    list = get_list_or_404(InputFile)
    context = {"list": list}
    return render(request, "core/file_index.html", context)


def file_detail(request, pk):
    input_file = get_object_or_404(InputFile, pk=pk)
    context = {
        "file": input_file,
        "entities": input_file.namedentity_set.order_by("name", "timecode"),
    }
    return render(request, "core/file_detail.html", context)
