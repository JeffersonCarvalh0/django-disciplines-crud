# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from .models import Discipline
from .forms import DisciplineForm

def index(request):
    return render(request, 'index.html', {'itens': Discipline.objects.all()})

def add(request):
    template = 'add.html'
    context = {}

    form = DisciplineForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            item = form.save()
            item.url = 'show/%d' % (item.id)
            item.save()
            return redirect('/')

    context['form'] = form
    return render(request, template, context)

def show(request, id):
    return render(request, 'show.html', {'discipline': get_object_or_404(Discipline, pk=id)})

def edit(request, id):
    template = 'edit.html'
    context = {}

    context['discipline'] = get_object_or_404(Discipline, pk=id)
    context['form'] = DisciplineForm(request.POST or None, instance=context['discipline'])

    if context['form'].is_valid():
        context['form'].save()
        return redirect('/')

    return render(request, template, context)

def delete(request, id):
    pass
