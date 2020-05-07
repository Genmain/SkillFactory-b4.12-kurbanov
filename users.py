
# импортируем библиотеку sqlalchemy и некоторые функции из нее 
import sqlalchemy as sa
# from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# базовый класс моделей таблиц
Base = declarative_base()

class User(Base):
    """
    Описывает структуру таблицы user для хранения регистрационных данных пользователей
    """
    # задаем название таблицы
    __tablename__ = 'user'

    # идентификатор пользователя, первичный ключ
    id = sa.Column(sa.INTEGER, primary_key=True, autoincrement=True)
    # имя пользователя
    first_name = sa.Column(sa.Text)
    # фамилия пользователя
    last_name = sa.Column(sa.Text)
    # пол
    gender = sa.Column(sa.Text)
    # адрес электронной почты пользователя
    email = sa.Column(sa.Text)
    # дата рождения
    birthdate = sa.Column(sa.Text)
    # рост
    height = sa.Column(sa.REAL)    
    
    def __str__(self):
        return f"ID = {self.id} Имя: {self.first_name} Фамилия: {self.last_name} ДатаРождения: {self.birthdate} Рост: {self.height}\n"

def write_user(session):
    # запрашиваем данные пользоватлея
    user = request_data()
    # добавляем нового пользователя в сессию
    session.add(user)
    session.commit()
    print("Спасибо, данные сохранены!")


def request_data():
    """
    Запрашивает у пользователя данные и добавляет их в список users
    """
    # выводим приветствие
    print("Привет! Я запишу твои данные!")
    # запрашиваем у пользователя данные
    first_name = input("Введите своё имя: ")
    last_name = input("Введите фамилию: ")
    gender = input("Введите Ваш пол (м/ж): ")
    email = input("Введите адрес Вашей электронной почты: ")
    birthdate = input("Введите дату Вашего рождения (гггг-мм-дд): ")
    height = input("Введите Ваш рост (м, десятичные через '.'): ")
    # создаем нового пользователя
    user = User(
        # id = None,
        first_name = first_name,
        last_name = last_name,
        gender = 'Male' if gender == "м" else 'Female',
        email = email,
        birthdate = birthdate,
        height = height
    )
    # возвращаем созданного пользователя
    return user

def print_users_list(session):
    """
    Выводит на экран всех пользователей
    """
    # проверяем на пустоту список идентификаторов
    query = session.query(User)
    users = [user for user in query.all()]
    for user in users:
        print(user)
    # подсчитываем количество таких записей в таблице с помощью метода .count()
    print(f'Всего: {query.count()} пользователей')