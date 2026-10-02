movies = {}

def add_movie(name, rating):
    movies[name] = rating

def show_movies():
    for name, rating in sorted(movies.items(), key=lambda x: x[1], reverse=True):
        print(f"{name}: {rating}/10")

add_movie("Interstellar", 9)
add_movie("Inception", 8.8)
add_movie("The Martian", 8.5)

show_movies()
