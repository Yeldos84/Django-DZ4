from django.urls import path

from . import views


urlpatterns = [
    # ex: /polls/
    path("zoo", views.zoo, name="zoo"),

]
