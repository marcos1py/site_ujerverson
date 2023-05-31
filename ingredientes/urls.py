from django.urls import path
from ingredientes import views

urlpatterns = [
    path('', views.home, name="home"),
    path('resultados/', views.resultados, name="resultados"),

]
