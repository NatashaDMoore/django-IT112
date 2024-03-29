from django.shortcuts import render
from django.views import View

from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse

# Gets data from server and feeds back thru my javascript
from django.http import JsonResponse
# Imports function load_default_data from default_data.py
# . means current directory and the .py is assumed
from .default_data import load_default_data

from django.views.generic import ListView
from django.urls import reverse_lazy

from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from .models import Invention, Category
from .forms import InventionForm


# CLASS FROM WHICH ALL CLASS BASED VIEWS INHERIT
# Allows for different themes to be applied
class BaseView(TemplateView):
  default_title = 'My Website'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context.setdefault('title', self.default_title)
    return context


# HOME VIEW
class Home(BaseView):
  template_name = 'bootswatch.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context.update({
        'title': 'Home',
        'page_heading': 'Welcome to the Class-Based View',
        'page_content':
        'This is the content generated by the class-based view',
        'image_url': '/static/images/django_logo.png',
        'alt_text': 'django logo',
    })
    return context


# ABOUT VIEW
class About(View):

  def get(self, request):
    context = {
        'page_title':
        'About Page',
        'page_heading':
        'Welcome to the About page',
        'page_content':
        'This is the content generated by the class-based view.',
        'image_url':
        '/static/images/person_pic.png',
        'alt_text':
        'a computer generated photo of a person in a coffe shop working at a computer',
    }
    return render(request, 'bootswatch.html', context)


# LLAMAS VIEW
class Llamas(View):

  def get(self, request):
    context = {
        'page_title': 'Llama Page',
        'page_heading': 'Welcome to the Llama page',
        'page_content':
        'This is the content generated by the class-based view.',
        'image_url': '/static/images/llama_pic.png',
        'alt_text': 'a computer generated photo of a llama wearing glasses',
    }
    return render(request, 'bootswatch.html', context)


# CATS VIEW
class Cats(View):

  def get(self, request):
    context = {
        'page_title': 'Cat Page',
        'page_heading': 'Welcome to the Cats page',
        'page_content':
        'This is the content generated by the class-based view.',
        'image_url': '/static/images/cat_pic.png',
        'alt_text': 'a computer generated photo of a cat in a library',
    }
    return render(request, 'bootswatch.html', context)


# INVENTION VIEW
class InventionDetailView(DetailView):
  model = Invention
  template_name = 'invention_view.html'
  context_object_name = 'invention'


# View to change the Bootswatch theme applied to the site
class ThemeView(BaseView):
  template_name = 'theme.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    # Add additional context data if needed
    return context

  def post(self, request, *args, **kwargs):
    theme = request.POST.get('theme')
    response = HttpResponseRedirect(reverse('theme'))
    response.set_cookie('theme', theme)
    return response


#  Function based view that loads default data on click
def load_default_data_view(request):
  load_default_data()  # Call the load_default_data function
  return JsonResponse({'status': 'success'})


class InventionListView(ListView):
  model = Invention
  template_name = 'invention_list.html'
  context_object_name = 'inventions'


class InventionCreateView(CreateView):
  model = Invention
  form_class = InventionForm
  template_name = 'create_invention.html'
  success_url = reverse_lazy('invention-list')


class InventionUpdateView(UpdateView):
  model = Invention
  form_class = InventionForm
  template_name = 'update_invention.html'
  success_url = reverse_lazy('invention-list')


class InventionDeleteView(DeleteView):
  model = Invention
  success_url = reverse_lazy('invention-list')
