from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    Extended user profile model to store additional user information.
    Each user has a one-to-one relationship with this profile.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    skills = models.TextField(
        help_text="Enter your skills separated by commas (e.g., Python, Django, Machine Learning)"
    )
    bio = models.TextField(blank=True, null=True, help_text="Brief description about yourself")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def get_skills_list(self):
        """
        Returns skills as a list for easier processing.
        """
        if self.skills:
            return [skill.strip() for skill in self.skills.split(',') if skill.strip()]
        return []

    def get_skills_display(self):
        """
        Returns formatted skills for display.
        """
        return ', '.join(self.get_skills_list())
