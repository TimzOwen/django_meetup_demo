from django.shortcuts import render


# Create your views here.

def index(request):
    meetups = [
        {'title': 'Meet up 1'},
        {'title': 'meetup 2'},
        {'title': 'meet up 3'}
    ]
    return render(request, 'meetups/index.html',
                  {'show_meetups': True,
                   'meetups': meetups})
