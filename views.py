from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import MyModel
from .forms import MyModelForm

class IndexView(ListView):
    model = MyModel
    template_name = 'index.html'
    context_object_name = 'objects'

class MyModelDetailView(DetailView):
    model = MyModel
    template_name = 'detail.html'
    context_object_name = 'object'

class MyModelCreateView(CreateView):
    model = MyModel
    form_class = MyModelForm
    template_name = 'form.html'
    success_url = reverse_lazy('index')

class MyModelUpdateView(UpdateView):
    model = MyModel
    form_class = MyModelForm
    template_name = 'form.html'
    success_url = reverse_lazy('index')

class MyModelDeleteView(DeleteView):
    model = MyModel
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('index')

