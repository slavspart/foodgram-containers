from rest_framework import exceptions, permissions


class UpdateRestriction(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'PUT':
            raise exceptions.MethodNotAllowed('PUT')
        return True
