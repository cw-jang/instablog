from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.core.urlresolvers import reverse
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

from .models import Category
from .models import Post
from .models import Tag
from .forms import PostForm

# TEMP:
from django.contrib.auth import get_user_model


@login_required
def create_post(request):
    # 이곳에 글을 저장하는 코드를 작성하세요.

    if request.method == 'GET':
        form = PostForm()
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            post.user = request.user
            
            # TEMP: 로그인처리가 제대로 안되는것 같아서 확인용 임시코드
            # User = get_user_model()
            # u1 = User.objects.last()
            # post.user1 = u1

            post.save()
            
            # 저장한 글(post)의 pk를(post.pk) 이곳에 할당하세요.
            post_pk = post.pk
            return redirect('blogtest:view_post', pk=post.pk)
        
    categories = Category.objects.all()
    return render(request, 'edit.html', {
        'categories': categories,
        'form': form
    })


@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.user == post.user:
        post.delete()
        return redirect('blogtest:list_posts')
    else:
        return HttpResponseForbidden()


@login_required
def view_post(request, pk):
    # 글을 가져와서 post 에 담으세요.
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'view_post.html', {
        'post': post,
    })


def list_posts(request):
    # 글 전체를 가져와서 posts 에 담으세요.
    # posts = None
    posts =  Post.objects.all()

    return render(request, 'list_posts.html', {
        'posts': posts,
    })
