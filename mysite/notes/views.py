from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Notes
from .forms import NotesForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = 'notes'
    login_url = '/login'

    def get_queryset(self):
        return self.request.user.notes.all()

class NotesDetailView(LoginRequiredMixin, DetailView):
    model = Notes
    context_object_name = 'note'
    login_url = '/login'

    def get_queryset(self):
        return self.request.user.notes.all()

class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    form_class = NotesForm
    success_url = reverse_lazy('notes.list')
    login_url = '/login'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class NotesUpdateView(LoginRequiredMixin, UpdateView):
    model = Notes
    success_url = '/notes/'
    form_class = NotesForm
    login_url = '/login'

    def get_queryset(self):
        return self.request.user.notes.all()

class NotesDeleteView(LoginRequiredMixin, DeleteView):
    model = Notes
    success_url = '/notes/'
    template_name = 'notes/notes_delete.html'
    login_url = '/login'

    def get_queryset(self):
        return self.request.user.notes.all()


# Function-based list view for Notes (commented out)
# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})

# Function-based detail view for Notes (commented out)
# def detail(request, pk):
#     note = Notes.objects.get(pk=pk)
#     return render(request, 'notes/notes_detail.html', {'note': note})
