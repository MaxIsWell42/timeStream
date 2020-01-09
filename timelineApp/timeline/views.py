from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Event, Timeline
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User


def index(request):
    return render(request, 'timeline/home.html')

class TimelineListView(ListView):
    model = Timeline
    template_name = 'Timelines/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'Timelines'
    # ordering = ['-date_posted'] # to order from newest to oldest
    paginate_by = 5

class UserTimelineListView(ListView):
    model = Timeline
    template_name = 'timeline/user_timelines.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'Timelines'
    # ordering = ['-date_posted'] # to order from newest to oldest
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Timeline.objects.filter(author=user).order_by('-date_posted')

class TimelineDetailView(DetailView):
    model = Timeline

class TimelineCreateView(LoginRequiredMixin, CreateView):
    model = Timeline
    fields = ['title'], ['description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TimelineUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Timeline
    fields = ['title'], ['description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class TimelineDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Timeline

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'timeline/about.html', {'title': 'About'})