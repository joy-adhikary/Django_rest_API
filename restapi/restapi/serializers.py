
# amra serializer use korbo jkn amra amader api er madhome akta model return korbo 

# Serialization that supports both ORM and non-ORM data sources.

# process of python object to json ( python object ke json a format kore return kore dibe , jkn kono request pabe api er maddhome)

from rest_framework import serializers

from .models import Joy
from .models import Joy1



# this one is only for Joy table 
class JoySerializer(serializers.ModelSerializer):
    # inner class meta => kon model , r kon kon fields dekhabe 
    class Meta:
        model = Joy
        # fields = ['id','name','description']
        fields = '__all__'


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = Joy1
        fields = '__all__'