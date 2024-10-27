class Vacancy:
    def __init__(self, name, area, salary: int):  # , url, snippet):
        self.name = self.__validation_data(name)
        self.area = self.__validation_data(area)
        self.salary = salary
        """self.url = url
        self.snippet = snippet"""

    def __str__(self):
        return (f"{self.name}\n"
                f"Город: {self.area}\n"
                f"Зарплата: {self.salary if self.salary else "Зарплата не указана"}")

    def __lt__(self, other):
        if not self.salary:
            return "Зарплата не указана"
        elif not other.salary:
            return "hi"
        elif self.salary < other.salary:
            return True
        else:
            return False
        # if not self.salary["from"]:
        #     return "Зарплата не указана"
        # if not self.salary:
        #     return "Зарплата не указана"
        # if not other.salary["from"]:
        #     return "hi"
        # if not other.salary:
        #     return "hi"
        # if self.salary < other.salary:
        #     return True
        # else:
        #     return False

    @staticmethod
    def __validation_data(data):
        if data:
            return data
        else:
            return "Отсутствует"

    @classmethod
    def new_vacancy(cls, vacancy):
        name = vacancy.get("name")
        area = vacancy.get("area").get("name")
        if vacancy.get("salary"):
            if vacancy.get("salary").get("from"):
                salary = int(vacancy.get("salary").get("from"))
            else:
                salary = 0
        else:
            salary = "Не указана"
        return cls(name, area, salary)