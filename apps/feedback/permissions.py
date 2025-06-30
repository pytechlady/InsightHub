from rest_framework import permissions


class IsSameOrganisation(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.uploaded_by.organisation == request.user.organisation