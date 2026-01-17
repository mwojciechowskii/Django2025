from django.shortcuts import get_object_or_404, render

from .models import Category, Post

def postListView(request, categoryName=None):

    if categoryName:
        queryset = Post.objects.filter(isPublic=True, categoryName=categoryName)
    else:
        queryset = Post.objects.all()

    queryset = queryset.filter(isPublic=True).order_by("-datePublish")
    context = { 'categoryList': Category.objects.all(),
        'objectList': queryset,
        'categoryName': categoryName}

    return render(request, 'blog/postList.html', context)

def postDetailView(request, postID):
    
    post = get_object_or_404(Post, id=postID)
    context = { 'object': post,
        'categoryList': Category.objects.all(),
        'categoryName': post.category.name if post.category else 'Uncategorized' }

    return render(request, 'blog/postDetail.html', context)

