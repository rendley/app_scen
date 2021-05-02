from django.urls import path
from .views import TacticsView

app_name = 'mainapp'

urlpatterns = [
    path('', TacticsView.as_view(), name='index'),
]