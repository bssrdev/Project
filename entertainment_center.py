import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()

pele = media.Movie("Pele",
                     "Birth of a Legend",
                     "https://en.wikipedia.org/wiki/File:Pel%C3%A9_(film_poster).jpg",
                     "https://www.youtube.com/watch?v=pwBXs2B2ZbI")
#print(pele.storyline)
#pele.show_trailer()

movies = [toy_story, avatar, pele]
fresh_tomatoes.open_movies_page(movies)
