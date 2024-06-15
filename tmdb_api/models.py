from django.db import models
from django.contrib.auth.models import User


class Tmdb_Movie(models.Model):
    tmdb_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    overview = models.TextField()
    release_date = models.DateField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    poster_path = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title

    def poster_url(self):
        if self.poster_path:
            return f"https://image.tmdb.org/t/p/w500{self.poster_path}"
        return "https://via.placeholder.com/500x750?text=No+Image"


class Review(models.Model):
    movie = models.ForeignKey(Tmdb_Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.movie.title}"


class Comment(models.Model):
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name="review_set")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.review.movie.title}"


class Recommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Tmdb_Movie, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return f"{self.user.username} - {self.movie.title}"
