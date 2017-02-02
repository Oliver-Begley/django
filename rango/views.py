from django.shortcuts import render

from django.http import HttpResponse

#Import the category model
from rango.models import Category
#Import the page model
from rango.models import Page

def show_category(request, category_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExisst exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)

        # Retrieve all of the associated pages.
        # Note that filter() will return a list of page objects or an empty list
        pages = Page.objects.filter(category=category)

        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages

        # We also add the category object from
        # the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category

    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything -
        # the template will display the "no category" message for us.
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context_dict)

def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary
    # that will be passed to the template engine.

    category_list = Category.objects.order_by('-likes')[:5]
    pages_list = Page.objects.order_by('-views')[:5]

    # Construct a dictionary to pass to the template engine as it's context.
    context_dict = {'categories':category_list, 'pages':pages_list}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Not that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context = context_dict)

    # return HttpResponse("Rango says hey there partner! <br/> <a href='/rango/about/'> About page </a>")

def about(request):
    context_dict = {}
    return render(request, 'rango/about.html',context = context_dict)