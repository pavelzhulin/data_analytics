import json


class FilmsManager:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.films = []

    def load_db(self) -> None:
        with open(self.db_path, 'r', encoding='utf-8') as file:
            self.films = json.load(file)

    def save_db(self) -> None:
        with open(self.db_path, 'w', encoding='utf-8') as outfile:
            json.dump(self.films, outfile, ensure_ascii=False)

    def add_film(self, title: str, genre: str, seasons: int, rating: float) -> None:
        new_film = {
            'title': title,
            'genre': genre,
            'seasons': seasons,
            'rating': rating
        }
        self.films.append(new_film)

    def __str__(self) -> str:
        text = ''
        for i, film in enumerate(self.films):
            items = ', '.join(f"{key.title()}: {value}" for key, value in film.items())
            text += f"{i + 1}. {items}\n"
        return text

    def delete_film(self, title: str) -> bool:
        for i in range(len(self.films)):
            if self.films[i]['title'] == title:
                del self.films[i]
                return True
        return False

    def find_by_rating(self, rating_min: float, rating_max: float = 10) -> list[dict]:
        films_by_rating = []
        for film in self.films:
            if rating_min <= film['rating'] <= rating_max:
                films_by_rating.append(film)
        return films_by_rating

    def find_by_genre(self, genre: str) -> list[dict]:
        films_by_genre = []
        for film in self.films:
            if film['genre'] == genre:
                films_by_genre.append(film)
        return films_by_genre

    def manage(self):
        while True:
            print('Выберите операцию:\n'
                  '1. Вывод всех фильмов.\n'
                  '2. Добавление фильма.\n'
                  '3. Удаление фильма.\n'
                  '4. Поиск по рейтингу.\n'
                  '5. Поиск по жанру.\n'
                  'Q. Выход из программы.')
            action = input('Ваш выбор: ').strip().lower()
            if action == '1':
                print(self)
            elif action == '2':
                title = input('Введите название фильма: ')
                genre = input('Введите жанр фильма: ')
                try:
                    seasons = int(input('Введите количество сезонов: '))
                    rating = float(input('Введите рейтинг фильма: '))
                except ValueError:
                    print('Количество сезонов и рейтинг должны быть числами!')
                    continue
                if not 1 <= rating <= 10:
                    print('Рейтинг должен быть от 1 до 10 включительно!')
                    continue
                if seasons < 1:
                    print('Количество сезонов должно быть от 1 и более!')
                    continue
                self.add_film(title, genre, seasons, rating)
                print(f'Фильм {title} успешно добавлен!')
            elif action == '3':
                title = input('Введите название фильма для удаления: ')
                if self.delete_film(title):
                    print(f'Фильм {title} успешно удалён!')
                else:
                    print(f'Фильм {title} не найден!')
            elif action == '4':
                try:
                    rating_min = float(input('Введите меньшее значение рейтинга: '))
                    rating_max = float(input('Введите большее значение рейтинга: '))
                except ValueError:
                    print('Значения рейтинга должны быть числом!')
                    continue
                if not 1 <= rating_min <= 10 or not 1 <= rating_max <= 10:
                    print('Меньший и больший рейтинг должен быть от 1 до 10 включительно!')
                    continue
                if rating_min > rating_max:
                    print('Меньший рейтинг должен быть меньше или равен большего!')
                    continue
                films_by_rating = self.find_by_rating(rating_min, rating_max)
                if films_by_rating:
                    for i, film in enumerate(films_by_rating):
                        print(f'{i + 1}. {film["title"]}, {film["rating"]}')
                else:
                    print(f'Фильмов с рейтингом от {rating_min} до {rating_max} не найдено!')
            elif action == '5':
                genre = input('Введите жанр фильма: ')
                films_by_genre = self.find_by_genre(genre)
                if films_by_genre:
                    for i, film in enumerate(films_by_genre):
                        print(f'{i + 1}. {film["title"]}')
                else:
                    print(f'Фильмы с жанром {genre} не найдены!')
            elif action == 'q':
                self.save_db()
                print('Работа завершена!')
                break
            else:
                print('Операция не найдена, повторите попытку!')
