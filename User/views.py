from django.shortcuts import render,redirect
from .forms import register_form,user_edit_form,profile_edit_form
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile as Profile_cls

# Create your views here.

def Register(request):
    if(request.method=='POST'):
        form=register_form(request.POST)
        if form.is_valid():
            myuser=form.save()
            user=request.POST['username']
            messages.success(request, f"Account created for {user} successfully! You can now log in.")
            

            # print("here my boi")
            # Profile_cls.objects.create(user=myuser)
            return redirect('user-login')      
    else:
        form=register_form()
        return render(request,'User/register.html',{'form':form})
@login_required
def Profile(request):
    return render(request,'User/profile.html')

def editProfile(request):
    if (request.method=='POST'):
        u_form=user_edit_form(request.POST,instance=request.user)
        p_form=profile_edit_form(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid and p_form.is_valid:
            u_form.save()
            p_form.save()
            return redirect('user-profile')
        else:
            return request('profile-edit')
    else:
        u_form=user_edit_form(instance=request.user)
        p_form=profile_edit_form(instance=request.user.profile)

        context ={
            'u_form':u_form,
            'p_form':p_form,
        }
        return render(request,'User/EditProfile.html',context)
