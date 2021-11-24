from rest_framework.permissions import BasePermission


class IsQuestionAuthor(BasePermission):

    def has_objects_permission(self, request, view, obj):
        return request.user.is_authentificated and obj.author == request.user