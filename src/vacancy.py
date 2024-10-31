class Vacancy:
    """Класс для представления вакансии."""

    def __init__(self, name, area, salary: int, url=None, snippet=None):
        """Инициализация вакансии.

        Args:
            name (str): Название вакансии.
            area (str): Город.
            salary (int): Зарплата.
            url (str): URL вакансии.
            snippet (str): Краткое описание.
        """
        self.name = self.__validation_data(name)
        self.area = self.__validation_data(area)
        self.salary = salary
        self.url = url or "URL не указан"
        self.snippet = snippet or "Описание отсутствует"

    def __str__(self):
        """Возвращает строковое представление вакансии."""
        return (f"{self.name}\n"
                f"Город: {self.area}\n"
                f"Зарплата: {self.salary if self.salary else 'Зарплата не указана'}\n"
                f"URL: {self.url}\n"
                f"Описание: {self.snippet}")

    def __lt__(self, other):
        """Сравнение вакансий по зарплате."""
        if not self.salary:
            return False
        elif not other.salary:
            return True
        return self.salary < other.salary

    @staticmethod
    def __validation_data(data):
        """Проверка данных и замена на значение по умолчанию, если пусто.

        Args:
            data (str): Данные для проверки.

        Returns:
            str: Проверенные данные или значение по умолчанию.
        """
        return data if data else "Отсутствует"

    @classmethod
    def new_vacancy(cls, vacancy):
        """Создание новой вакансии из словаря.

        Args:
            vacancy (dict): Данные вакансии.

        Returns:
            Vacancy: Экземпляр класса Vacancy.
        """
        name = vacancy.get("name")
        area = vacancy.get("area", {}).get("name")
        salary = vacancy.get("salary", {}).get("from", 0)
        url = vacancy.get("alternate_url")
        snippet = vacancy.get("snippet", {}).get("requirement", "Описание отсутствует")
        return cls(name, area, salary, url, snippet)
