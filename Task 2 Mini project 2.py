#!/usr/bin/env python
# coding: utf-8

# In[4]:


movies = [
    ['enternal sunshine of the spotless mind',20000000],
    ['Memento',9000000],
    ['Requiem for a dream',4500000],
    ['Pirates of the caribbean: on stranger tides',379000000],
    ['Avengers: Age of the ultron',365000000],
    ['Avengers: Endgame',365000000],
    ['Incredible 2',200000000]
]

def average_budget(movie_list):
    total_budget = 0
    for movie in movie_list:
        total_budget +=movie[1]
    avg_budget = total_budget / len(movie_list)
    return avg_budget
def high_budget_movie(movie_list,av_budget):
    high_budget_movie = []
    for movie in movie_list:
        if movie[1] > av_budget:
            high_budget_movie.append([movie[0],movie[1],movie[1]-av_budget])
    return high_budget_movie
def add_movies(movie_list):
    number_movies = int(input("How many movies you want to add"))
    for i in range(number_movies):
        name = input('Enter the movie names')
        budget = int(input(f'Enter the budget for {name}'))
        movie_list.append([name,budget])
        
add_movies(movies)

Average_budget = average_budget(movies)
print(f'\nThe Average budget is :{Average_budget}')
high_budget_movie = high_budget_movie(movies,Average_budget)
print('\nMovies with a budget higher than a average')
for movie in high_budget_movie:
    print(f'{movie[0]} had a budget {movie[2]} higher than a average')
    
print(f'\nNumber of a movies with a higher than a average budget:{len(high_budget_movie)}')


# In[ ]:




