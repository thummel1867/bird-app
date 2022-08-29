from django.shortcuts import render, redirect
from .models import Bird, User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.db.models import Q
# Create your views here.


class SearchResultsView(ListView):
    model = Bird
    template_name = 'main_app/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Bird.objects.filter(
            Q(title__icontains=query) | Q(scientific_name__icontains=query) | Q(
                conservation_status__icontains=query) | Q(family__icontains=query) | Q(description__icontains=query)
        )
        return object_list


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
    fields = ['title', 'scientific_name',
              'conservation_status', 'image', 'family', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BirdUpdate(LoginRequiredMixin, UpdateView):
    model = Bird
    fields = ['title', 'scientific_name',
              'conservation_status', 'image', 'family', 'description']
    success_url = '/'


class BirdDelete(LoginRequiredMixin, DeleteView):
    model = Bird
    success_url = '/'


def user_page(request, user_id, user):
    bird_user = Bird.objects.filter(user=user_id)
    user_seen = bird_user.seen.all().values_list('id')
    birds = Bird.objects.exclue(id__in=user_seen)
    return render(request, 'main_app/user_page.html', {'bird_user': bird_user, 'birds': birds})


@login_required
def user_detail(request):
    bird_user = Bird.objects.filter(user=request.user)
    return render(request, 'main_app/user_page.html', {'bird_user': bird_user})


# go through the birds and return the one's with the user that matches user

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


@login_required
def seen_bird(request, user_id, bird_id):
    bird = Bird.objects.get(id=bird_id)
    user = User.objects.get(id=user_id)
    bird.seen.add(user)
    return redirect('/')

@login_required
def searching_bird(request, user, bird_id):
    bird = Bird.objects.get(id=bird_id)
    bird.searching.add(user)
    return redirect('/')
