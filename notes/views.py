from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from notes.models import NoteModel


# Create your views here.
class NoteListView(ListView):
    template_name = 'note_list.html'
    queryset = NoteModel.objects.all()


class NoteDetailView(DetailView):
    template_name = 'note_detail.html'
    model = NoteModel


class NoteCreateView(CreateView):
    template_name = 'note_create.html'
    model = NoteModel
    fields = ('title', 'description')
    success_url = '/'


class NoteUpdateView(UpdateView):
    template_name = 'note_update.html'
    model = NoteModel
    fields = ('title', 'description')
    success_url = '/'


class NoteDeleteView(DeleteView):
    template_name = 'note_delete.html'
    model = NoteModel
    success_url = '/'
