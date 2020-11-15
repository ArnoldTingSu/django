from django.urls import path, include           # import include

urlpatterns = [
   # path('', include('first_app_project.urls')),
   path('', include('random_word.urls'))
]