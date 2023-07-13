from .models import staff, User



def get_staff(request):
    try:
        dashboard_user = staff.objects.get(user=request.user)
        
    except:
        dashboard_user = None
       
    
    return dict(dashboard_user=dashboard_user)




def get_user_details(request):
    try:
        user_details = User.objects.get(user=request.user)
    except:
        user_details = None
    
    return dict(user_details=user_details)