from rest_framework import serializers
from . models import products

class productSerializer(serializers.ModelSerializer):

    class Meta:
        model = products
        ''' __all__ is because we have small number of 
        of fields and we need to return them all
        Usually a list of fields is set to be returned like 
        fields = ['item_name', 'item_id']
        '''
        fields = '__all__'