from django.urls import path
from .views import TacticsView, GeneratePdfView

app_name = 'mainapp'

urlpatterns = [
    path('', TacticsView.as_view(), name='index'),
    path('load_pdf/', GeneratePdfView.as_view(), name='load_pdf'),

]