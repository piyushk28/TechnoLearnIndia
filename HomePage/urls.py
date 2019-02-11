from django.urls import path
from .views import HomePageView,home_redirect_view

app_name='HomePage'
urlpatterns = [
    path('<pk>/', HomePageView.as_view(),name='home'),
]