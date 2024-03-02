# from django.contrib.auth.models import Group
# from django.db import transaction
# from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
# from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
# from rest_framework.permissions import IsAuthenticated

# from users.serializers import GroupSerializer, UserSerializer, UserCreateSerializer
# from users.models import User


# class UserListAPIView(ListAPIView):
#     permission_classes = [IsAuthenticated, TokenHasReadWriteScope]
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetailsAPIView(RetrieveAPIView):
#     permission_classes = [IsAuthenticated, TokenHasReadWriteScope]
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserCreateAPIView(CreateAPIView):
#     permission_classes = []
#     queryset = User.objects.all()
#     serializer_class = UserCreateSerializer

#     def perform_create(self, serializer):
#         with transaction.atomic():
#             super().perform_create(serializer)
#             # место для продюсинга данных


# class GroupList(ListAPIView):
#     permission_classes = [IsAuthenticated, TokenHasScope]
#     required_scopes = ["groups"]
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
