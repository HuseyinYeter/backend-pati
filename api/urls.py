
from django.urls import path, include
from .views import *
urlpatterns = [

    path('list/',ReportListView.as_view()),
    path("login/",login),
    path("logout/",logout),
    path("detail/<int:id>",ReportDetailView.as_view())

]