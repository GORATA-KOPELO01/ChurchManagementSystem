
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("Authentication.urls")),
    path("", include("Members.urls")),
    path("", include("Events.urls")),
    path("", include("Donations.urls")),
    path("", include("Communication.urls"))
    ]
