from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login , authenticate , logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.
def signIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('username : ' , username)
        print('password ;' , password)

        if not User.objects.filter(username = username).exists():
            messages.error(request , 'Invalid Username')
            return redirect(request.path_info)
        else:
            user = authenticate(username = username , password = password)
            if user is not None:
                userobj = User.objects.get(username = username)
                profileobj = userProfile.objects.get(user = userobj)
                if profileobj.is_approved:
                    login(request , user)  
                    messages.info(request , 'Logged in Successfully !' )  
                    return redirect('home')
                else:
                    messages.error(request , 'Please ask your Support team to approve your account !')
                    return redirect(request.path_info)
            else:
                messages.error(request , 'Invalid Password')
                return redirect(request.path_info)
    return render(request , 'auth/login.html')


def signOut(request):
    if request.user.is_authenticated:
        messages.info(request , 'Looged out successfully , Login again to access dashboard')
        logout(request)
        return redirect('sign-in')
    else:
        return redirect(request.path_info)
    

@login_required
def profilePage(request):
    user = request.user
    context = {
        'user':user
    }
    return render(request , 'auth/profile.html' , context)


@login_required
def settings(request):
    if request.method == 'POST':
        img = request.FILES.get('img')
        print(img)
        print(img)
        print(img)
        print(img)
        print(img)
        print(img)
        print(img)
        print(request.POST)
        print(request.FILES)
        if img is not None:
            profile = userProfile.objects.get(user = request.user)
            profile.image = img
            profile.save()
            messages.info(request , 'profile image updated successfully')
            return redirect(request.path_info)
        else:
            messages.error(request , 'Please select the correct one')
            return redirect(request.path_info)
    return render(request , 'auth/settings.html')

def editProfile(request):
    if request.method == "POST":
        #gettings data from request object 
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        pin_code = request.POST.get('pin_code')       
        district = request.POST.get('district')
        shop_name = request.POST.get('shop_name')
        
        #saving the details in model
        profile = userProfile.objects.get(user = request.user)
        profile.user.first_name = fname
        profile.user.last_name = lname
        profile.user.email = email
        profile.user.save()
        profile.address = address
        profile.phone_number = phone_number
        profile.pin_code = pin_code
        profile.district = district
        profile.shop_name = shop_name
        profile.save()
        messages.info(request , 'changes saved successfully ')
        return redirect(request.path_info)

    return redirect('settings')




@login_required
def security(request):
    if request.method == 'POST':
        old_pass = request.POST.get('currentPassword')
        new_pass = request.POST.get('newPassword')
        con_pass = request.POST.get('confirmPassword')
        print( old_pass , new_pass , con_pass)
        new_pass = new_pass.strip()
        con_pass = con_pass.strip()
        user = authenticate(username = request.user.username , password = old_pass)
        print()
        print()
        print()
        print(user)
        print()
        print()
        if user is not None:
            if len(new_pass)>=8:
                if new_pass == con_pass:
                    user.set_password(new_pass)
                    user.save()
                    logout(request)
                    messages.info(request , 'password changes successfully ! , login again')
                    return redirect('sign-in')
                else:
                    messages.error(request , 'new password and confirm password are didn;t match')
                    return redirect(request.path_info)
            else:
                messages.error(request , 'newpassword should contains minimum 8 characters and mixed of numbers')
                return redirect(request.path_info)
                
        else:
            messages.error(request , 'your current password is  incorrect')
            return redirect(request.path_info)

        return redirect(request.path_info)
    return render(request, 'auth/security.html')