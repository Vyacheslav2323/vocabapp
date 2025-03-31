from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


Language_Choices = [
    ('en','English'),
    ('kr', 'Korean'),
    ('ch', 'Chinese'),
    ('ru', 'Russian'),
    ('kz', 'Kazakh'),

]
class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    country = forms.CharField()
    first_language = forms.ChoiceField(choices=Language_Choices)
    target_language = forms.ChoiceField(choices=Language_Choices)
    class Meta:
        model = User
        fields = ('username', 'email', 'country', 'first_language', 'target_language', 'password1', 'password2')
