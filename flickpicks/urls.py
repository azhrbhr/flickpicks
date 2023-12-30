from django.contrib import admin
from django.urls import path, include
from flickpicks.views import HomePageView
from django.conf import settings
from django.conf.urls.static import static
from movies.views import WatchedMovieListView
urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("movies/", include("movies.urls")),
    path('watched/', WatchedMovieListView.as_view(), name='watched-movie-list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
