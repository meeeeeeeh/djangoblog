from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, verbose_name='Автор'
    )
    title = models.CharField(
        max_length=56, verbose_name='Название'
    )
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now, verbose_name='Текст'
    )

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост')
    author = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, verbose_name='Автор'
    )
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now, verbose_name='Текст'
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.post}: {self.author}: {self.pk}'

