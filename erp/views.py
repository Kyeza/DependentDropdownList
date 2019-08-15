from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView

from erp.models import Person


class PersonListView(ListView):
    model = Person
    context_object_name = 'people'


class PersonCreateView(CreateView):
    model = Person
    fields = ['name', 'birth_date', 'country', 'city']
    success_url = reverse_lazy('erp:person_changelist')


class PersonUpdateView(UpdateView):
    model = Person
    fields = ['name', 'birth_date', 'country', 'city']
    success_url = reverse_lazy('erp:person_changelist')
