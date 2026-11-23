from django.urls import path
from .views import LoginPageView,RegView


urlpatterns=[

    path('login',LoginPageView.as_view(),name='login'),
    path('reg',RegView.as_view(),name="reg")


]