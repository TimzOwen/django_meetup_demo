from django.shortcuts import render


# Create your views here.

def index(request):
    meetups = [
        {'title': 'Meet up 1', 'venue': 'ihub', 'slug': 'a-first-meetup'},
        {'title': 'meetup 2', 'venue': 'kabarak', 'slug': 'a-second-meetup'},
        {'title': 'meet up 3', 'venue': 'Juja', 'slug': 'a-third-meetup'}
    ]
    return render(request, 'meetups/index.html',
                  {'show_meetups': True,
                   'meetups': meetups})
