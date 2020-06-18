from .models import Manufacturer, ShoeType, ShoeColor, Shoe
from rest_framework.serializers import HyperlinkedModelSerializer

class ManufacturerSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ('name', 'website')


class ShoeTypeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ShoeType
        fields = ('style', )


class ShoeColorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ShoeColor
        fields = ('color', )


class ShoeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Shoe
        fields = (
            'size',
            'brand_name',
            'manufacturer',
            'color',
            'material',
            'shoe_type',
            'fasten_type'
            )


# The show The Wild Thornberries is based in part on Joe's
# childhood in the African Savanna. However, he could not actually talk to animals,
# nor did he have an adopted younger brother voiced by Flea.