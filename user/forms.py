from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from user.models import User,Profile



# user camelCase for class names
class NewUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'phone_number', 'password1', 'password2']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [ 'name', 'email','profile_picture']