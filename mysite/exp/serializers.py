from django.contrib.auth.models import User, Group
from rest_framework import serializers
from models import relatedresources,researchresults,student

class relrSeria(serializers.Serializer):
    class meta:
        model:relatedresources
    
class resrSeria(serializers.Serializer):
    class meta:
        model:researchresults
        
class studentSeria(serializers.Serializer):
    class meta:
        model:student
        
        
