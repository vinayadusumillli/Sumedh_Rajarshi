from django.urls import path
from .views import HomeView, contact_submit

app_name = 'portfolio'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', contact_submit, name='contact_submit'),
]
