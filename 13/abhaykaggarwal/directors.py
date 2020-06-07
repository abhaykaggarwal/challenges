import csv
from collections import defaultdict, namedtuple, OrderedDict
from statistics import mean
import operator

MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director(data= MOVIE_DATA):
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''
    directors = defaultdict(list)
    with open(data, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue

            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)

    return directors


def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate average score'''
    reduced_directors = {k: v for k, v in directors.items() if len(v) >= MIN_MOVIES}
    new_dict = {}
    for director_n in reduced_directors:
        movies_list = reduced_directors[director_n]
        mean_score = _calc_mean(movies_list)
        new_dict[director_n] = mean_score

    new_dict = sorted(new_dict.items(), key=operator.itemgetter(1), reverse=True)

    return new_dict

def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    ratings_list = []
    for mov_tuple in movies:
        ratings_list.append(mov_tuple.score)

    ratings_mean = mean(ratings_list)
    return round(ratings_mean,1)

def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    fmt_director_entry = '{counter}. {director:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60

    score_dict = get_average_scores(directors)
    score_list_unsorted = list(score_dict)
    score_list = sorted(score_list_unsorted, key=lambda tup: tup[1], reverse=True)

    for i in range(NUM_TOP_DIRECTORS):

        dir_name = score_list[i][0]
        dir_score = score_list[i][1]

        print(fmt_director_entry.format(counter=i+1, director=dir_name, avg=dir_score))
        print(sep_line)

        tuple_list = sorted(directors[dir_name], key=operator.attrgetter('score'), reverse=True)

        for mov in tuple_list:
            print(fmt_movie_entry.format(year=mov.year, title=mov.title, score=mov.score))

        print("\n")


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    print_results(directors)


if __name__ == '__main__':
    main()
