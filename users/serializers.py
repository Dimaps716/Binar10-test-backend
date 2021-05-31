from .models import User
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        models = User
        fields = '__all__'