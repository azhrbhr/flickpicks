from django.contrib import admin
from movies.models import Genre, Movie


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('genres',)
    search_fields = ('title',)
    filter_horizontal = ('genres',)


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
