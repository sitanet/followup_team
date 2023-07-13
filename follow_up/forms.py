from django import forms
from .models import Member, Comment




class MemberForm(forms.ModelForm):
    
    class Meta:
        model = Member
        fields = ['image','first_name','middle_name', 'last_name', 'date_of_birth','email', 'phone_no','gender',
                  'marital_status','occupation','address','nationality','kcc_center','wedding_ann',
                  'join','reg_date','about','dept','purpose']
        # exclude = ['staff']
        # widgets = {
        #     'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
        #     'middle_name': forms.TextInput(attrs={'placeholder': 'Middle Name'}),
        #     'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
        #     'phone_no': forms.TextInput(attrs={'placeholder': 'Phone No'}),
        #     'email': forms.TextInput(attrs={'placeholder': 'Email'}),
        #     'occupation': forms.TextInput(attrs={'placeholder': 'Occupation'}),
           
        #     'address': forms.TextInput(attrs={'placeholder': 'Address'}),
        #     'nationality': forms.TextInput(attrs={'placeholder': 'Nationality'}),

            
        #     'landmark': forms.TextInput(attrs={'placeholder': 'Landmark'}),
           
        # }
        
class CommentForm(forms.ModelForm):       
        
    class Meta:
        model = Comment
        fields = ['first_name','last_name',  'comment', 'team_sup']
   