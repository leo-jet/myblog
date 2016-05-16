from django import forms

from .models import SignUp

class ContactForm(forms.Form):
    full_name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField()
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        #validation code
        return email
    
    def clean_full_name(self):
        full_name = self.cleaned_data.get("full_name")
        #validation code
        return full_name

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = [ "email", "full_name"]
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        #validation code
        return email
    
    def clean_full_name(self):
        full_name = self.cleaned_data.get("full_name")
        #validation code
        return full_name