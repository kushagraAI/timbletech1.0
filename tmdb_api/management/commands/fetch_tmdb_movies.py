import os
import requests
from django.core.management.base import BaseCommand
from tmdb_api.models import Tmdb_Movie
from dotenv import load_dotenv
load_dotenv()


class Command(BaseCommand):
    help = 'Fetch movies from TMDB API and save to database'

    def handle(self, *args, **kwargs):
        API_KEY = os.getenv("API_KEY")
        url = f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}'

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for movie_data in data['results']:
                Tmdb_Movie.objects.update_or_create(
                    tmdb_id=movie_data['id'],
                    defaults={
                        'title': movie_data['title'],
                        'overview': movie_data['overview'],
                        'release_date': movie_data['release_date'],
                        'vote_average': movie_data['vote_average'],
                        'vote_count': movie_data['vote_count'],
                        'poster_path': movie_data['poster_path'],
                    }
                )
            self.stdout.write(self.style.SUCCESS(
                'Successfully fetched and saved movies from TMDB API'))
        else:
            self.stdout.write(self.style.ERROR(
                'Failed to fetch data from TMDB'))
