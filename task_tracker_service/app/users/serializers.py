# from django.contrib.auth.models import Group
# from rest_framework import serializers

# from users.models import User


# class UserSerializer(serializers.ModelSerializer):
#     uuid = serializers.UUIDField(read_only=True)

#     class Meta:
#         model = User
#         fields = ("username", "email", "first_name", "last_name", "role", "uuid")
        


# class UserCreateSerializer(UserSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta(UserSerializer.Meta):
#         fields = (*UserSerializer.Meta.fields, "password")


# class GroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Group
#         fields = ("name", )
