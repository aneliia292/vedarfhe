from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.views import View
from .models import *
from .forms import *


def index(request):
    info = ToDo.objects.all()
    return render(request, 'app/index.html', context={'info': info})


def create(request):
    if request.method == 'POST':

        form = TodoModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'app/create.html', context={'form': TodoModelForm()})


def update(request, id):
    task = ToDo.objects.get(id=id)
    if request.method == 'POST':
        form = TodoModelForm(data=request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'app/create.html', context={'form': TodoUpdateModelForm(instance=task)})


def delete(request, id):
    task = get_object_or_404(ToDo, id=id)
    # task = ToDo.objects.get(id=id)
    task.delete()
    return redirect('home')

class BaseViewClosed(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/index.html', context={'info': ToDo.objects.all()})


class BaseViewCreate(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/create.html', context={'form': TodoModelForm()})

    def post(self, request, *args, **kwargs):
        form = TodoModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('getClass')
        return self.get(request, *args, **kwargs)


class BaseViewDetail(View):
    def get(self, request, pk, *args, **kwargs):
        task = get_object_or_404(ToDo, pk=pk)
        return render(request, 'app/index.html', context={'task': task})


class BaseViewUpdate(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/create.html', context={'form': TodoModelForm()})

    def post(self, pk, request, *args, **kwargs):
        task = ToDo.objects.get(pk=pk)
        form = TodoModelForm(data=request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('getClass')
        return self.get(request, pk, *args, **kwargs)


class BaseViewDelete(View):
    def get(self, request, pk, *args, **kwargs):
        task = get_object_or_404(ToDo, pk=pk)
        task.delete()
        return redirect('home')


# =================================================================

class List(ListView):
    model = ToDo


class Detail(DetailView):
    model = ToDo
    template_name = 'app/detail.html'



class CreateViewClass(CreateView):
    model = ToDo
    fields = "__all__"
    success_url = '/list'


class UpdateViewClass(UpdateView):
    model = ToDo
    fields = "__all__"
    success_url = '/list'


class DeleteViewClass(DeleteView):
    model = ToDo
    success_url = reverse_lazy('getList')
