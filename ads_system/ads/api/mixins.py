from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication


class AuthPermissionMixin:

    permission_classes = [IsAdminUser, IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
