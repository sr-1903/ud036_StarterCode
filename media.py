import webbrowser


class Movie():
    """Simple Movie Class
    Attributes:
        Movie_title: String containing Movie Title
        poster_image_url: String containing url to movie poster image
        trailer_youtube_url: String containing url to movie trailer in You Tube
    """
    def __init__(self, movie_title, poster_image_url, trailer_youtube_url):
        """Inits Movie Class with title, poster_url and trailer_url"""
        self.title = movie_title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """Opens web browser at trailer url to display the movie trailer"""
        webbrowser.open(self.trailer)
