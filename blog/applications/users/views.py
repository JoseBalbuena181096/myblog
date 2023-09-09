from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.http import HttpRequest, HttpResponse
from django import forms
from django.views.generic import (
    View,
    CreateView, 
    UpdateView
)
from django.views.generic.edit import (
    FormView
)
from .forms import (
    UserRegisterForm, 
    LoginForm,
    UpdatePasswordForm,
    VerificationForm,
) 
#
from .models import User
from .funtions import code_generator
# 


class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users_app:user-login')

    def form_valid(self, form):
        # generamos el código
        codigo = code_generator()
        #
        usuario = User.objects.create_user(
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            full_name = form.cleaned_data['full_name'],
            ocupation = form.cleaned_data['ocupation'],
            genero = form.cleaned_data['genero'],
            date_birth = form.cleaned_data['date_birth'],
            codregistro = codigo,
        )
        # enviar el codigo al email al usuario
        asunto = 'Confirmación de email de registro Iron Makers'
        mensaje = 'Tu código de verificación es: ' + codigo
        send_mail(
            asunto,
            mensaje,
            "josebalbuena181096@gmail.com",
            [form.cleaned_data['email'],],
            fail_silently=False,
        )
        # return super(UserRegisterView, self).form_valid(form)
        return HttpResponseRedirect(reverse('users_app:user-verification', kwargs={'pk': usuario.id}))


class LoginUser(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('favoritos_app:perfil')

    def form_valid(self, form):
        user = authenticate(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)


class LogoutView(View):

    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users_app:user-login'
            )
        )


class UpdatePasswordView(LoginRequiredMixin, FormView):
    template_name = 'users/update_password.html'
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('users_app:user-login')
    login_url = reverse_lazy('users_app:user-login')

    def form_valid(self, form):
        usuario = self.request.user
        user = authenticate(
            email=usuario.email,
            password=form.cleaned_data['password1']
        )

        if user:
            new_password = form.cleaned_data['password2']
            usuario.set_password(new_password)
            usuario.save()
        else:
            return HttpResponseRedirect(reverse_lazy('users_app:user-update-password'))

        logout(self.request)
        return super(UpdatePasswordView, self).form_valid(form)
    
class CodeVerificationView(FormView):
    template_name = 'users/verification.html'
    form_class = VerificationForm
    success_url = reverse_lazy('users_app:user-login')
    
    def get_form_kwargs(self):

        kwargs = super(CodeVerificationView, self).get_form_kwargs()
        kwargs.update({
            'pk':self.kwargs['pk'],
        })
        return kwargs

    def form_valid(self, form):
        # id_user = self.kwargs['pk']
        User.objects.filter( 
            id = self.kwargs['pk']
        ).update(
            is_active = True
        )
        return super(CodeVerificationView, self).form_valid(form)
    

class EmpleadoUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "users/update.html"
    model = User
    fields = [
        'email',
        'full_name',
        'ocupation',
        'genero',
        'date_birth',
    ]
    success_url = reverse_lazy('favoritos_app:perfil')
    def form_valid(self, form):
        # Lógica del proceso     
        return super(EmpleadoUpdateView, self).form_valid(form)