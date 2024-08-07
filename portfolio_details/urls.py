from django.urls import path
from portfolio_details.views import *

urlpatterns = [
    # path('home', home_view, name='home_view'),
    path('about', about_view, name='about_view'),
    path('resume', resume_view, name='resume_view'),
    path('contact', contact_view, name='contact_view'),
    path('services', services_view, name='services_view'),
    path('portfolio', portfolio_view, name='portfolio_view'),
    path('portfolio/details/<int:pk>', portfolio_details, name='portfolio_details'),
]
