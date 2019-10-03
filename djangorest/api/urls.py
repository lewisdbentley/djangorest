from django.urls import path
from django.conf.urls import url, include
from .views import CreateView, DetailsView
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = {
    path('', CreateView.as_view(), name="create"),
    path('<int:pk>/', DetailsView.as_view(), name="details")
}

urlpatterns = format_suffix_patterns(urlpatterns)