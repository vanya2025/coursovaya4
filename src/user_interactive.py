from src.parser import HH

class UserInteractive:
    """Класс для взаимодействия с пользователем."""

    def __init__(self, user_name):
        """Инициализация пользователя.

        Args:
            user_name (str): Имя пользователя.
        """
        self.user_name = user_name
        self.vacancies_list = []

    @staticmethod
    def get_vacancies_list(keyword):
        """Получение списка вакансий по ключевому слову.

        Args:
            keyword (str): Ключевое слово для поиска вакансий.

        Returns:
            list: Список вакансий.
        """
        hh = HH(keyword)
        return hh.load_vacancies()

    def get_top_n_for_salary(self):
        """Получение топ N вакансий с наивысшей зарплатой.

        Returns:
            list: Отсортированный список вакансий.
        """
        n = int(input("Введите Top N: "))
        sort_by_salary = sorted(self.vacancies_list, key=lambda x: x.salary, reverse=True)
        return sort_by_salary[:n]
