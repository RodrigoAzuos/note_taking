from django.urls import include, path

urlpatterns = [
  path("contas/", include("django.contrib.auth.urls")),
]

