from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse , JsonResponse
from django.views.generic import TemplateView , CreateView
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from .models import User , Profile
from django.contrib import messages
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import DjangoUnicodeDecodeError, force_bytes,   force_str, smart_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from threading import Thread
from .mail_services import MailServices
# Create your views here.




def home(request):
    print(get_current_site(request))
    return render(request, 'post/postsList.html')

class AccountView(TemplateView):
    template_name = 'account/account.html' 


    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        user = Profile.objects.select_related('user').get(user__id=request.user.id)
        context.update({'user_profile': user })
        return self.render_to_response(context)

    

class RegisterView(TemplateView): 
    template_name = 'account/register.html'

    def post(self, request: HttpRequest, *args, **kwargs):
        username = request.POST.get('username')   
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2 :
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exist')
                return redirect('register')
            new_user = User.objects.create(username=username, email=email)
            new_user.set_password(password2)
            new_user.save()
            login(request , new_user )
            return redirect('posts_list')
        return redirect('register')


class LoginView(TemplateView): 
    template_name = 'account/login.html'    

    def post(self, request: HttpRequest, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password )
        check_user = authenticate(username=username , password=password)
        if check_user is not None:
            print(check_user) 
            login(request , check_user)
            return redirect('posts_list')
        return redirect('login')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def account_profile_update(request):
    if request.method == 'POST':
        data = request.POST
        print(data)
        first_name = data.get('first_name')
        las_name = data.get('last_name')
        email = data.get('email')
        username = data.get('username')
        gender = data.get('gender')
        if User.objects.filter(username=username).exclude(id=request.user.id).exists():
            return JsonResponse(
                {'success':True , 
                'detail': 'Username already exist',
                'status':400
                })
        if User.objects.filter(email=email).exclude(id=request.user.id).exists():
            return JsonResponse(
                {'success':True , 
                'detail': 'Email already exist',
                'status':400
                })
        user = User.objects.get(id=request.user.id)
        user.username = username
        user.email = email 
        user.save()
        user_profile = Profile.objects.get(user=user)
        user_profile.first_name = first_name
        user_profile.last_name = las_name
        user_profile.gender = gender
        user_profile.save()

    return JsonResponse({'success':True ,'detail': 'Profile updated successfully', 'status':200})

class ForgetPasswordView(TemplateView): 
    template_name = 'account/forgetPassword.html'

    def post(self, request):
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            uuidb64 = urlsafe_base64_encode(force_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            Thread(target=MailServices.forget_password_mail, kwargs={
                'email': user.email ,'token': token , 'uuidb64':uuidb64 , 'current_site' : get_current_site(request)
            }).start()
        except:
            pass
        messages.info(request,'Password reset instruction will be sent to the your mail' )
        return redirect('forget-password') 


class ForgetPasswordConfirm(TemplateView):
    template_name = 'account/forgetPasswordConfirm.html'

    def post(self, request, token , uuidb64 ):
        try:
            id = smart_str(urlsafe_base64_decode(uuidb64))
            user = User.objects.get(id=id)
            password1 = request.data['password1']
            password2 = request.data['password2']
            if password1 != password2 :
                messages.error(request,'Password does not match' )
                return  redirect('forget_password-confirm')
            if PasswordResetTokenGenerator().check_token(user, token):
                user.set_password(password2)
                user.save() 
                return redirect('login')
            messages.error(request,'Token is not valid' )
            return  redirect('forget_password-confirm')
        except DjangoUnicodeDecodeError as identifier:
            messages.error(request,'Token is not valid' )
            return redirect('forget_password-confirm')
                    


