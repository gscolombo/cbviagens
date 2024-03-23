from django.urls import path

from . import operations

urlpatterns = [
    path("", operations.crud, name="operations"),
    path("destinations/", operations.destinations, name="destinations"),
    path("test/", operations.test, name="API route test"),
]
