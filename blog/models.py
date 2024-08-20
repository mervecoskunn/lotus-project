from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    img = models.ImageField(upload_to='posts', null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(
        get_user_model(), verbose_name=_('Author'),
        help_text=_('Post creator'),
        on_delete=models.PROTECT,
        related_name='user_posts',
        blank=True
    )
    date_posted = models.DateTimeField(default=timezone.now)

    like = models.ManyToManyField(
        get_user_model(),
        related_name='post_likes',
        blank=True
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    A comment on a post, with an author, post, body, and creation date.
    """
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='user_comments',
        verbose_name='Comment Creator',
        help_text='Comment creator'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.PROTECT,
        related_name='post_comments', verbose_name='Post',
        help_text='Select the post to which this comment will be associated.'
    )
    body = models.TextField()
    created_on = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created On',
        help_text='The date and time the comment was created.',
    )

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ('-created_on',)

    def __str__(self):
        return self.post.__str__()


class DraftPost(models.Model):
    img = models.ImageField(upload_to='drafts', null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.name) + ' - ' + str(self.email)


class Newsletter(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email
