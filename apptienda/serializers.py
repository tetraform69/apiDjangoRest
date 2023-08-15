from rest_framework import serializers
from apptienda.models import *


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ("id", "nombreCat")


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ("id", "codigoPro", "nombrePro", "precioPro", "categoriaPro", "fotoPro")
