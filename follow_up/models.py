from django.db import models
from datetime import date
# Create your models here.
class Member(models.Model):
    
    MALE = 1
    FEMALE = 2
    SINGLE = 1
    MARRIED = 2
    PRIVATE = 1
    STATE = 2
    FEDERAL = 3
    
    
    GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
       
    )
    
    MARITAL = (
        (SINGLE, 'Single'),
        (MARRIED, 'Married'),
       
    )

  
    # staff = models.ForeignKey(staff, on_delete=models.CASCADE)
    # custom_id = models.CharField(primary_key = True, max_length=10, unique=True, default=custom_id)
    image = models.ImageField(upload_to='images/')
    first_name = models.CharField(max_length=50, blank=False, null=False , unique=True,)
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    date_of_birth = models.DateField(default=date.today, blank=True, null=True)
    email = models.EmailField(max_length=40, blank=True, null=True)
    phone_no = models.CharField(max_length=15, blank=True, null=True)
    gender = models.PositiveIntegerField(choices=GENDER, blank=True, null=True)
    marital_status = models.PositiveIntegerField(choices=MARITAL, blank=True, null=True)
    occupation = models.CharField(max_length=20, blank=True,null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    nationality = models.CharField(max_length=20, blank=True, null=True)
    kcc_center = models.CharField(max_length=20, blank=True, null=True)
    
    wedding_ann = models.CharField(max_length=30, blank=True, null=True)
    join = models.CharField(max_length=20, blank=True, null=True)
    reg_date = models.CharField(max_length=20, blank=True, null=True)
    about = models.CharField(max_length=20, blank=True, null=True)
    dept = models.CharField(max_length=20, blank=True, null=True)
    purpose = models.CharField(max_length=20, blank=True, null=True)
  
   
    
    


    def __str__(self):
        return self.first_name
    # add any other fields you need here
    



class Comment(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='comments')
    first_name = models.CharField(max_length=40, blank=False, null=False )
    last_name = models.CharField(max_length=25, blank=True, null=True)
    team_sup = models.CharField(max_length=20, blank=True, null=True)
    date_created = models.DateField(default=date.today, blank=True, null=True)
    comment = models.TextField()
  
   
    
    


    def __str__(self):
        return self.first_name
    # add any other fields you need here