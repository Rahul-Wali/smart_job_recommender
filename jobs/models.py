from django.db import models


class Job(models.Model):
    """
    Job model representing available job positions.
    Each job has a title, required skills, and description.
    """
    title = models.CharField(max_length=200, help_text="Job title/position name")
    required_skills = models.TextField(
        help_text="Required skills separated by commas (e.g., Python, Django, REST API)"
    )
    description = models.TextField(help_text="Detailed job description")
    company = models.CharField(max_length=200, default="Not Specified")
    location = models.CharField(max_length=200, default="Remote", blank=True)
    salary_range = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True, help_text="Is this job currently active?")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Job"
        verbose_name_plural = "Jobs"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_skills_list(self):
        """
        Returns required skills as a list for ML processing.
        """
        if self.required_skills:
            return [skill.strip() for skill in self.required_skills.split(',') if skill.strip()]
        return []

    def get_skills_display(self):
        """
        Returns formatted skills for display.
        """
        return ', '.join(self.get_skills_list())

    def get_short_description(self):
        """
        Returns truncated description for list views.
        """
        if len(self.description) > 150:
            return self.description[:150] + '...'
        return self.description
