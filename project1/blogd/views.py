from django.http import HttpResponse
from django.template import loader

def blogd(request):
  template = loader.get_template('blogd.html')
  return HttpResponse(template.render())
