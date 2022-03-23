from django.shortcuts import render


# Create your views here.

def index(request):
    meetups = [
        {'title': 'Meet up 1'},
        {'title': 'meetup 2'}
    ]
    return render(request, 'meetups/index.html',
                  {'show_meetups': True,
                   'meetups': meetups})
