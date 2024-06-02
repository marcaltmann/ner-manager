import json
import spacy
from pathlib import Path
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.urls import reverse

from core.forms import UploadFileForm
from core.models import InputFile, NamedEntity

nlp = spacy.load("de_core_news_lg")


def do_ner(input_file: InputFile, transcript: list) -> None:
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


def entities_as_json(input_file: InputFile) -> str:
    entity_dict = dict()
    entities = input_file.namedentity_set.all()
    for entity in entities:
        if entity.label not in entity_dict:
            entity_dict[entity.label] = dict()
        if entity.name not in entity_dict[entity.label]:
            entity_dict[entity.label][entity.name] = list()
        tc = float(entity.timecode)
        entity_dict[entity.label][entity.name].append(tc)
    entity_json = json.dumps(entity_dict, indent=4, ensure_ascii=False)
    return entity_json


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
    file_list = get_list_or_404(InputFile)
    context = {"list": file_list}
    return render(request, "core/file_index.html", context)


def file_detail(request, pk):
    input_file = get_object_or_404(InputFile, pk=pk)
    context = {
        "file": input_file,
        "entities": input_file.namedentity_set.order_by("name", "timecode"),
    }
    return render(request, "core/file_detail.html", context)


def file_download(request, pk):
    input_file = get_object_or_404(InputFile, pk=pk)
    json_str = entities_as_json(input_file)
    response = HttpResponse(json_str, content_type="application/json")
    filename_stem = Path(input_file.name).stem
    filename = f"{filename_stem}_ner.json"
    response["Content-Disposition"] = f'attachment; filename="{filename}"'
    return response


def file_delete(request, pk):
    input_file = get_object_or_404(InputFile, pk=pk)
    input_file.delete()
    path = reverse('file_index')
    return HttpResponseRedirect(path)


def entity_delete(request, pk):
    entity = get_object_or_404(NamedEntity, pk=pk)
    file_id = entity.input_file.id
    entity.delete()
    path = reverse('file_detail', args=[file_id])
    return HttpResponseRedirect(path)
