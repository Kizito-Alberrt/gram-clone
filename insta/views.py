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