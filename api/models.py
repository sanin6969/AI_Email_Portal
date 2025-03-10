from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    full_name = models.CharField(max_length=50)  
    bio = models.TextField()
    resume = models.FileField(upload_to="user/resumes/")
    linkedin_url = models.URLField()
    github_url = models.URLField()
    portfolio_url = models.URLField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    def __str__(self):
        return self.full_name
    
class JobPostion(models.Model):
    company = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    email = models.EmailField()
    employment_type = models.CharField(max_length=20)
    salary = models.CharField(max_length=50)
    job_description = models.TextField()
    location = models.CharField(max_length=50)
    job_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.title} at {self.company}'
    
class JobApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey('JobPostion', on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_applied = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.job.title}"