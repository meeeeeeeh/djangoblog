from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment, Tag, Category
from django.db.models import Count
from .forms import PostForm, CommentForm
from django.shortcuts import redirect


def post_list(request):
    posts = Post.objects.filter(draft=False)
    tags = Tag.objects.all()
    categories = Category.objects.all()
    return render(request, 'post/post_list.html', {'posts': posts, 'tags': tags, 'categories': categories})


def draft_list(request):
    posts = Post.objects.filter(draft=True)
    return render(request, 'post/post_list.html', {'posts': posts})


def post_detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    tags = post.tag.all()
    rating_values = post.rating.all()
    # tags = tag.posts.all()
    rating = 0
    for element in rating_values:
        rating += element.rating
    if len(rating_values) != 0:
        rating //= len(rating_values)

    comments = Comment.objects.filter(post=post_pk)
    comment_form = CommentForm()
    post.view += 1
    post.save()
    return render(request, 'post/post_detail.html',
                  {'post': post, 'comments': comments, 'comment_form': comment_form,
                   'tags': tags, 'rating': rating})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', post_pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post/post_new.html', {'form': form})


def post_edit(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', post_pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post/post_new.html', {'form': form})


def delete_post(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    post.delete()
    return redirect(post_list)


def delete_comment(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    post_pk = comment.post.pk
    return redirect(post_detail, post_pk=post_pk)


def comment_new(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect(post_detail, post_pk=comment.post.pk)
    else:
        comment_form = CommentForm()
    return render(request, 'post/comment_new.html', {'comment_form': comment_form})


def comment_edit(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == "POST":
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.save()
            return redirect(post_detail, post_pk=comment.post.pk)
    else:
        comment_form = CommentForm(instance=comment)
    return render(request, 'post/comment_new.html', {'comment_form': comment_form})


def post_like_or_dislike(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.GET.get('like') == 'like':
        post.likes += 1
        post.save()
    if request.GET.get('dislike') == 'dislike':
        post.dislikes += 1
        post.save()
    return redirect('post_detail', post_pk=post.pk)


def publish(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    post.draft = False
    post.save()
    return redirect('post_detail', post_pk=post.pk)


def tag_list(request, tag_pk):
    tag = get_object_or_404(Tag, pk=tag_pk)
    posts = tag.posts.all()
    return render(request, 'post/post_list.html', {'posts': posts})


def category_posts(request, category_pk):
    category = get_object_or_404(Tag, pk=category_pk)
    posts = category.posts.all()
    return render(request, 'post/post_list.html', {'posts': posts})


def recommendations(request):
    posts_by_likes = Post.objects.all().order_by('-likes')[:10]
    posts_by_views = Post.objects.all().order_by('-view')[:10]
    posts_by_comments = Post.objects.all().annotate(cnt=Count('comments')).order_by('-cnt')[:10]
    return render(request, 'post/recommendations.html', {'posts_by_likes': posts_by_likes,
                                                         'posts_by_views': posts_by_views,
                                                         'posts_by_comments': posts_by_comments})


def add_to_favorite(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    post.favorite = True
    post.save()
    return redirect('post_detail', post_pk=post.pk)


def favorites(request):
    posts = Post.objects.filter(favorite=True)
    return render(request, 'post/post_list.html', {'posts': posts})





