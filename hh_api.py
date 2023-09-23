import json
from requests import get


class HHAPI:
    """Класс для работы с Api HeadHunter"""

    hh_url = "https://api.hh.ru/vacancies"

    def __init__(self):
        self.ten_ip_vacancies = [80, 139, 579, 947, 955, 1740, 2180, 3529, 78638, 1122462]

    def __str__(self):
        return "hh.ru"

    @staticmethod
    def printj(data_dict):
        """Выводит словарь в json формате с отступами"""
        print(json.dumps(data_dict, indent=2, ensure_ascii=False))

    def get_vacancies_api(self, **kwargs):
        """
        :param kwargs:
        area - Код региона (1 - Москва)
        text - Поисковый запрос
        employer_id - id компании. Указывать фактические идентификаторы компаний, разделенные запятыми.
        'employer_id':49, 80, 355, 364, 579, 947, 955, 1276, 1378, 1740"
        per_page - Количество вакансий на странице
        """

        params = {}
        for key, value in kwargs.items():
            params[key] = value

        response = get(self.hh_url, params=params)

        if response.status_code == 200:
            data = response.text
            data_dict = json.loads(data)
            return data_dict
        else:
            print("Ошибка при выполнении запроса:", response.status_code)
            return None

    def get_json_files(self):
        """Сохранение файлов 10 компаний."""
        for one_id in self.ten_ip_vacancies:
            with open(f'{one_id}.json', 'w', encoding="utf-8") as file:
                json.dump(self.get_vacancies_api(employer_id=one_id, per_page=100), file, indent=2, ensure_ascii=False)
