from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Post
from .models import Category
from .models import Comment
from .forms import PostForm


def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post = comment.post
    comment.delete()
    return redirect('blog:view_post', post.pk)

def create_comment(request, pk):
    if request.method == 'POST':
        form = request.POST
        post = get_object_or_404(Post, pk=pk)
        comment = Comment(
            post=post,
            content=form['comment']
            )
        comment.save()
        return redirect('blog:view_post', pk)

    return view_post(request, pk)

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog:list_posts')

    return render(request, 'delete.html', {
        'post': post
        })

def edit_post(request, pk):
    if request.method == 'GET':
        post = get_object_or_404(Post, pk=pk)
        categories = Category.objects.all()
    else:
        return create_post(request)

    return render(request, 'edit.html', {
        'post': post, 
        'categories': categories
        })

# def create_post(request):
#     if request.method == 'GET':
#         form = PostForm()
#         categories = Category.objects.all()
#         ctx = {
#             'categories': categories,
#             'form': form
#         }
#     elif request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             Post(
#                 title=form.cleaned_data['title'],
#                 content=form['content'],
#                 )
#             post.save()
#             return retirect('blog:view_post', pk=post.pk)

#     return render(request, 'edit.html', {
#         'form': form,})

@login_required
def create_post(request):

    # if not request.user.is_authenticated():
    #     raise Exception('님 로그인 안함.')

    messages.add_message(request, messages.ERROR, '메시지 테스트!!')
    messages.add_message(request, messages.INFO, '메시지 테스트!!')

    if request.method == 'GET':
        form = PostForm()
        
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('blog:view_post', pk=post.pk)

    categories = Category.objects.all()
    ctx = {
        'categories': categories,
        'form': form
    }
    return render(request, 'edit.html', ctx)

def list_posts(request):
    page = request.GET.get('page', 1)
    per_page = 5

    posts = Post.objects.order_by('-created_at')
    pg = Paginator(posts, per_page)

    try:
        contents = pg.page(page)
    except PageNotAnInteger:
        contents = pg.page(1)
    except EmptyPage:
        contents = []

    return render(request, 'list.html', {
        'posts': contents,
        })


def view_post(request, pk):
    if request.method == 'POST':
        form = request.POST
        post = get_object_or_404(Post, pk=pk)
        comment = Comment(
            post=post,
            content=form['comment']
            )
        comment.save()
        url = reverse('blog:view_post', kwargs={'pk':pk})
        return redirect(url)
    
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'view.html', {
        'post': post
        })