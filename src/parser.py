from abc import ABC, abstractmethod
import requests

class Parser(ABC):
    """Абстрактный класс для загрузки данных с API."""

    @abstractmethod
    def load_vacancies(self):
        """Загрузка списка вакансий."""
        pass

class HH(Parser):
    """Класс для работы с API HeadHunter."""

    def __init__(self, keyword):
        """Инициализация с указанием ключевого слова для поиска вакансий.

        Args:
            keyword (str): Ключевое слово для поиска.
        """
        self._url = 'https://api.hh.ru/vacancies'  # Приватный атрибут URL
        self._headers = {'User-Agent': 'HH-User-Agent'}  # Приватный атрибут headers
        self.params = {'text': keyword, 'page': 0, 'per_page': 100}

    def load_vacancies(self):
        """Загрузка вакансий с использованием API HH.

        Returns:
            list: Список вакансий.
        """
        vacancies = []
        while True:
            response = requests.get(self._url, headers=self._headers, params=self.params)
            page_data = response.json().get('items', [])
            vacancies.extend(page_data)
            if not page_data:
                break
            self.params['page'] += 1
        return vacancies
