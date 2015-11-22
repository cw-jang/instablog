from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

from .models import Post
from .models import Category


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

def create_post(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        ctx = {
            'categories': categories,
        }
    else:
        form = request.POST
        category = get_object_or_404(Category, pk=form['category'])
        post = Post(
            title=form['title'],
            content=form['content'],
            category=category,
            )
        post.full_clean()
        post.save()
        url = reverse('blog:view_post', kwargs={'pk':post.pk})
        return redirect(url)

    return render(request, 'edit.html', ctx)

def list_posts(request):
    page = request.GET.get('page', 1)
    per_page = 2

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
    # post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'view.html', {
        'post': post
        })