from django.contrib import admin
from .models import Tmdb_Movie, Review, Comment, Recommendation

admin.site.register(Tmdb_Movie)
admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(Recommendation)
# Register your models here.
