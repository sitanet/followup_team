from django.shortcuts import render

# Create your views here.
from django.utils.http import urlsafe_base64_decode
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .forms import StaffForm, UserForm, staff_Profile
from .models import User, UserProfile, staff
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .utils import send_verification_email
from django.contrib.auth.tokens import default_token_generator



# Create your views here.
@login_required(login_url='login')
def registerUser(request):
    if request.method == 'POST':
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
    #   create the user using the form
            # password = form.cleaned_data['password']
            # user = form.save(commit=False)
            # user.set_password(password)
            # user.role = User.CUSTOMER
            # form.save()
            
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.CUSTOMER
            user.save()
            messages.success(request, "Your Account has been registered successfully")
            return redirect('registerUser')
        else:
            print(form.errors)
    else:
        form = UserForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/registerUser.html', context)


@login_required(login_url='login')
def registerStaff(request):
  
    if request.method == 'POST':
        form = UserForm(request.POST)
        s_form = StaffForm(request.POST, request.FILES)
       
        if form.is_valid() and s_form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.STAFF
            user.save() 
            staff = s_form.save(commit=False)
            staff.user = user
            
            user_profile = UserProfile.objects.get(user=user)
            staff.user_profile = user_profile
            staff.save()
            messages.success(request, "Your Account has been registered successfully")
           
           
            
            
            
            
            # send verification email
            email_subject = 'Please Activate Your Account'
            email_template = 'accounts/emails/accounts_verification_email.html'
            send_verification_email(request, user, email_subject, email_template)
            
            messages.success(request, 'Your account has been registered successfully! Please wait for the approval.')
            return redirect('registerStaff')
        else:
            print('invalid form')
            print(form.errors)
    else:
        
        form = UserForm()
        s_form = StaffForm()
        
    context = {
        'form': form,
        's_form' : s_form,
        
    }
    return render(request, 'accounts/registerStaff.html', context)

def activate(request, uidb64, token):
    # Activate the user by setting the is_active status to true
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError,User.DoesNotExist):
        user = None
        
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulation your account is activated')
        return redirect('login')
    else:
        messages.error(request, 'Invalid Activation Link')
        return redirect('registerStaff')
    

def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login credential')
            return redirect('login')
    return render(request, 'accounts/login.html')



@login_required(login_url='login')
def dashboard(request):
  
    return render(request, 'accounts/dashboard.html')



def logout(request):
    auth.logout(request)
    
    return redirect('login')
    

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email__exact=email)
            
            # send reset password email
            email_subject = 'Reset Your Password'
            email_template = 'accounts/emails/reset_password_email.html'
            send_verification_email(request, user, email_subject, email_template)
            messages.success(request, 'Password reset link has been sent to your email address.')
            return redirect('login')
        else:
            messages.error(request, 'Account does not exist.')
            return redirect('forgot_password')
    return render(request, 'accounts/forgot_password.html')

def reset_password_validate(request, uidb64, token):
    # validate the user by decode the token and user pk
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User._default_manager.get(pk=uid)
        except(TypeError, ValueError, OverflowError,User.DoesNotExist):
            user = None
        if user is not None and default_token_generator.check_token(user, token):
            request.session['uid'] = uid
            messages.info(request, 'Please reset your password')
            return redirect('reset_password')
        else:
            messages.error(request, 'This link has been expired')
            return redirect('login')
   

def reset_password(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            pk = request.session.get('uid')
            user = User.objects.get(pk=pk)
            user.set_password(password)
            user.is_active = True
            user.save()
            messages.success(request, 'Password reset successfully')
            return redirect('login')
        else:
            messages.error(request, 'Password do no match')
            return redirect('reset_password')
    return render(request, 'accounts/reset_password.html')

@login_required(login_url='login')
def staff_profile(request):
    staff1 = get_object_or_404(staff, user=request.user)
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        profile_form = staff_Profile(request.POST, request.FILES, instance=profile)
        user_form = StaffForm(request.POST, request.FILES, instance=staff1)
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            messages.success(request, 'Settings updated.')
            return redirect('staff_profile')
        else:
            print(profile_form.errors)
            print(user_form.errors)
    else:
    
    
    
        user_form = StaffForm(instance = staff1)
        profile_form = staff_Profile(instance = profile)
 
   
    context = {
   
        'user_form': user_form,
        'profile_form': profile_form,
        'profile': profile,
        'staff1': staff1,
      
       
    }
    return render(request, 'staff/staff_profile.html', context)



# def dashboard(request):
#     return render(request, 'follow_up/dashboard.html')