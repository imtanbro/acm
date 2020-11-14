from django.shortcuts import render, redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
# from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .forms import UserUpdateForm, ProfileUpdateForm
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth import get_user_model
from allauth.account.forms import SetPasswordForm

# def register(request):
#     def save(self):
#
#         # Ensure you call the parent class's save.
#         # .save() does not return anything
#         super(register, self).save()
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             # form.save()
#             # username = form.cleaned_data.get('username')
#             # messages.success(request, f'Your account has been created! You are now able to log in')
#             # return redirect('login')
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()
#             current_site = get_current_site(request)
#             mail_subject = 'Activate your ACM DYPIEMR Student Chapter Website account.'
#             # message = render_to_string('acc_active_email.html')
#             message = render_to_string('users/email/activate_account_email.html', {
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token': account_activation_token.make_token(user),
#             })
#             # message = f"http://127.0.0.1:8000/activate/?uidb64={urlsafe_base64_encode(force_bytes(user.pk))}/?token={account_activation_token.make_token(user)}/"
#             to_email = form.cleaned_data.get('email')
#             email = EmailMessage(
#                 mail_subject, message, to=[to_email]
#             )
#             email.send()
#             messages.success(request, f'Please confirm your email address to complete the registration')
#             return redirect('/')
#             # return HttpResponse('Please confirm your email address to complete the registration')
#
#     else:
#         form = UserRegisterForm()
#     return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        # return redirect('home')
        messages.success(request, f'Your account has been created')
        return redirect('/')
    else:
        return HttpResponse('Activation link is invalid!')