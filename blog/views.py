from django.shortcuts import render

from .models import Post

def postListView(request):

    queryset = Post.objects.filter(isPublic=True).order_by("-datePublish")
    context = {
        'objectList': queryset
    }
    return render(request, 'blog/postList.html', context)
