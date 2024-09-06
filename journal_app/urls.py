
from django.urls import path

from journal_app.views import Journal


urlpatterns = [
    path("", Journal.as_view(), name=""),
]