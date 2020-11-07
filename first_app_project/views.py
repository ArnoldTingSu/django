from django.shortcuts import render, HttpResponse

def index(request):
    print("a new user has entered the chat! Welcome!")
    return HttpResponse("This is my response!")

def new(request):
    print("making a new blog! welcome")
    return HttpResponse("This is where you maka a new blog!!")

def create(request):
    print("AHHHHHHHHHHHHH. YOU HAVE ENTERED THE CREATE PAGE!")
    return HttpResponse("Welcome to the create page!!")

def show(request, id):
    print(f"the id of this page is {id}")
    return HttpResponse(f"Welcome! The page id of this page is {id}")

def edit(request, id):
    print(f"currently editing page {id}.")
    return HttpResponse(f"this page is for editing blog:{id}")

def delete(request,id):
    print(f"currently deleting page {id}")
    return HttpResponse(f"Are you sure you want to delete page: {id}? Y/N?")