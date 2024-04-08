from services.personal_area_service import PersonalAreaService


class PersonalAreaResource:  # контроллер для работы с функционалом получения данных личного кабинета
    personal_area_service = PersonalAreaService()

    def get_user_tickets(self):  # получить все билеты пользователя
        return self.personal_area_service.get_user_tickets()
