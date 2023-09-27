from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label='Nome de usuário', max_length=100)
    password = forms.CharField(label='Senha', max_length=100, widget=forms.PasswordInput)

    class Meta:
        fields = ['username', 'password']
