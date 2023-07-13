from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, UserProfile




@receiver(post_save, sender=User) 
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    if created:
        # This will create User Profile
        UserProfile.objects.create(user=instance)
    else:
        try:
            # This will update the profle
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            # This will create the profile if it is not found
            UserProfile.objects.create(user=instance)
            
            # def __str__(self):
            #     return self.user.email

# post_save.connect(post_save_create_profile_receiver, sender=User)



