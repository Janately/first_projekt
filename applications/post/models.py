from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()


class Shoes(models.Model):
    """
        Моделька обуви
    """
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='shoes', verbose_name='Продавец'
    )
    title = models.CharField('Название', max_length=70)
    description = models.TextField('Описание', blank=True, null=True)
    count_views = models.PositiveIntegerField('Количество просмотров', default=0)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('-id',)


class ShoesImage(models.Model):
    """
        Картинки обуви
    """
    image = models.ImageField(upload_to='images/')
    film = models.ForeignKey(
        Shoes, on_delete=models.CASCADE,
        related_name='images'
    )

    def str(self):
        return f'{self.film.title}'

class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    film = models.ForeignKey(Shoes, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.owner} -> {self.post.title}'


class Like(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='likes'
    )
    post = models.ForeignKey(
        Shoes, on_delete=models.CASCADE,
        related_name='likes'
    )
    is_like = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.owner} liked - {self.post.title}'


class Rating(models.Model):
    owner = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='ratings')
    post = models.ForeignKey(Shoes,
                              on_delete=models.CASCADE,
                              related_name='ratings')
    rating = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ], blank=True, null=True)

    def __str__(self):
        return f'{self.owner} --> {self.post.title}'

