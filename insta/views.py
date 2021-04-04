from django.shortcuts import render
from django.views import View
from .models import post
from .forms import PostForm
# Create your views here.


class PostListView(View):
    def get(self, request, *args, **kwargs):
        posts = post.objects.all().order_by('created_on')
        form =PostForm

        context = {
            'post_list': posts,
            'form': form,
        }

        return render(request, 'insta/post_list.html', context)

    def post(self, request, *args, **kwargs):
        posts = post.objects.all().order_by('created_on')
        form = PostForm(request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()

            context = {
            'post_list': posts,
            'form': form,
        }

        return render(request, 'insta/post_list.html', context)

class PostDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        post = post.object.get(pk=pk)

        context = {
            'post': post
        }

        return render(request, 'insta/post_detail.html', context)