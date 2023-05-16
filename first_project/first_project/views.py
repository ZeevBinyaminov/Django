from django.http import HttpResponse
from django.shortcuts import render

import datetime


def home(request):
    date = datetime.datetime.now().date()
    time = datetime.datetime.now().time()
    name = 'Dave'
    _context = {'date': date, 'time': time, 'name': name}
    return render(request, "index.html", _context)
