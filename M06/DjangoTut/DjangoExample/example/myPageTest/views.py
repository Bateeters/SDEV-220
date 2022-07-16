from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Post

Post.ojbects.filter(published_date__lte=timezone.now()
                    ).order_by('published_date')

# Create your views here.


def Home(request):
    page = """
    <html>
    
        <head>
            <title>Test Page</title>
        </head>

        <body>
            <h1>Hello World!</h1>
        </body>

    </html>
    
    """

    return HttpResponse(page)


def Other(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, "otherPage.html", {"title": "Other Page", "message": "This is my second page!", "posts": posts})
