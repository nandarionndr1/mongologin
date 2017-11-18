
from .models import User
from rest_framework_mongoengine import serializers

# Register your models here.
class UserSerializer(serializers.DocumentSerializer):
    class Meta:
        model = User
        fields = ('usrnm','pss', 'email', 'name','githuburl','bio')



