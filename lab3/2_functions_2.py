movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

def highly_rated(movie):
    return movie["imdb"] > 5.5

def sublist_highly_rated(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]

def category(movies, category):
    return [movie for movie in movies if movie["category"].lower() == category.lower()]

def average_imdb_score(movies):
    return sum(movie["imdb"] for movie in movies) / len(movies)

def average_imdb_score_by_category(movies, category):

    category_movies = category(movies, category)
    return average_imdb_score(category_movies)


print(highly_rated(movies[0]))
print(sublist_highly_rated(movies))  
print(category(movies, "Romance"))
print(average_imdb_score(movies)) 
print(average_imdb_score_by_category(movies, "Romance")) 
