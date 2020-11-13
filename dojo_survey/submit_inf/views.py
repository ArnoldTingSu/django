from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')


def display(request):
    if request.method == 'POST':
        print(request.POST)
        context = {
            'name':request.POST['name'],
            'location':request.POST['location'],
            'language':request.POST['language'],
            'comments':request.POST['comments']
        }
        return render(request, 'display.html', context)
    else:
        return render(request, 'landing.html')