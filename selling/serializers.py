from .models import Manufacturer, ShoeType, ShoeColor, Shoe
from rest_framework.serializers import ModelSerializer

class ManufacturerSerializer(ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ('name', 'website')


class ShoeTypeSerializer(ModelSerialister):
    class Meta:
        model = ShoeType
        fields = ('style', )


class ShoeColorSerializer(ModelSerializer):
    class Meta:
        model = ShoeColor
        fields = ('color', )


class ShoeSerializer(ModelSerializer):
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