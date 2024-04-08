from services.book_service import BookService


class BookResource:  # контроллер для работы с функционалом бронирования билетов
    book_service = BookService()

    def book(self, ticket_id: int):  # бронирование
        self.book_service.book(ticket_id)
