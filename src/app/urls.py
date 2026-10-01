from django.urls import path
from . import views

urlpatterns = [path("", views.index), path("health", views.health), path("quote", views.quote)]
handler404 = "app.views.not_found"
handler500 = "app.views.server_error"
