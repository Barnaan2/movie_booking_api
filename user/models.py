from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save,post_delete

# Create your models here.
class User(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=25,unique=True) 
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=30,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    profile_picture =models.ImageField(null=True,blank=True,default='avatar.png')
    phone_number = models.CharField(max_length=50, blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return str(self.user.phone_number)
    
class Meta:
    ordering = ['name']
    

# signals 
    """
    Where to user  Signals in Django?
   ** most of the time its good to use signals between two models which have 1-1 relationship.
    
    """
    
# def create_profile(sender,instance,created,**kwargs):
#     if created:
#         user = instance
#         Profile.objects.create(user=user,phone_number = user.phone_number)
        
        
        
# post_save(create_profile,sender=User)

# def delete_user(sender,instance,created,**kwargs):
#     user = instance.user
#     user.delete()
    
# post_delete(delete_user,sender=Profile)

# def update_profile(sender,instance,created,**kwargs):
#     if not created:
#         user = instance.user
#         user.phone_number = instance.phone_number
#         user.email = instance.email
#         user.save()
# post_save(update_profile,sender=Profile)