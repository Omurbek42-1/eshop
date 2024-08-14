from django.db import models

class Review(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    content = models.TextField()
    stars = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)], default=1)

    def __str__(self):
        return f'Review for {self.movie.title} by {self.user.username}'

class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.ForeignKey('Director', on_delete=models.CASCADE, related_name='movies')

    def __str__(self):
        return self.title

class Director(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
