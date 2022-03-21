from unittest import result
from django.shortcuts import render

# Create your views here.
results = {'results': [
      {'name': 'Fatima Lopez', 'email': 'f.lopez@email.com'},
      {'name': 'Gary Johnston', 'email': 'g.johnston@email.com'}
    ]}

def index(request):
  if request.POST:
    context = {
      'name': request.POST['name'],
      'email': request.POST['email'],
    }
    # tmp = results.get('results')
    # tmp.append(context)
    # results.update({'results': tmp})
    return render(request, 'thanks.html', context)

  return render(request, 'index.html', results)
