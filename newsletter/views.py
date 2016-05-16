from django.shortcuts import render
from .forms import SignUpForm
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