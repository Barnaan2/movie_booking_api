from django.core.management.base import BaseCommand
from  user.forms import NewUserCreationForm
class Command(BaseCommand):
    def handle(self, *args, **options):
        phone_number = input("Enter Phone Number: ")
        password1 = input(" Enter your password: ")
        password2 = input(" Enter your password again:  ")
        data = {"phone_number":phone_number,"password1":password1,"password2":password2}
        form = NewUserCreationForm(data)
        if form.is_valid():
          super_user =  form.save(commit=False)
          super_user.is_superuser=True
          super_user.is_staff = True
          super_user.is_active = True
          super_user.save()
          print(" you have created your superuser successfully ")
        else:
            print("There is some error in your input.....")
        