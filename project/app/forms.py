from django import forms
from .models import User, Task

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields ='__all__'


    def check_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(Email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields ='__all__'


    user = forms.ModelChoiceField(queryset=User.objects.all(), empty_label="Select User")
