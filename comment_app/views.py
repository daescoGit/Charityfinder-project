from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Comment, UserCommentRating


def project_comments(request, pid):
    comments = Comment.objects.filter(project_id=pid)  # .order_by('-rated', '-created')

    context = {
        'pid': pid,
        'comments': comments,
    }
    return render(request, 'comment_app/comments.html', context)


@login_required  # alt: request.user.is_authenticated check
def new_comment(request, pid):
    if request.method == 'POST':
        text = request.POST['newComment']
        comment = Comment()
        comment.body = text
        comment.author = request.user
        comment.project_id = pid
        if "reply" in request.POST:
            comment.parent = Comment.objects.get(pk=request.POST['reply'])
        comment.save()
        print('comment saved')
        return redirect(reverse('charityfinder_app:project', args={pid}))
    else:
        print('not authorized to comment')


@login_required
def new_comment_rating(request, pid):
    if request.method == 'POST':
        # "defaults" only execute when create, created = boolean
        # also protects against race conditions
        rated, created = UserCommentRating.objects.get_or_create(
            user=request.user,
            comment=Comment.objects.get(pk=request.POST['reply']),
            defaults={'state': request.POST['comment_rating']},
        )
        if not created:
            rated.state = request.POST['comment_rating']
            rated.save()
            print('comment rating updated')
        else:
            print('comment rating created')
        return redirect(reverse('charityfinder_app:project', args={pid}))
    else:
        print('not authorized to vote')


@login_required
def delete_comment(request, pid):
    if request.method == 'POST':
        comment = get_object_or_404(Comment, author=request.user, pk=request.POST['reply'])
        comment.body = 'Deleted'
        comment.save()
        print('comment deleted')
        return redirect(reverse('charityfinder_app:project', args={pid}))
    else:
        print('not authorized to delete')
