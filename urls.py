from django.urls import path
from app_1 import views
urlpatterns = [
    path('index_1/',views.index,name='index_1'),
    path('home/',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('webpage/',views.webpage,name='webpage'),
    path('url/',views.url,name='url'),
]