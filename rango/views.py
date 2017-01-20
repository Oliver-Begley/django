from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    # Construct a dictionary to pass to the template engine as it's context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "Do or do not, there is no try."}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Not that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context = context_dict)


     # return HttpResponse("Rango says hey there partner! <br/> <a href='/rango/about/'> About page </a>")

def about(request):
    return HttpResponse("Rango says here is the about page, <br/> <a href='/rango/'> Index </a> ")