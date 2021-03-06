from django.db import models


class Film(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False, verbose_name='Название')
    production_year = models.PositiveIntegerField(validators=[MinValueValidator(1895), MaxValueValidator(datetime.now().year)])
    director = models.CharField(max_length=200, blank=False, null=False, verbose_name='режиссер')
    duration = models.PositiveIntegerField(blank=False, null=False, verbose_name='продолжительность')
    description = models.TextField(blank=False, null=False, verbose_name='описание')

    def __str__(self):
        return self.title


class Review(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False, verbose_name='заголовок', default='')
    author = models.CharField(max_length=200, blank=False, null=False, verbose_name='автор')
    text = models.TextField(blank=False, null=False, verbose_name='содержание')
    film = models.ForeignKey(to=Film, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=200, blank=False, null=False, verbose_name='автор')
    comment_text = models.TextField(blank=False, null=False, verbose_name='содержание')
    review = models.ForeignKey(to=Review, on_delete=models.CASCADE)

