from django import forms

# created form from model 
# creating form form scratch

class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField()

    # def save(self):
    #     user = model.objects.create_user(username=un, password=password1, email=email)
    #     user.save()


# HTML INPUT FIELDS <----> widgets
# input:text   <---> TextInput
# input:password   <---> PasswordInput
# input:email   <---> EmailInput
# input:number   <---> EmailInput

# input:email --> <input type="email" >

# FormField vs widget
# 