from django.core.management.base import BaseCommand
from movies.models import Genre


class Command(BaseCommand):
    help = 'Creates initial genres'

    def handle(self, *args, **kwargs):
        genre_names = [
            "Action",
            "Adventure",
            "Comedy",
            "Drama",
            "Fantasy",
            "Horror",
            "Mystery",
            "Romance",
            "Science Fiction",
            "Thriller",
        ]

        for name in genre_names:
            genre, created = Genre.objects.get_or_create(name=name)
            if created:
                genre.save()

        self.stdout.write(self.style.SUCCESS('Genres created successfully'))
