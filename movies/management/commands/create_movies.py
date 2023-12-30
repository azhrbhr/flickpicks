from django.core.management.base import BaseCommand
from movies.models import Genre, Movie
from django.utils.text import slugify


class Command(BaseCommand):
    help = 'Creates initial movies'

    def handle(self, *args, **kwargs):
        movies_data = [
            {
                'title': 'The Matrix',
                'duration': 136,
                'genres': ['Action', 'Science Fiction'],
                'description': 'A computer hacker learns about the true nature of reality.',
                'poster': None,  # Replace with the path or image file
            },
            {
                'title': 'Pulp Fiction',
                'duration': 154,
                'genres': ['Crime', 'Drama'],
                'description': 'Interconnected stories of criminals in Los Angeles.',
                'poster': None,  # Replace with the path or image file
            },
            {
                'title': 'Forrest Gump',
                'duration': 142,
                'genres': ['Drama', 'Romance'],
                'description': 'A man\'s journey through several decades of American history.',
                'poster': None,  # Replace with the path or image file
            },
            {
                'title': 'Inception',
                'duration': 148,
                'genres': ['Action', 'Adventure', 'Sci-Fi'],
                'description': 'A thief who enters the dreams of others.',
                'poster': None,  # Replace with the path or image file
            },
            {
                'title': 'The Dark Knight',
                'duration': 152,
                'genres': ['Action', 'Crime', 'Drama'],
                'description': 'Batman faces the Joker.',
                'poster': None,  # Replace with the path or image file
            },
            {
                'title': 'The Shawshank Redemption',
                'duration': 142,
                'genres': ['Drama'],
                'description': 'A story of hope and friendship in prison.',
                'poster': None,  # Replace with the path or image file
            },
            {
                'title': 'The Lord of the Rings: The Fellowship of the Ring',
                'duration': 178,
                'genres': ['Adventure', 'Fantasy'],
                'description': 'Frodo Baggins begins his journey to destroy the One Ring.',
                'poster': None,  # Replace with the path or image file
            },
            {
                'title': 'Fight Club',
                'duration': 139,
                'genres': ['Drama'],
                'description': 'An insomniac office worker forms an underground fight club.',
                'poster': None,  # Replace with the path or image file
            },

            {
                'title': 'The Godfather',
                'duration': 175,
                'genres': ['Crime', 'Drama'],
                'description': 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.',
                'poster': None,  # Replace with the path or image file
            },
            {
                'title': 'The Silence of the Lambs',
                'duration': 118,
                'genres': ['Crime', 'Drama', 'Thriller'],
                'description': 'A young FBI cadet must receive the help of an incarcerated and manipulative cannibal killer to help catch another serial killer.',
                'poster': None,  # Replace with the path or image file
            },
            {
                'title': 'The Shining',
                'duration': 146,
                'genres': ['Drama', 'Horror'],
                'description': 'A family heads to an isolated hotel for the winter where a sinister presence influences the father into violence.',
                'poster': None,  # Replace with the path or image file
            },
            {
                'title': 'The Green Mile',
                'duration': 189,
                'genres': ['Crime', 'Drama', 'Fantasy'],
                'description': 'The lives of guards on Death Row are affected by one of their charges: a black man accused of child murder and rape, yet who has a mysterious gift.',
                'poster': None,  # Replace with the path or image file
            },
            {
                'title': 'The Departed',
                'duration': 151,
                'genres': ['Crime', 'Drama', 'Thriller'],
                'description': 'An undercover cop and a mole in the police attempt to identify each other while infiltrating an Irish gang in South Boston.',
                'poster': None,  # Replace with the path or image file
            },
            {
                'title': 'Gladiator',
                'duration': 155,
                'genres': ['Action', 'Adventure', 'Drama'],
                'description': 'A former Roman General sets out to exact vengeance against the corrupt emperor who murdered his family and sent him into slavery.',
                'poster': None,  # Replace with the path or image file
            },
            {
                'title': 'The Godfather: Part II',
                'duration': 202,
                'genres': ['Crime', 'Drama'],
                'description': 'The early life and career of Vito Corleone in 1920s New York City is portrayed, while his son, Michael, expands and tightens his grip on the family crime syndicate.',
                'poster': None,  # Replace with the path or image file
            },
            {
                'title': 'The Prestige',
                'duration': 130,
                'genres': ['Drama', 'Mystery', 'Sci-Fi'],
                'description': 'After a tragic accident, two stage magicians engage in a battle to create the ultimate illusion while sacrificing everything they have to outwit each other.',
                'poster': None,  # Replace with the path or image file
            },
            {
                'title': 'Saving Private Ryan',
                'duration': 169,
                'genres': ['Drama', 'War'],
                'description': 'Following the Normandy Landings, a group of U.S. soldiers go behind enemy lines to retrieve a paratrooper whose brothers have been killed in action.',
                'poster': None,  # Replace with the path or image file
            },
            {
                'title': 'The Usual Suspects',
                'duration': 106,
                'genres': ['Crime', 'Mystery', 'Thriller'],
                'description': 'A sole survivor tells of the twisty events leading up to a horrific gun battle on a boat.',
                'poster': None,  # Replace with the path or image file
            },
            {
                'title': 'The Lion King',
                'duration': 88,
                'genres': ['Animation', 'Adventure', 'Drama'],
                'description': 'Lion cub and future king Simba searches for his identity. His eagerness to please others and penchant for testing his boundaries sometimes gets him into trouble.',
                'poster': None,  # Replace with the path or image file
            },
            {
                'title': 'Goodfellas',
                'duration': 146,
                'genres': ['Biography', 'Crime', 'Drama'],
                'description': 'The story of Henry Hill and his life in the mob, covering his relationship with his wife Karen Hill and his mob partners Jimmy Conway and Tommy DeVito.',
                'poster': None,  # Replace with the path or image file
            },
            {
                'title': 'The Sixth Sense',
                'duration': 107,
                'genres': ['Drama', 'Mystery', 'Thriller'],
                'description': 'A boy who communicates with spirits seeks the help of a disheartened child psychologist.',
                'poster': None,  # Replace with the path or image file
            },
            {
                'title': 'The Social Network',
                'duration': 120,
                'genres': ['Biography', 'Drama'],
                'description': 'As Harvard student Mark Zuckerberg creates the social networking site that would become known as Facebook, he is sued by the twins who claimed he stole their idea, and by the co-founder who was later squeezed out of the business.',
                'poster': None,  # Replace with the path or image file
            },
            {
                'title': 'Avatar',
                'duration': 162,
                'genres': ['Action', 'Adventure', 'Fantasy'],
                'description': 'A paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.',
                'poster': None,  # Replace with the path or image file
            },
            {
                'title': 'The Breakfast Club',
                'duration': 97,
                'genres': ['Comedy', 'Drama'],
                'description': 'Five high school students meet in Saturday detention and discover how they have a lot more in common than they thought.',
                'poster': None,  # Replace with the path or image file
            },
            {
                'title': 'City of God',
                'duration': 130,
                'genres': ['Crime', 'Drama'],
                'description': 'Two boys growing up in a violent neighborhood of Rio de Janeiro take different paths: one becomes a photographer, the other a drug dealer.',
                'poster': None,  # Replace with the path or image file
            },
            {
                'title': 'The Truman Show',
                'duration': 103,
                'genres': ['Comedy', 'Drama', 'Sci-Fi'],
                'description': 'An insurance salesman discovers his whole life is actually a reality TV show.',
                'poster': None,  # Replace with the path or image file
            },
            {
                'title': 'The Terminator',
                'duration': 107,
                'genres': ['Action', 'Sci-Fi'],
                'description': 'A human soldier is sent from 2029 to 1984 to stop an almost indestructible cyborg killing machine, sent from the same year, which has been programmed to execute a young woman whose unborn son is the key to humanity\'s future salvation.',
                'poster': None,  # Replace with the path or image file
            },
            {
                'title': 'The Wizard of Oz',
                'duration': 102,
                'genres': ['Adventure', 'Family', 'Fantasy'],
                'description': 'Dorothy Gale is swept away from a farm in Kansas to a magical land of Oz in a tornado and embarks on a quest with her new friends to see the Wizard who can help her return home to Kansas and help her friends as well.',
                'poster': None,  # Replace with the path or image file
            },
            {
                'title': 'Jurassic Park',
                'duration': 127,
                'genres': ['Action', 'Adventure', 'Sci-Fi'],
                'description': 'A pragmatic paleontologist visiting an almost complete theme park is tasked with protecting a couple of kids after a power failure causes the park\'s cloned dinosaurs to run loose.',
                'poster': None,  # Replace with the path or image file
            },
        ]

        for movie_data in movies_data:
            movie = Movie.objects.create(
                title=movie_data['title'],
                duration=movie_data['duration'],
                description=movie_data['description'],
                poster=movie_data['poster'],
            )
            movie.genres.add(*[Genre.objects.get_or_create(name=genre_name)[0]
                             for genre_name in movie_data['genres']])
            movie.save()

        self.stdout.write(self.style.SUCCESS('Movies created successfully'))
