from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from serializers import relrSeria
from models import relatedresources

class relrList(APIView):
    def get(self,request,format=None):
        relrlist = relatedresources.objects.all()
        serializer = relrSeria(relrlist, many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        newrelr = relrSeria(data=request.data)
        if newrelr.is_valid():
            newrelr.save()
            return Response(newrelr.data, status=status.HTTP_201_CREATED)
        return Response(newrelr.errors, status=status.HTTP_400_BAD_REQUEST)

class relrDetail(APIView):
    
    def get(self,pkey):
        try:
            return  relatedresources.objects.get(pk=pkey)
        except relatedresources.DoesNotExist:
            return Http404
            
            