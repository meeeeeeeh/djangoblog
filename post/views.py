from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.shortcuts import redirect


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post/post_list.html', {'posts': posts})


def post_detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    comments = Comment.objects.filter(post=post_pk)
    comment_form = CommentForm()
    return render(request, 'post/post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
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
    post = get_object_or_404(Post, pk=comment.post.pk)
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

