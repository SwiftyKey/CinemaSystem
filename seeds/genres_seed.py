from domain import db_session
from domain.genre import Genre

db_session.global_init("../db/system.db")
session = db_session.create_session()

genres = {"Роман": Genre(title='Роман'), "Биографический": Genre(title='Биографический'),
          "Триллер": Genre(title='Триллер'), "Боевик": Genre(title='Боевик'),
          "Вестерн": Genre(title='Вестерн'), "Военный": Genre(title='Военный'),
          "Детектив": Genre(title='Детектив'), "Документальный": Genre(title='Документальный'),
          "Фантастика": Genre(title='Фантастика'), "Драма": Genre(title='Драма'),
          "Исторический": Genre(title='Исторический'), "Комедия": Genre(title='Комедия'),
          "Криминал": Genre(title='Криминал'), "Мелодрама": Genre(title='Мелодрама'),
          "Мистика": Genre(title='Мистика'), "Мюзикл": Genre(title='Мюзикл'),
          "Начный": Genre(title='Начный'), "Нуар": Genre(title='Нуар'),
          "Приключения": Genre(title='Приключения'), "Артхаус": Genre(title='Артхаус'),
          "Семейный": Genre(title='Семейный'), "Спорт": Genre(title='Спорт'),
          "Ужасы": Genre(title='Ужасы'), "Фэнтези": Genre(title='Фэнтези'),
          "Эротика": Genre(title='Эротика')}
session.add_all(genres.values())
session.commit()
