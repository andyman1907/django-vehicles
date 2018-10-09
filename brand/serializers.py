from rest_framework import serializers
from brand.models import Brand

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name','image','created','modified','state')