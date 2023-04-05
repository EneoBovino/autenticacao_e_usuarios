from django.shortcuts import render, redirect
from accounts.forms import LoginForm, RegisterForm
from django.contrib import auth, messages
from accounts.models import CustomUser


def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            
            username = form['username'].value()
            email = form['email'].value()
            password_1 = form['password_1'].value()
            image = form.cleaned_data.get('profile_image')
            first_name = form['first_name'].value()
            last_name = form['last_name'].value()
            
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, "Usuário já existe!")
                return render(request, 'accounts/register.html', {"form":form})
            
            user = CustomUser.objects.create(
                username=username,
                email=email,
                password=password_1,
                first_name=first_name,
                last_name=last_name,
                user_image=image
            )

            user.save()

            messages.success(request, f"{username} agora está registrado como usuário!")
            return redirect('login')

    return render(request, 'accounts/register.html', {"form":form})

def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form['username'].value()
            password = form['password'].value()

            user = auth.authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:
                auth.login(request, user)
                messages.success(request, f"{username} logado com sucesso!")
                return redirect('login')
            messages.error(request, "usuário/senha estão incorretos ou usuário não existe!")
            return redirect('login')
    return render(request, 'accounts/login.html', {"form":form})