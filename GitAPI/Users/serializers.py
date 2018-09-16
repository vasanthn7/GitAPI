from rest_framework import serializers
from users.models import users

class user_serializers(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = [
            'user',
            'name',
            'email',
            'public_repo',
            'created',
            'followers',
            'following',
        ]
