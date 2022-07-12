from django.urls import path
from .views import *

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('register/',registeruser ,name='register'),
    path('document/', document_input, name='document'),
    path('profile/', profile, name='profile'),
    path('profile_info/<int:id>', profile_info, name='profile_info'),

]
