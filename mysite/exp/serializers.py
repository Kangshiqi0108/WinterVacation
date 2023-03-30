from django.contrib.auth.models import User, Group
from rest_framework import serializers
from exp.models import relatedresources,researchresults,student

class relrSeria(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=relatedresources
        fields=['name','link']

    def create(self, validated_data):
         return relatedresources.objects.create(validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.link = validated_data.get('link', instance.link)
        instance.save()
        return instance
class resrSeria(serializers.Serializer):
    class Meta:
        model:researchresults
        fields='__all__'
        
class studentSeria(serializers.Serializer):
    class Meta:
        model:student
        fields='__all__'
        
        
