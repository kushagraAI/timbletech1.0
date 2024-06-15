import pandas as pd
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from tmdb_api.models import Review, Tmdb_Movie, Recommendation
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split


class Command(BaseCommand):
    help = 'Compute movie recommendations based on user reviews'

    def handle(self, *args, **kwargs):
        # Clear existing recommendations
        Recommendation.objects.all().delete()

        # Load the data into a pandas dataframe
        reviews = Review.objects.all()
        data = {
            'user_id': [review.user.id for review in reviews],
            'movie_id': [review.movie.id for review in reviews],
            'rating': [review.rating for review in reviews]
        }
        df = pd.DataFrame(data)

        # Load the data into Surprise's Dataset
        reader = Reader(rating_scale=(1, 5))
        surprise_data = Dataset.load_from_df(
            df[['user_id', 'movie_id', 'rating']], reader)

        # Split the data into training and test sets
        trainset, testset = train_test_split(surprise_data, test_size=0.25)

        # Use the SVD algorithm
        algo = SVD()
        algo.fit(trainset)

        # Make predictions for all users and movies
        for user in User.objects.all():
            for movie in Tmdb_Movie.objects.all():
                pred = algo.predict(user.id, movie.id)
                if pred.est >= 3.0:  # Recommend movies with a predicted rating of 3.0 or higher
                    Recommendation.objects.create(
                        user=user, movie=movie, score=pred.est)

        self.stdout.write(self.style.SUCCESS(
            'Successfully computed recommendations'))
