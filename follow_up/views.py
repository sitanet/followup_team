import os
from sre_constants import BRANCH
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages, auth

from accounts.context_processors import get_staff
from accounts.models import staff
from .forms import MemberForm, CommentForm
from .models import Member, Comment
from django.shortcuts import render, get_object_or_404
from .utils import custom_id
from accounts.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required(login_url='login')
def mem_reg(request):
    
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        
       
        if form.is_valid():
            
            # type_of_account = form.cleaned_data['type_of_account']
            image = form.cleaned_data['image']
            first_name = form.cleaned_data['first_name']
            middle_name = form.cleaned_data['middle_name']
            last_name = form.cleaned_data['last_name']
            date_of_birth = form.cleaned_data['date_of_birth']
            email = form.cleaned_data['email']
            phone_no = form.cleaned_data['phone_no']
            gender = form.cleaned_data['gender']
            marital_status = form.cleaned_data['marital_status']
            occupation = form.cleaned_data['occupation']
       
            address = form.cleaned_data['address']
            nationality = form.cleaned_data['nationality']
         
            kcc_center = form.cleaned_data['kcc_center']
            wedding_ann = form.cleaned_data['wedding_ann']
            join = form.cleaned_data['join']
            reg_date = form.cleaned_data['reg_date']
            about = form.cleaned_data['about']
            dept = form.cleaned_data['dept']
            purpose = form.cleaned_data['purpose']
            
            # customer = Customer(first_name=first_name,middle_name=middle_name,last_name=last_name,date_of_birth=date_of_birth,email=email,phone_no=phone_no,gender=gender,marital_status=marital_status,occupation=occupation,district=district,acct_off=acct_off,id_type=id_type,id_no=id_no,issued_authority=issued_authority,issued_state=issued_state,expiry_date=expiry_date,address=address,nationality=nationality,state=state,local_govt=local_govt,city=city,landmark=landmark,next_of_kin=next_of_kin,next_address=next_address,next_phone_no=next_phone_no,type_of_account=type_of_account, customer= True)
            # member = form.save(commit=False)
            
            # member.staff = staff.objects.get(user=request.user)
            # user = staff.objects.get(user=request.user)
          
            form.save()
            messages.success(request, 'Account has been registered successfully!.')
            return redirect('display_all')
        
    
        
        else:
            messages.warning(request, form.errors)
            messages.warning(request, 'Please Check the form filed and fill them before submission!.')
            return redirect('mem_reg')
            # print('invalid form')
            
    else:
       
        form = MemberForm()
        
        # cust_coa = Coa.objects.raw("select * from chart_of_accounts_coa where right(gl_no,3) = '200'")
        
        
        context = {
             'form': form,
       
            
           
             
            
        }

  
    return render(request, 'follow_up/mem_reg.html', context)



@login_required(login_url='login')
def display_all(request):
    if 'q' in request.GET:
        q = request.GET['q']
        # data = Data.objects.filter(last_name__icontains=q)
        multiple_q = Q(Q(first_name__icontains=q) | Q(middle_name__icontains=q) | Q(last_name__icontains=q) | Q(email__icontains=q))
        members = Member.objects.filter(multiple_q)
    else:
        members = Member.objects.all()
    return render(request, 'follow_up/display_all.html', {'members': members})






@login_required(login_url='login')
def member_detail(request, id):
    member = get_object_or_404(Member, id=id)

    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(member.image) > 0:
                os.remove(member.image.path)
            member.image = request.FILES['image']
        member.first_name = request.POST.get('first_name')
        member.middle_name = request.POST.get('middle_name')
        member.last_name = request.POST.get('last_name')
        member.date_of_birth = request.POST.get('date_of_birth')
        member.email = request.POST.get('email')
        member.phone_no = request.POST.get('phone_no')
        member.gender = request.POST.get('gender')
        member.marital_status = request.POST.get('marital_status')
        member.occupation = request.POST.get('occupation')
        member.address = request.POST.get('address')
        member.nationality = request.POST.get('nationality')
        member.kcc_center = request.POST.get('kcc_center')
        member.wedding_ann = request.POST.get('wedding_ann')
        member.join = request.POST.get('join')
        member.reg_date = request.POST.get('reg_date')
        member.about = request.POST.get('about')
        member.dept = request.POST.get('dept')
        member.purpose = request.POST.get('purpose')
        member.save()
        messages.success(request, 'Account has been updated successfully!.')
        return redirect('display_all')
    context = {
         'member':member,
         
     }   

    return render(request, 'follow_up/member_detail.html', {'member': member,})





@login_required(login_url='login')
def delete_object(request, id):
    member = get_object_or_404(Member, id=id)
    member.delete()
    return redirect('display_all')
  

# def delete_comment(request, id):
#     member = get_object_or_404(Comment, id=id)
#     member.delete()
#     return redirect('display_all')
    
@login_required(login_url='login')
def display_comment(request):
     if 'q' in request.GET:
        q = request.GET['q']
        # data = Data.objects.filter(last_name__icontains=q)
        multiple_q = Q(Q(first_name__icontains=q)  | Q(last_name__icontains=q) | Q(comment__icontains=q))
        comment = Comment.objects.filter(multiple_q)
     else:
        comment = Comment.objects.all()
     return render(request, 'follow_up/display_comment.html', {'comment': comment})


@login_required(login_url='login')
def comment(request, id):
    member = get_object_or_404(Member, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.member = member
            comment.save()
            return redirect('display_comment')
   
    else:
        form = CommentForm()
    context = {
         'member':member,
         'form':form,
         
     }
    return render(request, 'follow_up/comment.html', context)






# def index(request):
#     if 'q' in request.GET:
#         q = request.GET['q']
#         # data = Data.objects.filter(last_name__icontains=q)
#         multiple_q = Q(Q(first_name__icontains=q) | Q(last_name__icontains=q))
#         data = Member.objects.filter(multiple_q)
#     else:
#         data = Member.objects.all()
#     context = {
#         'data': data
#     }
#     return render(request, 'dashboard/index.html', context)
    
# def member_detail(request, id):
#     form1 = Member.objects.get(id=id)
#     # form = get_object_or_404(Member, id=id)
#     if request.method == 'POST':
#         form = MemberForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Account has been Updated successfully!.')
#     else:
#         form = MemberForm(instance=form1)
#     return render(request, 'member_registration/member_detail.html', {'form': form})

# def member_detail(request, id):
#     customer = get_object_or_404(Member, id=id)
#     if request.method == 'POST':
#         form = MemberForm(request.POST, request.FILES, instance=customer)
#         if form.is_valid():
#             form.save()
#             return redirect('member_detail', id=customer.id)
#     else:
#         form = MemberForm(instance=customer)
#     return render(request, 'member_registration/member_detail.html', {'form': form})
# def delete_customer(request, custom_id):
#     cust_single = Customer.objects.get(custom_id=custom_id)
#     cust_single.delete()
    
#     messages.success(request, 'Account deleted successfully!.')
#     return redirect('modify_delete')


# def cust_menu(request):
#     return render(request, 'customers/cust_menu.html')



# def list_customer(request):
#     return render(request, 'customers/list_customer.html')