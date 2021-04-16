from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models.user import Profile, CustomUser, Billing
from .models.product import Category, Subcategory, Sub_category_type
from .models.contact import Contact_Us, Subscribers
from django.contrib.auth import authenticate, login as auth_login, logout


# Create your views here.
def index(request):
    all_category = get_cat_and_subcat()
    # messages.error(request,'Hello Welcome to HiFi')
    param = {'all_category':all_category}
    return render(request, 'shop/index.html', param)


def temp(request):
    return render(request, 'shop/temp.html')

def contact_us(request):
    all_category = get_cat_and_subcat()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact_Us(name=name,email=email,mobile=phone,message=message)
        contact.save()
        messages.success(request, 'We will get back to you ASAP. ')
        return redirect('contact_us')

    else:
        param = {'all_category': all_category}
        return render(request, 'shop/contact.html', param)

def store(request):
    all_category = get_cat_and_subcat()
    param = {'all_category': all_category}
    return render(request, 'shop/store.html', param)

def Product_view(request):
    all_category = get_cat_and_subcat()
    param = {'all_category': all_category}
    return render(request, 'shop/view_product.html', param)

def cart(request):
    all_category = get_cat_and_subcat()
    param = {'all_category': all_category}
    return render(request, 'shop/cart.html', param)


@login_required(login_url='login')
def profile(request):
    all_category = get_cat_and_subcat()
    user = get_object_or_404(CustomUser, email=request.user.email)
    try:
        user_info = Profile.objects.get(user=user.id)
    except:
        user_info = None

    if request.method == 'POST':
        data = request.POST
        try:
            image = request.FILES['image']
        except:
            image = None

        fname = data.get('fname', None)
        lname = data.get('lname', None)
        phone = data.get('phone', None)
        dob = data.get('dob', None)
        gender = data.get('gender', None)
        user.first_name = fname
        user.last_name = lname
        user.save()

        if user_info is None:
            profile = Profile(user=user, mobile=phone)
            if dob != "":
                profile.dob = dob
            if gender is not None:
                profile.gender = gender
            if image is not None:
                profile.image = image
            profile.save()
        else:
            user_info.mobile = phone
            if dob != "":
                user_info.dob = dob
            elif gender is not None:
                user_info.gender = gender
            elif image is not None:
                user_info.image = image

            user_info.save()
    param = {'all_category': all_category, 'user':user, 'profile':user_info}
    return render(request, 'shop/profile.html', param)

@login_required(login_url='login')
def billing(request):
    all_category = get_cat_and_subcat()
    user = get_object_or_404(CustomUser, email=request.user.email)
    try:
        profile = Profile.objects.get(user=user.id)
    except:
        profile = None

    billing = Billing.objects.filter(user = user.id)
    if not billing:
        billing = False
    else:
        billing = billing

    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        mobile = data.get('mobile')
        country = data.get('country')
        state = data.get('state')
        city = data.get('city')
        pin_code = data.get('pin_code')
        locality = data.get('locality')
        address = data.get('address')
        landmark = data.get('landmark')
        alt_mobile = data.get('alt_mobile')
        type = data.get('type')

        billing = Billing(
            user      = user,
            name      = name,
            mobile    = mobile,
            country   = country,
            state     = state,
            city      = city,
            pin       = pin_code,
            locality  = locality,
            address   = address,
            landmark  = landmark,
            alt_mobile= alt_mobile,
            type      = type
            )
        billing.save()
        messages.success(request, 'Your Address Added successfully .')
        return redirect('addresses')

    param = {'all_category': all_category, 'profile': profile, 'billing': billing}
    return render(request, 'shop/billing.html', param)

def delete_billing(request, **kwargs):
    id = kwargs.get('pk')
    billing = get_object_or_404(Billing, pk=id)
    billing.delete()
    messages.success(request, 'Your Address deleted Successfully')
    return redirect('addresses')

def edit_billing(request, **kwargs):
    id = kwargs.get('pk')
    billing = get_object_or_404(Billing, pk=id)
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        mobile = data.get('mobile')
        country = data.get('country')
        state = data.get('state')
        city = data.get('city')
        pin_code = data.get('pin_code')
        locality = data.get('locality')
        address = data.get('address')
        landmark = data.get('landmark')
        alt_mobile = data.get('alt_mobile')
        type = data.get('type')

        billing.name=name
        billing.mobile=mobile
        billing.country=country
        billing.state=state
        billing.city=city
        billing.pin=pin_code
        billing.locality=locality
        billing.address=address
        billing.landmark=landmark
        billing.alt_mobile=alt_mobile
        billing.type=type
        billing.save()
        messages.success(request, 'Your Address Updated successfully')
        return redirect('addresses')

    all_category = get_cat_and_subcat()
    param = {'all_category': all_category, 'billing':billing}
    return render(request, 'shop/edit-billing.html', param)





#### User Authintaction


def register_user(request):
    all_category = get_cat_and_subcat()
    if request.method == 'POST':
        data = request.POST
        fname = data.get('fname')
        lname = data.get('lname')
        email = data.get('email')
        password1 = data.get('password1')
        password2 = data.get('password2')
        if password1 == password2:
            user = CustomUser(email=email, first_name=fname, last_name=lname)
            user.set_password(password1)
            user.save()
        return redirect('home')
    param = {'all_category': all_category}
    return render(request, 'shop/signup.html', param)


def login(request):
    all_category = get_cat_and_subcat()
    next = request.GET.get('next')
    if request.method == 'POST':
        data = request.POST
        next = data.get('next')
        email = data.get('email')
        password = data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, f'Welcome back {user.first_name.upper()} .')
        else:
            messages.error(request, 'Please confirm your password and try again !!')
        if next != 'None':
            return HttpResponseRedirect(next)


        print(next)
        return redirect('home')
    param = {'all_category': all_category, 'next':next}
    return render(request, 'shop/login.html', param)


def Logout(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def Change_password(request):
    all_category = get_cat_and_subcat()
    if request.method == "POST":
        current_pass = request.POST.get('cur_pass')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        user = get_object_or_404(CustomUser, email=request.user.email)
        flag = check_password(current_pass, user.password)
        if flag and pass1==pass2:
            user.set_password(pass1)
            user.save()
            messages.success(request,'Password has been changed successfully .')
        else:
            messages.error(request, 'Please Confirm your password and try again.')
        return redirect('Change_password')
    param = {'all_category': all_category, 'next': next}
    return render(request, 'shop/change_password.html', param)



def get_cat_and_subcat():
    category_data = {}
    category = Category.objects.all()
    for cat in category:
        try:
            subcat_data = {}
            subcategory = Subcategory.objects.filter(category=cat.id).distinct()
            if len(subcategory) > 0:
                for subcat in subcategory:
                    try:
                        subcat_type = []
                        sub_cat_type = Sub_category_type.objects.filter(subcategory=subcat.id)
                        if len(sub_cat_type) > 0:
                            subcat_type.append(sub_cat_type)

                        subcat_data[subcat] = subcat_type
                    except:
                        pass
            category_data[cat] = subcat_data
        except:
            pass
    return category_data




