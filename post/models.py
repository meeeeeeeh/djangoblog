from django.db import models
from django.utils import timezone


class Tag(models.Model):
    tag_name = models.CharField(max_length=24, verbose_name='Тег')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return f'{self.tag_name}'


class Category(models.Model):
    category_name = models.CharField(max_length=24, verbose_name='Категория')

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


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
    view = models.IntegerField(default=0, verbose_name='Просмотры')
    likes = models.IntegerField(default=0, verbose_name='Лайки')
    dislikes = models.IntegerField(default=0, verbose_name='Дизлайки')
    draft = models.BooleanField(default=True, verbose_name='Черновик')
    tag = models.ManyToManyField(Tag, related_name='posts', verbose_name='Теги', blank=True)
    cover = models.ImageField(upload_to='images/', default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts',
                                 default=1, verbose_name='Категория')
    favorite = models.BooleanField(default=False, verbose_name='Избранное')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f'{self.title}'

    @property
    def comments(self):
        comments = Comment.objects.filter(post=self.pk)
        return comments.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост', related_name='comments')
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


class Rating(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, verbose_name='Пост', related_name='rating')
    rating = models.IntegerField(verbose_name='Рейтинг')

    def __str__(self):
        return f'{self.rating}'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинг'
