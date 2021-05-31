# django
from django.urls import path
from users import views

urlpatterns = [
    # url of the items
    path(
        route='api/usesr-list/',
        view= views.usersList,
        name= 'items_list'
    ),
]