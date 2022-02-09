from datetime import date
from application.salary import calculate_salary
from application.db.people import get_employees


def date_now():
    print(date.today())


if __name__ == '__main__':
    date_now()
    calculate_salary()
    get_employees()
