from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator

from .models import Category, Post

def postListView(request, categoryName=None, authorName=None):

    queryset = Post.objects.all()
    if categoryName:
        queryset = Post.objects.filter(isPublic=True, category__name__iexact=categoryName)
    if authorName:
        queryset = Post.objects.filter(isPublic=True, author__name__iexact=authorName)

    queryset = queryset.filter(isPublic=True).order_by("-datePublish")

    paginator = Paginator(queryset, 4)
    pageNo = request.GET.get("page")
    pageObj = paginator.get_page(pageNo)
    context = { 'categoryList': Category.objects.all(),
               'objectList': pageObj,
               'categoryName': categoryName,
               'authorName': authorName}

    return render(request, 'blog/postList.html', context)

def postDetailView(request, postID):
    
    post = get_object_or_404(Post, id=postID)
    context = { 'object': post,
        'categoryList': Category.objects.all(),
        'categoryName': post.category.name if post.category else 'Uncategorized' }

    return render(request, 'blog/postDetail.html', context)

