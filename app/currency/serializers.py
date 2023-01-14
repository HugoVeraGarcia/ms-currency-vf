from rest_framework import serializers
from .models import Currency, Track_Fee

# serializer para el modelo Currency
class CurrencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Currency

        #ocultando id_currency, por seguridad
        exclude = ['id_currency']
        




# serializer para el modelo Track_Fee
class Track_Fee_Formatted_Serializer(serializers.Serializer):
    
    money_request = serializers.FloatField(max_value=1000, min_value=1)
    base = serializers.CharField(max_length=4, allow_blank=False)
    quote = serializers.CharField(max_length=4, allow_blank=False)


    class Meta:
        fields = ('base', 'quote', 'money_request')

# serializer para el poblar el modelo Currency, generate: True es requerido
class setup_Serializer(serializers.Serializer):  

    generate = serializers.BooleanField(required=True)

    class Meta:

        fields = ('generate' )