from django.urls import path
from .views import home,registeruser,document_input,profile,UpdateDocumentView

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('register/',registeruser ,name='register'),
    path('document/', document_input, name='document'),
    path('profile/', profile, name='profile'),
    path('document/edit/<int:pk>', UpdateDocumentView, name='update_document'),

]
