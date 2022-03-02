from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# Create your views here.
posts = Post.objects.all();

@login_required
def Index(request):
    context ={'Post':posts}
    return render(request,"Blog/Index.html",context);

def About(request):
        return render(request,"Blog/About.html");

class PostListView(LoginRequiredMixin,ListView):
    model=Post
    template_name='Blog/Index.html'
    context_object_name='Post'
    ordering=['-Date_posted']

class PostDetailView(LoginRequiredMixin,DetailView):
    model= Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields=['Title','Content']
    success_url='/'

    def form_valid(self, form):
        form.instance.Author=self.request.user
        return super().form_valid(form)

class PostEditView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['Title','Content']
    success_url='/'

    def test_func(self):
        post =self.get_object()
        if (self.request.user==post.Author):
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url='/'

    def test_func(self):
        post =self.get_object()
        if (self.request.user==post.Author):
            return True
        else:
            return False



