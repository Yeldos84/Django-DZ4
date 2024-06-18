from django.shortcuts import render, HttpResponseRedirect, HttpResponse

# Create your views here.
def zoo(request):
    return HttpResponse("This is ZOO page")