from django.urls import path
from verkefni import views
app_name = 'verkefni'
urlpatterns = [
    path('', views.index, name='index'),
]
