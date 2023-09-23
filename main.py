import os

import psycopg2

from config import config
from db_manager import DBManager
from hh_api import HHAPI

params = config()

if __name__ == "__main__":
    db_manager = DBManager('hh', **params)
    db_manager.create_tables()
    hh = HHAPI()
    hh.get_json_files()

    i = 1

    for file in os.listdir(os.getcwd()):
        if file.endswith('json'):
            db_manager.insert_vacancies(file)
            i += 1

    print(db_manager.get_companies_and_vacancies_count())
    print(db_manager.get_all_vacancies())
    print(round(db_manager.get_avg_salary(), 2), 'руб. Средняя зарплата')
    for row in db_manager.get_vacancies_with_higher_salary():
        print(row)
    print(db_manager.get_vacancies_with_keyword("python"))

    db_manager.close_conn()