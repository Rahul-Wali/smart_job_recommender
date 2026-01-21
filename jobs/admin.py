from django.contrib import admin
from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    """
    Admin interface for Job model with enhanced functionality.
    """
    list_display = ['title', 'company', 'location', 'is_active', 'created_at']
    list_filter = ['is_active', 'company', 'created_at']
    search_fields = ['title', 'company', 'required_skills', 'description']
    readonly_fields = ['created_at', 'updated_at']
    list_editable = ['is_active']
    
    fieldsets = (
        ('Job Information', {
            'fields': ('title', 'company', 'location', 'salary_range')
        }),
        ('Requirements & Description', {
            'fields': ('required_skills', 'description')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def get_queryset(self, request):
        """
        Customize the queryset displayed in admin.
        """
        qs = super().get_queryset(request)
        return qs

    actions = ['activate_jobs', 'deactivate_jobs']

    def activate_jobs(self, request, queryset):
        """Bulk action to activate selected jobs."""
        updated = queryset.update(is_active=True)
        self.message_user(request, f'{updated} job(s) activated successfully.')
    activate_jobs.short_description = 'Activate selected jobs'

    def deactivate_jobs(self, request, queryset):
        """Bulk action to deactivate selected jobs."""
        updated = queryset.update(is_active=False)
        self.message_user(request, f'{updated} job(s) deactivated successfully.')
    deactivate_jobs.short_description = 'Deactivate selected jobs'
