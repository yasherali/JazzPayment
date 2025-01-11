from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=50)
    display_name = models.CharField(max_length=50, default="")
    created_on = models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=False)

    @classmethod
    def get_default_role(cls):
        obj, _ = cls.objects.get_or_create(
            name="admin",
            defaults={
                    "name": "admin",
                    "display_name": "Admin",
                    "active": True
            }
        )
        return obj.pk

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name = "profile")
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="user_role", default=Role.get_default_role)
    name = models.CharField(max_length=255, blank=True , null = True)
    address = models.CharField(blank=True , null = True, max_length=255)
    city = models.CharField(blank=True , null = True, max_length=255)
    is_delete = models.BooleanField(default=False)
    notification = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    is_verified = models.BooleanField(default=False, null=True, blank=True)
    main_image = models.FileField(max_length=256, upload_to = 'save_profile_image/', null=True, blank=True)
        
    def get_name(self):
        if self.name:
            return self.name
        
    def get_email(self):
        if self.user.email:
            return self.user.email
    
    def get_main_image(self):
        if self.main_image:
            return self.main_image.url
        
    class Meta:
        db_table = 'profile'