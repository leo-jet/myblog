from django.shortcuts import render
from .forms import SignUpForm
from .forms import ContactForm
# Create your views here.
def home(request):
    title = "My Title"
    #add a form
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)#on enregistre pas encore dans la ase
        print(instance)
        instance.save()
    context = {
               "template_title": title,
               "form": form,
               }
    return render(request, "home.html", context)

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get("email")
        message = form.cleaned_data.get("message")
        full_name = form.cleaned_data.get("full_name")
        print(email, message, full_name)
    context = {
               "contact_form": form,
               }
    return render(request, "contact.html", context)