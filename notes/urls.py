from django.urls import path
from notes.views import NoteListView, NoteDetailView, NoteCreateView, NoteUpdateView, NoteDeleteView

urlpatterns = [
    path('', NoteListView.as_view(), name='notes_list'),
    path('note/<int:pk>/', NoteDetailView.as_view(), name='notes_detail'),
    path('create/', NoteCreateView.as_view(), name='notes_create'),
    path('update/<int:pk>/', NoteUpdateView.as_view(), name='notes_update'),
    path('delete/<int:pk>/', NoteDeleteView.as_view(), name='notes_delete'),
]
