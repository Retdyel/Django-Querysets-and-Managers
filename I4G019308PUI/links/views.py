from django.utils import timezone

from rest_framework import generics
from .serializers import LinkSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Link

from . import models
from . import serializers

import datetime

# Create your views here.
class PostListAPI(generics.ListAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
    
class PostCreateAPI(generics.CreateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
    
class PostDetailAPI(generics.RetrieveAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
    
class PostUpdateAPI(generics.UpdateAPIView):
    queryset = Link.object.filter(active=True)
    serializer_class = LinkSerializer
    
class PostDeleteAPI(generics.DestroyAPIView):
    queryset= Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class ActiveLinkView(APIView):
    """
    Returns a list of all active (publicly accessible) links
    """
    def get(self, request):
        """ 
        Invoked whenever a HTTP GET Request is made to this view
        """
        qs = models.Link.public.all()
        data = serializers.LinkSerializer(qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)
    
class RecentLinkView(APIView):
    """
    Returns a list of recently created active links
    """
    def get(self, request):
        """ 
        Invoked whenever a HTTP GET Request is made to this view
        """
        seven_days_ago = timezone.now() - datetime.timedelta(days=7)
        qs = models.Link.public.filter(created_date__gte=seven_days_ago)
        data = serializers.LinkSerializer(qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)
    