import json

import pytest

from src.films.films_manager import FilmsManager

db_content = [
    {"title": "Chronicles of the Galaxy", "genre": "Adventure", "seasons": 5, "rating": 8.0},
    {"title": "Mystery Island", "genre": "Fantasy", "seasons": 3, "rating": 9.0},
    {"title": "Epic Quest", "genre": "Fantasy", "seasons": 4, "rating": 7.0},
    {"title": "Crime Files", "genre": "Crime Drama", "seasons": 6, "rating": 5.0},
    {"title": "Medical Miracles", "genre": "Medical Drama", "seasons": 2, "rating": 8.0},
    {"title": "Time Travelers", "genre": "Adventure", "seasons": 4, "rating": 8.0},
    {"title": "Comedy Central", "genre": "Comedy", "seasons": 7, "rating": 9.0},
    {"title": "Fallout", "genre": "Action", "seasons": 1, "rating": 8.5}
]


@pytest.fixture
def temp_db_path(tmp_path):
    # db_file = f'{tmp_path}/tv_shows_db.json'
    db_file = tmp_path / "films_db.json"
    with open(db_file, 'w', encoding='UTF-8') as f:
        json.dump(db_content, f)
    return str(db_file)


@pytest.fixture
def manager_with_db(temp_db_path):
    manager = FilmsManager(temp_db_path)
    manager.load_db()
    return manager


def test_load_db(manager_with_db):
    assert len(db_content) == len(manager_with_db.films)
    matching_films = 0
    for film in db_content:
        if film in manager_with_db.films:
            matching_films += 1
    assert matching_films == len(db_content)


def test_add_film(manager_with_db):
    film = {"title": "Flash", "genre": "Action", "seasons": 9, "rating": 7.5}
    films_count_before = len(manager_with_db.films)
    manager_with_db.add_film(**film)
    assert len(manager_with_db.films) == films_count_before + 1
    assert film in manager_with_db.films


def test_delete_film(manager_with_db):
    title = "Comedy Central"
    films_count_before = len(manager_with_db.films)
    manager_with_db.delete_film(title)
    assert len(manager_with_db.films) == films_count_before - 1
    is_matching = False
    for film in manager_with_db.films:
        if film['title'] == title:
            is_matching = True
            break
    assert not is_matching


def test_find_by_rating(manager_with_db):
    rating_min = 8
    rating_max = 10
    matching_films_count = 6
    films_by_rating = manager_with_db.find_by_rating(rating_min, rating_max)
    assert matching_films_count == len(films_by_rating)
    matching_films_rating = 0
    for film in films_by_rating:
        if rating_min <= film['rating'] <= rating_max:
            matching_films_rating += 1
    assert matching_films_rating == matching_films_count


def test_find_by_genre(manager_with_db):
    genre = "Adventure"
    matching_films_count = 2
    films_by_genre = manager_with_db.find_by_genre(genre)
    assert matching_films_count == len(films_by_genre)
    matching_films_genre = 0
    for film in films_by_genre:
        if film['genre'] == genre:
            matching_films_genre += 1
    assert matching_films_genre == matching_films_count


def test_save_db(manager_with_db):
    film_to_adding = {"title": "Flash", "genre": "Action", "seasons": 9, "rating": 7.5}
    films_count_before_adding = len(manager_with_db.films)
    manager_with_db.add_film(**film_to_adding)
    manager_with_db.save_db()
    manager_with_db.load_db()
    assert films_count_before_adding == len(manager_with_db.films) - 1
    assert film_to_adding in manager_with_db.films
