from django.urls import path
from . import views

urlpatterns = [
    #path('homePage/', views.homePage, name='homePage'),
    #fk
    path('', views.base, name="myApp"),
    path('info/', views.info, name='info'),
    path('education/', views.education, name='education'),
    path('events/', views.events, name='events'),
    path('careevent/', views.careevent, name='careevent'),
    path('communicationevent/', views.communicationevent, name='communicationevent'),
    path('images/', views.images, name='image'),
    path('privacy/', views.privacy, name='privacy'),
    path('contactpage/', views.contactpage, name='contactpage'),
    path('organization/', views.organization, name='organization')
]