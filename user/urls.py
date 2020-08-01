from django.urls import path, include
from user import views

urlpatterns = [
    path('index/', views.index),
    path('search/', views.search),
    path('login/', views.login),
    path('initdb/', views.init_db),
    path('demand/update/', views.demand_update),
    path('demand/new/', views.demand_new),
    path('error/', views.error),
    path('demand/new/', views.demand_new),
    path('demand/pool/', views.demand_pool),
    path('api/login/', views.api_login),
    path('api/logout/', views.api_logout),
    path('api/demands/', views.api_demands),
    path('api/name_is_av/', views.name_is_av),
    path('api/delete/', views.api_delete),
    path('api/archive/', views.api_archive),
    path('api/update/', views.api_update),
    path('api/demand_new/', views.api_demand_new),

]
