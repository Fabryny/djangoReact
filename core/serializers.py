from .models import List
from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['id','nome', 'finalizado']

class ListSerializer(serializers.HyperlinkedModelSerializer):
    item_set = ItemSerializer(many=True)
    class Meta:
        model = List
        fields = ['id', 'nome', 'proprietario', 'url', 'item_set']