from django.shortcuts import render

TITLE = 'EasyRail'

# Create your views here.
def Home(req):
    return render(req, 'index.html', {'title': TITLE})