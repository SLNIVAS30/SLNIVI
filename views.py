from django.http import HttpResponse

def MyBlog(request):
    return HttpResponse("MyBlog!")