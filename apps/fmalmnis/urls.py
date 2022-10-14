from django.urls import path

from . import views

urlpatterns = [
    path('download/', views.DownloadView.as_view(), name='download')
]
