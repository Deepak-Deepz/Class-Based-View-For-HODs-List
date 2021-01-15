from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from myApp.models import HOD
# Create your views here.
class HODListView(ListView):
    model = HOD
    #default template = hod_list.html
    #default context  = hod_list
class HODDetailView(DetailView):
    model = HOD
    #default template = hod_Detail.html
    #default context  = hod
class HODCreateView(CreateView):
    model = HOD
    fields =('name','no','exp','sal','dept')
    #default template = hod_form.html
class HODUpadteView(UpdateView):
    model = HOD
    fields = ('name','sal')
    #default template = hod_form.html
class HODDeleteView(DeleteView):
    model = HOD
    success_url = reverse_lazy('hods')
    #default template = hod_confirm_delete.html
