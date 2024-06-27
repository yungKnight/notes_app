from django.urls import path
from . import views

urlpatterns = [
	path('notes/', views.NotesListView.as_view(), name = "notes.list"),
	path('notes/<int:pk>', views.NotesDetailView.as_view(), name = "note.detail"),
	path('notes/<int:pk>/edit', views.NotesUpdateView.as_view(), name = "note.update"),
	path('notes/<int:pk>/delete', views.NotesDeleteView.as_view(), name = "note.delete"),
	path('notes/new', views.NotesCreateView.as_view(), name = "notes.new")
]