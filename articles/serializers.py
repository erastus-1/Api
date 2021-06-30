from .models import *
from rest_framework import serializers

#Add your serializers here.
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
       model = Article
       fields = "__all__" 
       read_only_fields = ('published_date', 'modified_date')