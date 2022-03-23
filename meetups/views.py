from django.shortcuts import render


# Create your views here.

def index(request):
    meetups = [
        {
            'title': 'Meet up 1',
            'venue': 'Ihub',
            'slug': 'a-first-meetup'
        },
        {
            'title': 'meetup 2',
            'venue': 'Kabarak',
            'slug': 'a-second-meetup'
        },
        {
            'title': 'meet up 3',
            'venue': 'Juja',
            'slug': 'a-third-meetup'
        }
    ]
    return render(request, 'meetups/index.html',
                  {'show_meetups': True,
                   'meetups': meetups})


def meetup_details(request, meetup_slug):
    print(meetup_slug)
    selected_meetup = {
            'title': 'First Meet up',
            'description': 'This is the meet up led by Timz owen'
        }

    return render(request, '/meetups/meetup-details.html', {
        'meetup_title': selected_meetup['title'],
        'meetup-description': selected_meetup['description']
    })
