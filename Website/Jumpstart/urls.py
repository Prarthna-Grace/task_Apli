from django.urls import path
from . import views



urlpatterns = [
    path('<int:test_id>/',views.detail, name='detail'),
    path('', views.test , name='home-page'),

]