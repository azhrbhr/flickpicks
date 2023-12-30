from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from movies.models import Movie, WatchedMovie
from django.views.generic import ListView


class MovieRecommender:
    @staticmethod
    def get_watch_history(user):
        return WatchedMovie.objects.filter(user=user).values_list('movie', flat=True)

    @staticmethod
    def get_recommendations(user):
        watched_movies = MovieRecommender.get_watch_history(user)
        similar_users = WatchedMovie.objects.filter(movie__in=watched_movies).exclude(
            user=user).values_list('user', flat=True)

        similar_movie_ids = WatchedMovie.objects.filter(
            user__in=similar_users).values_list('movie__id', flat=True)

        watched_movie_ids = watched_movies.values_list('id', flat=True)

        recommended_movie_ids = set(similar_movie_ids) - set(watched_movie_ids)

        # Retrieve recommended movies excluding the ones watched by the current user
        recommended_movies = Movie.objects.filter(
            id__in=recommended_movie_ids).exclude(id__in=watched_movie_ids)

        return recommended_movies


class HomePageView(LoginRequiredMixin, ListView):
    template_name = "home/home.html"
    context_object_name = 'recommended_movies'

    def get_queryset(self):
        user = self.request.user
        recommendations = MovieRecommender.get_recommendations(user)
        return recommendations
