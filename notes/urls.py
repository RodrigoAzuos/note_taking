from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("atualizar/<int:note_id>/", views.update, name="update"),
    path("delete/<int:note_id>/", views.delete, name="delete")
]