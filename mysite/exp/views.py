from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import lang
from .serializers import LangSerializer


class LangList(APIView):
    
    def get(self, request):
        langs = lang.objects.all()
        serializer = LangSerializer(langs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = LangSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LangDetail(APIView):
    
    def get_Lang(self, pk):
        try:
            return lang.objects.get(pk)
        except lang.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        language = self.get_Lang(pk)
        serializer = LangSerializer(language)
        return Response(serializer.data)
    
    def put(self, request, pk):
        language = self.get_object(pk)
        serializer = LangSerializer(language, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        

