import os
from django.http import HttpResponse
from .settings import BASE_DIR
from .settings import FilePath

def show(request):
    #this print exactly the path of this document in the file system
    #return HttpResponse('algumas coisa: ' + str(__file__))
    #string =         #" ".join('BASE_DIR: ' + str(BASE_DIR) + " \n  portfolio.py: " + str(__file__))
    return HttpResponse( FilePath )