from django.shortcuts import render
from rest_framework import generics
from .serializers import BucketlistSerializer
from .models import Bucketlist


# Create your views here.

class CreateView(generics.ListCreateAPIView):
    """This class defines saving a new bucketlist to db"""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist"""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class defines reading, updating and destroying bucketlists"""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

