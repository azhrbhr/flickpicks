
# FlickPicks: Movie Recommender App

FlickPicks is a Django-based movie recommendation application that offers personalized movie suggestions based on user watch history and movie genres using the Jaccard similarity approach.

## Features
- User Authentication: Allows user registration, login, and logout functionalities.
- Movie Database: Stores movie information including title, duration, genres, description, and posters.
- Watch History: Tracks user movie-watching history.
- Movie Recommendations: Recommends similar movies based on genres and user watch history.
- User Interface: Utilizes Django templates with Bootstrap for a clean and responsive interface.
## Installation and Setup
### Prerequisites
- Python (3.x recommended)
- Django framework
- Bootstrap (included)
### Setup Instructions
1. Clone the Repository

```
git clone https://github.com/your-username/flickpicks.git
cd flickpicks
```
2. Install Dependencies

```
pip install -r requirements.txt
```
3. Database Setup (Make Migrations)

```
python manage.py makemigrations
python manage.py migrate
```
4. Run the Application

```
python manage.py runserver
```
5. Access the Application

Open your web browser and visit http://localhost:8000 to access FlickPicks.

## Author

- **[Azhar Bihari](https://github.com/azhrbhr)**
- **Contact:** azhrbhr@gmail.com



## License

This project is licensed under the [MIT License](LICENSE).

The MIT License is a permissive open-source license that allows users to do anything they want with the project, as long as they provide appropriate attribution and don't hold the author liable.
