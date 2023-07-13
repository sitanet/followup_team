from django import forms
from .models import User, staff, UserProfile
from .validators import allow_only_images_validator




class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
        }
        
    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
           
        if password != confirm_password:
            raise forms.ValidationError("Password does not match")





class StaffForm(forms.ModelForm):
   
    class Meta:
        model = staff
        fields = ['staff_full_name']
        widgets = {
            'staff_full_name': forms.TextInput(attrs={'placeholder': 'Staff ID'})
         
        }
        
        
        
# class staff_form(forms.ModelForm):
   
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'username', 'email', 'phone_number']
        
                
 
class staff_Profile(forms.ModelForm):
   profile_picture = forms.FileField(widget=forms.FileInput(attrs={'class':'cur-p btn-info'}), validators=[allow_only_images_validator])
 
   class Meta:
        model = UserProfile
        fields = ['profile_picture',  'address_line1', 'country', 'state', 'city']