from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(
        label="Usuário",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "digite seu usuário"
            }
        )
    )

    profile_image = forms.ImageField(
        label="Imagem Perfil",
        required=False,
        widget=forms.FileInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    email = forms.EmailField(
        label="email",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: joao_silva@xpto.com"
            }
        )
    )

    first_name = forms.CharField(
        label="Primeiro nome",
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "digite seu nome"
            }
        )
    )

    last_name = forms.CharField(
        label="Sobrenome",
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "digite seu sobrenome"
            }
        )
    )

    password_1 = forms.CharField(
        label="Senha",
        required=True,
        max_length=30,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "digite uma senha"
            }
        )
    )

    password_2 = forms.CharField(
        label="Confirmar senha",
        required=True,
        max_length=30,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "digite novamente a senha"
            }
        )
    )

    def clean_username(self):
        name = self.cleaned_data.get('username')

        if name:
            name = name.strip()
            if ' ' in name:
                raise forms.ValidationError('Não utilize espaços no nome de usuário.')
            elif not name.islower():
                raise forms.ValidationError("Nome de usuário não deve conter letras maiúsculas.")
            else:
                return name
            
    def clean_password_2(self):
        pass_1 = self.cleaned_data.get('password_1')
        pass_2 = self.cleaned_data.get('password_2')

        if pass_1 and pass_2:
            if pass_1 != pass_2:
                raise forms.ValidationError("As senhas não são iguais!")
            elif len(pass_2) < 8:
                raise forms.ValidationError("A senha deve conter pelo menos 8 caracteres.")
            elif pass_2.lower() == pass_2:
                raise forms.ValidationError("A senha deve conter pelo menos um caractere maiúsculo.")
            elif pass_2.upper() == pass_2:
                raise forms.ValidationError("A senha deve conter pelo menos um caractere minúsculo.")
            else:
                return pass_2

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Usuário",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"digite seu nome de usuário"
            }
        )
    )

    password = forms.CharField(
        label="Senha",
        required=True,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"digite sua senha"
            }
        )
    )