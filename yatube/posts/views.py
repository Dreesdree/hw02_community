from django.shortcuts import render, get_object_or_404

from posts.models import Post, Group


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
        'title': 'Главная страница Yatube',
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:10]
    context = {
        'group': group,
        'posts': posts,
        'title': 'Посты выбранной вами группы',
    }
    return render(request, 'posts/group_list.html', context)
