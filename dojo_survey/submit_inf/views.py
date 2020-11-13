from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')


def display(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.POST['name'])
        request.session['name'] = request.POST['name']
        print(request.POST['location'])
        request.session['location'] = request.POST['location']
        print(request.POST['language'])
        request.session['language'] = request.POST['language']
        print(request.POST['comments'])
        request.session['comments'] = request.POST['comments']
        
        context = {
            'name':request.POST['name'],
            'location':request.POST['location'],
            'language':request.POST['language'],
            'comments':request.POST['comments']
        }
        return render(request, 'display.html', context)
    else:
        return render(request, 'landing.html')