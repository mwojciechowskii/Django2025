import random
from django.utils.http import content_disposition_header
import requests

from django.shortcuts import render
from django.template import context


# Create your views here.
def home_view(request):
    context = {
        'your_number': random.randint(1, 10),
        'bool_item': True,
        'some_list': [
            random.randint(1, 10),
            random.randint(1, 10),
            random.randint(1, 10),
        ],
        'some_dict': {'A': 1, 'B': 2, 'C': 3}
    }
    return render(request, 'myapp/index.html', context)


def contact_view(request):
    return render(request, 'myapp/contact.html')

def aboutView(request):
    mytech = [
        {
          'name': 'HTML',
          'url': 'https://www.w3schools.com/html/',
          'level': 'beginner'
        },
        {
          'name': 'CSS',
          'url': 'https://www.w3schools.com/css/',
          'level': 'beginner'
        },
        {
          'name': 'Bootstrap',
          'url': 'https://getbootstrap.com',
          'level': 'beginner'
        },
        {
          'name': 'Python',
          'url': 'https://www.python.org',
          'level': 'intermediate'
        },
        {
          'name': 'Django',
          'url': 'https://www.djangoproject.com',
          'level': 'beginner'      
        },    
    ]
    context = {'luckyNumber': random.randint(1,10),
               'unluckyNumber': random.randint(1,10),
               'mytech': mytech}
    return render(request, 'myapp/about.html', context)

def genbankView(request):

    response = requests.get('https://ftp.ncbi.nlm.nih.gov/genbank/README.genbank')
    content = response.text

    #bez tego lsp krzyczy mi blad, bo pyright chcialby znac typy, ignore
    version: str | None = None
    date: str | None = None

    for line in content.split('\n'):
        if 'GenBank Flat File Release' in line:
            version = line
        if 'Release Availability Date' in line:
            date = line
        if version and date:
            break

    context = {'version': version,
               'date': date}
    return render(request, 'myapp/genbank.html', context)

