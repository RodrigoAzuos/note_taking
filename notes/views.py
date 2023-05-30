from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from notes.models import Note
from notes.form import NoteForm

# Create your views here.

def index(request):
	notes = Note.objects.all()
	template = "index.html" 
	context = {
		"notes": notes
	}
	return render(request, template,context)

def create(request):
	form = NoteForm(request.POST or None)

	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse("index"))

	template = "new.html"
	context = {
		"form": form,
		"action": "Criar"
	}

	return render(request, template, context)

def update(request, note_id):

	note = Note.objects.get(pk=note_id)
	form = NoteForm(request.POST or None, instance=note)
	template = "new.html"

	if request.method == "POST" and form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse("index"))

	context = {
		"form": form,
		"action": "Editar"
	}

	return render(request, template, context)

def delete(request, note_id):
	note = Note.objects.get(pk=note_id)
	note.delete()
	return HttpResponseRedirect(reverse("index"))


