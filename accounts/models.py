from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from companies.models import Branch




# Create your models here.

# Usermanager give you two method for creating normal user and superuser
# the job of usermanager is to create user for admin and normal user and you configure it to suite your application
class UserManager(BaseUserManager):
    # this will create for normal user
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('User must have an email address')
        
        if not username:
            raise ValueError('User must have username')
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # this will create for super user
    def create_superuser(self, first_name, last_name, username, email, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

# we inherit AbstractBaseUser from Django and we are taking full control of custom user model
# including authentication functionality of django
# there two class of user model which is abstractuser and AbstractBaseUser
# when you use abstractuser you will not have full control of the user model you can only add fields to it but not change
# AbstractBaseUser provide us full control of the model
# for example in abstractuser you can only use username as unique login paramenter
# but in AbstractBaseUser you can use email as a logn parameter
class User(AbstractBaseUser):
    STAFF = 1
    MEMBER = 2
 
    
    
    ROLE_CHOICE = (
        (STAFF, 'Staff'),
        (MEMBER, 'Member'),
       
    
    )
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, null=True)
            
    # required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    
    objects = UserManager()
    
    
    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
            
    def get_role(self):
        if self.role == 1:
            user_role = 'Staff'
        elif self.role == 2:
            user_role = 'Customer'
        return user_role
        




# profile model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='users/profile_pictures', blank=True, null=True)

    address_line1 = models.CharField(max_length=50, blank=True, null=True)
    address_line2 = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    
    
    
    
    def __str__(self):
        return self.user.email
    


class staff(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE, null=True, blank=True)
    # first_name = models.CharField(max_length=20)
    # branch = models.ForeignKey(Branch, related_name='branch', on_delete=models.CASCADE, null=True, blank=True)
    user_profile = models.OneToOneField(UserProfile, related_name='userprofile', on_delete=models.CASCADE)
    staff_full_name = models.CharField(max_length=30)
    
    is_approved = models. BooleanField(default=False)
    
    
    
    
    def __str__(self):
        return self.staff_full_name
  
    