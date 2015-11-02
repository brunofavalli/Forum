from django import forms

class RegistrerForm(forms.Form):
    user = forms.CharField(label='Usuário')
    email = forms.EmailField(label='E-mail')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    avatar = forms.ImageField()

class LoginForm(forms.Form):
    user = forms.CharField(label='Usuário')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

class ProfileForm(forms.Form):
    avatar = forms.ImageField()

class ThreadPostForm(forms.Form):
    title = forms.CharField(label='Título')
    body = forms.CharField(label='Conteúdo', widget=forms.Textarea)
