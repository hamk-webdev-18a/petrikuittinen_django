from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.CreateEntryView.as_view(), name='create'),
    path('<int:pk>/delete/', views.DeleteEntryView.as_view(), name='delete'),
    path('<int:pk>/', views.UpdateEntryView.as_view(), name='update'),
]

