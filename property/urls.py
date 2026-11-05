from django.urls import path
from . import views

app_name = 'property'


urlpatterns = [
    path('', views.PropertyListView.as_view(), name='property_list'),
    path('<slug:slug>/', views.PropertyDetailView.as_view(), name='property_detail'),
]