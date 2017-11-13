import fresh_tomatoes
import media

"""Defining an array of Movie instances with Movie Title, poster_image_url, trailer_youtube_url"""

Trainspotting = media.Movie("Trainspotting", "https://upload.wikimedia.org/wikipedia/en/7/71/Trainspotting_ver2.jpg",
                        "https://www.youtube.com/watch?v=8LuxOYIpu-I")

Bronx_Tale = media.Movie("Bronx Tale", "https://upload.wikimedia.org/wikipedia/en/3/3e/A_Bronx_Tale.jpg",
                        "https://www.youtube.com/watch?v=q5nQyoo1LwY")

Social_Network = media.Movie("Social Network","https://upload.wikimedia.org/wikipedia/en/7/7a/Social_network_film_poster.jpg",
                        "https://www.youtube.com/watch?v=lB95KLmpLR4")

Old_School = media.Movie("Old School","https://upload.wikimedia.org/wikipedia/en/2/21/Old_s_poster.jpg",
                        "https://www.youtube.com/watch?v=VqtymOtKr48")

Step_Brothers = media.Movie("Step Brothers","https://upload.wikimedia.org/wikipedia/en/d/d9/StepbrothersMP08.jpg",
                        "https://www.youtube.com/watch?v=CewglxElBK0")

Trainspotting_T2 = media.Movie("Trainspotting T2","https://upload.wikimedia.org/wikipedia/en/1/1c/T2_%E2%80%93_Trainspotting_poster.jpg",
                        "https://www.youtube.com/watch?v=EsozpEE543w")

movies = [Trainspotting, Bronx_Tale, Social_Network, Old_School, Step_Brothers, Trainspotting_T2]

"""Passing movies array to open_movies_page() function of freshtomatoes.py"""
fresh_tomatoes.open_movies_page(movies)


