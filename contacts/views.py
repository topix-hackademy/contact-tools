from django.http import HttpResponse


def index(request):
    return HttpResponse("Control is an illusion")
