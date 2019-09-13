from . import views
from django.urls import path

urlpatterns = [
    path('', views.Indexview.as_view(), name='home'),
    path('<slug:slug>/', views.Detailview.as_view(), name='post_detail'), 
    
    # display take value
]