from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from exp.serializers import relrSeria
from exp.models import relatedresources

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
    
    def get_object(self,pkey):
        try:
            return  relatedresources.objects.get(pk=pkey)
        except relatedresources.DoesNotExist:
            return Http404
    
    def get(self, request, pk, format=None):
        det = self.get_object(pk)
        serializer = relrSeria(det)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        det = self.get_object(pk)
        serializer = relrSeria(det, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        det = self.get_object(pk)
        det.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            