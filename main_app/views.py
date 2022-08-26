from django.shortcuts import render, redirect
from .models import Bird
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
    #   return render(request, 'main_app/home.html')
    birds = Bird.objects.all()
    return render(request, 'main_app/home.html', {'birds': birds})


def about(request):
    return render(request, 'main_app/about.html')


def bird_detail(request, bird_id):
    bird = Bird.objects.get(id=bird_id)
    return render(request, 'main_app/bird.html', {'bird': bird})

class BirdCreate(LoginRequiredMixin, CreateView):
    model = Bird
    fields = ['title', 'scientific_name', 'conservation_status', 'image', 'family', 'date', 'description']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BirdUpdate(LoginRequiredMixin, UpdateView):
    model = Bird
    fields = ['title', 'scientific_name', 'conservation_status', 'image', 'family', 'description']

class BirdDelete(LoginRequiredMixin, DeleteView):
    model = Bird
    success_url = '/'

@login_required
def user_detail(request):
    bird_user = Bird.objects.filter(user=request.user)
    return render(request, 'main_app/user_page.html', {'bird_user': bird_user})


def signup(request):
    error_message = ''
    # if the user is posting
    if request.method == 'POST':
        # get the data out of the form post request
        form = UserCreationForm(request.POST)
        # if the form passes validation
        if form.is_valid():
            # save the user to the database
            user = form.save()
            # login the user
            login(request, user)
            # redirect to /cats
            return redirect('/')
        else:
            # if the form is not valid, send an error message
            error_message = 'Invalid sign up - try again'
    # GET or bad POST requests
    # generate an empty user creation form
    form = UserCreationForm()
    # pass in the form and any error messages to context
    context = {'form': form, 'error_message': error_message}
    # render the template with the context data
    return render(request, 'registration/signup.html', context)