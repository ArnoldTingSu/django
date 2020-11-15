from django.shortcuts import render, redirect

languages = (
    'Python',
    'SQL',
    'MERN',
    'Java',
    'Ruby'
)

locations = (
    'Costa Mesa',
    'Los Angeles',
    'Irvine',
    'San Francisco',
    'Burbank'
)

def index(request):
    context = {
            'languages': languages,
            'locations': locations
        }
    return render(request, 'index.html', context)


def form(request):
    if request.method == 'POST':
        print(request.POST)
        request.session['result'] = {
            'name':request.POST['name'],
            'location':request.POST['location'],
            'language':request.POST['language'],
            'comment':request.POST['comments']
        }
        return redirect('/results')
    else:
        return redirect('/')

def results(request):
    context = {
        'result': request.session['result']
    }
    return render(request,'display.html', context)
