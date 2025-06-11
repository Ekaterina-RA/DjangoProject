from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserRegisterForm, UserLoginForm
from .models import User
from django.core.mail import send_mail
from django.contrib.auth import login


def send_welcome_email(user_email):
    subject = 'Добро пожаловать на наш сайт'
    message = 'Спасибо, что зарегистрировались на нашем сайте!'
    from_email = 'ekaterina.kuzl@gmail.com'
    recipient_list = [user_email]
    send_mail(subject, message, from_email, recipient_list)


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        send_welcome_email(user.email)
        return super().form_valid(form)


class CustomLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'