from django.urls import path
from .views import home,registeruser,document_input,profile, DocumentDetailView, DocumentUpdateView

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('register/',registeruser ,name='register'),
    path('document/', document_input, name='document'),
    path('profile/', profile, name='profile'),
    path('detail/<int:pk>/', DocumentDetailView.as_view(), name='document-detail'),
    path('update/<int:pk>/', DocumentUpdateView.as_view(), name='document-update'),

]
