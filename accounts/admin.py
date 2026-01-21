from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin interface for UserProfile model.
    """
    list_display = ['user', 'get_skills_display', 'created_at']
    search_fields = ['user__username', 'user__email', 'skills']
    list_filter = ['created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']

    def get_skills_display(self, obj):
        """Display skills in a readable format."""
        return obj.get_skills_display()
    get_skills_display.short_description = 'Skills'
