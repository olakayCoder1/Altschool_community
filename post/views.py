from django.shortcuts import render , get_object_or_404 , redirect 
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Post, Comment
from account.models import User

# Create your views here.






class PostListView(ListView):
    model = Post
    template_name = 'post/postsList.html'
    

@login_required
def posts_list_view(request):
    posts = Post.objects.all()
    context = { 
        'posts':posts
    }
    return render(request, 'post/postsList.html', context)


@login_required
def create_post(request):
    user = User.objects.get(id=request.user.id)
    print(request.POST)
    return redirect('posts_list')
      
@login_required
def delete_post(request,id):
    post_to_delete = get_object_or_404(Post , id=id )
    post_to_delete.delete()
    return redirect('posts_list')

@login_required
def create_comment(request,id):
    post_to_add_comment = get_object_or_404(Post,id=id )
    user = User.objects.get(id=request.user.id)
    if request.method ==  'POST':
        data = request.POST.get('content')
        Comment.objects.create(content=data, user=user  , post=post_to_add_comment)
    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def delete_comment(request,id):
    comment_to_delete = get_object_or_404(Comment , id=id )
    comment_to_delete.delete()
    return redirect(request.META.get('HTTP_REFERER'))
