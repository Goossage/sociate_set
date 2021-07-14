from django.urls import path
from .views import profile

app_name = 'user'

urlpatterns = [
    #path('register/', ),
    #path('login/', ),
    path('profile/', profile, name='profile')
]

