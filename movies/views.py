from django.views import View
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from movies.models import Movie, WatchedMovie


class MovieRecommender:
    @staticmethod
    def calculate_jaccard_similarity(movie1_genres, movie2_genres):
        set1 = set(movie1_genres)
        set2 = set(movie2_genres)
        intersection = len(set1.intersection(set2))
        union = len(set1.union(set2))
        return intersection / union if union != 0 else 0.0

    @staticmethod
    def get_similar_movies(movie, threshold=0.3):
        similar_movies = []
        all_movies = Movie.objects.exclude(id=movie.id)

        for other_movie in all_movies:
            similarity = MovieRecommender.calculate_jaccard_similarity(
                movie.genres.all(), other_movie.genres.all()
            )
            if similarity >= threshold:
                similar_movies.append(other_movie)

        return similar_movies


class MovieListView(ListView):
    model = Movie
    context_object_name = 'movies'


class MovieDetailView(LoginRequiredMixin, DetailView):
    model = Movie
    context_object_name = 'movie'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        movie = self.get_object()
        similar_movies = MovieRecommender.get_similar_movies(movie)
        watched = False

        if self.request.user.is_authenticated:
            watched = WatchedMovie.objects.filter(
                user=self.request.user, movie=movie).exists()

        context['watched'] = watched
        context['similar_movies'] = similar_movies
        return context


class MarkOrUnmarkAsWatchedView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        movie = get_object_or_404(Movie, slug=self.kwargs.get('slug'))
        watched, created = WatchedMovie.objects.get_or_create(
            user=request.user, movie=movie)

        if created:
            # Movie was marked as watched
            return redirect('movie-detail', slug=self.kwargs.get('slug'))
        else:
            # Movie was unmarked as watched
            watched.delete()
            return redirect('movie-detail', slug=self.kwargs.get('slug'))


class WatchedMovieListView(LoginRequiredMixin, ListView):
    model = WatchedMovie
    context_object_name = 'watched_movies'

    def get_queryset(self):
        return WatchedMovie.objects.filter(user=self.request.user)
