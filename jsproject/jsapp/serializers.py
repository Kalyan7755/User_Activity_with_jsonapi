from rest_framework_json_api import serializers
from jsapp.models import User_Act

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User_Act
        fields = ('id','real_name', 'tz', 'start_time', 'end_time')
