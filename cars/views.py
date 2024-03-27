from django.http import HttpResponse


def cars_view(request):
    return HttpResponse('Meus Carros 2')