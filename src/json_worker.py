import json
import os.path
from abc import ABC, abstractmethod


class FileWork(ABC):
    """Абстрактный класс для работы с файлами."""

    def __init__(self):
        pass

    @abstractmethod
    def read_file(self):
        """Чтение данных из файла."""
        pass

    @abstractmethod
    def save_file(self, data):
        """Сохранение данных в файл."""
        pass

    @abstractmethod
    def delete_file(self):
        """Удаление файла."""
        pass


class WorkWithJson(FileWork):
    """Класс для работы с JSON-файлами."""

    def __init__(self, file_name="data/vacancies.json"):
        """Инициализация с возможностью указать имя файла.

        Args:
            file_name (str): Имя файла для работы с данными.
        """
        self._file_name = file_name  # Приватный атрибут для хранения пути к файлу
        self._abs_path = os.path.abspath(self._file_name)

    def read_file(self):
        """Чтение данных из JSON-файла.

        Returns:
            list: Список данных из файла.
        """
        if os.path.exists(self._abs_path):
            with open(self._abs_path, "r", encoding="utf-8") as file:
                return json.load(file)
        return []

    def save_file(self, data):
        """Добавление данных в JSON-файл.

        Args:
            data (dict): Данные для добавления.
        """
        current_data = self.read_file()
        current_data.append(data)
        with open(self._abs_path, "w", encoding="utf-8") as file:
            json.dump(current_data, file, ensure_ascii=False, indent=4)

    def delete_file(self):
        """Удаление JSON-файла, если он существует."""
        if os.path.exists(self._abs_path):
            os.remove(self._abs_path)
