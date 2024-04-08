from datetime import date

from domain import db_session
from domain.film import Film

db_session.global_init("../db/system.db")
session = db_session.create_session()

films = [Film(title="Великий Гэтсби", duration="2ч 23мин", genre_id=1,
              release_date=date(year=2013, month=5, day=16), director="Баз Лурман"),
         Film(title="Аладдин", duration="2ч 8мин", genre_id=1,
              release_date=date(year=2019, month=5, day=23), director="Гай Ричи"),
         Film(title="Форма воды", duration="2ч 3мин", genre_id=1,
              release_date=date(year=2018, month=1, day=18), director="Гильермо дель Торо"),
         Film(title="Игры разума", duration="2ч 20мин", genre_id=2,
              release_date=date(year=2002, month=2, day=27), director="Рон Ховард"),
         Film(title="Вселенная Стивена Хокинга", duration="2ч 4мин", genre_id=2,
              release_date=date(year=2015, month=2, day=26), director="Джеймс Марш"),
         Film(title="Тоня против всех", duration="2ч 1мин", genre_id=2,
              release_date=date(year=2018, month=2, day=1), director="Крейг Гиллеспи"),
         Film(title="Дом, который построил Джек", duration="2ч 35мин", genre_id=3,
              release_date=date(year=2018, month=12, day=6), director="Ларс фон Триер"),
         Film(title="Паразиты", duration="2ч 12мин", genre_id=3,
              release_date=date(year=2019, month=7, day=4), director="Пон Чжун Хо"),
         Film(title="Сплит", duration="1ч 57мин", genre_id=3,
              release_date=date(year=2017, month=3, day=16), director="М. Найт Шьямалан"),
         ]
session.add_all(films)
session.commit()
