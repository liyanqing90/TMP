from django.urls import path, include
from user import views

urlpatterns = [
    path('index/', views.index),
    path('search/',views.search),
    path('login/', views.login),
    path('api/login/', views.api_login),
    path('api/logout/',views.api_logout),
    path('initdb/',views.init_db),
    path('api/new/',views.api_new),
    path('demand/new/',views.demand_new),
    path('demand/pool/',views.demand_pool),
    path('api/demands/',views.api_demands)

]
