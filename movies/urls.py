from django.urls import path
from movies.views import MovieListView, MovieDetailView, MarkOrUnmarkAsWatchedView

urlpatterns = [
    path('', MovieListView.as_view(), name='movie-list'),
    path('<slug:slug>/', MovieDetailView.as_view(), name='movie-detail'),
    path('<slug:slug>/mark_or_unmark_as_watched/',
         MarkOrUnmarkAsWatchedView.as_view(), name='mark-or-unmark-as-watched'),

]
