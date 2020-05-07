# импортируем библиотеку sqlalchemy и некоторые функции из нее 
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# для сравнения с пользователем импортируем модель пользователя
from users import User

# константа, указывающая способ соединения с базой данных
DB_PATH = "sqlite:///users.sqlite3"
# базовый класс моделей таблиц
Base = declarative_base()

class Athlete(Base):
    """
    Описывает структуру таблицы user для хранения регистрационных данных пользователей
    """
    # задаем название таблицы
    __tablename__ = 'athelete'

    id = sa.Column(sa.String(36), primary_key=True)
    age = sa.Column(sa.Integer)
    birthdate = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    height = sa.Column(sa.REAL)
    name = sa.Column(sa.Text)
    weight = sa.Column(sa.Integer)
    gold_medals = sa.Column(sa.Integer)
    silver_medals = sa.Column(sa.Integer)
    bronze_medals = sa.Column(sa.Integer)
    total_medals = sa.Column(sa.Integer)
    sport = sa.Column(sa.Text)
    country = sa.Column(sa.Text)
    
def find_athlete(session):

    id = input("\nВведите ID пользователя: ")
    query_user = session.query(User).filter(User.id == id).first()
    if query_user == None:
        print("Пользователя с таким ID не существует")
        return
    query_athletes = session.query(Athlete)
    print(query_user)
    athletes = [athlete for athlete in query_athletes.all()]
    # переменные для проверки даты рождения
    birth_diff = 9999999
    tmp_diff = 0
    # переменные для проверки роста
    height_diff = 1000
    tmp_height = 0
    
    # поиск атлетов в один проход
    for athlete in athletes:
        if athlete.height != None:
            tmp_heigh = abs(athlete.height - query_user.height)  
            if  tmp_heigh < height_diff:
                height_diff = tmp_heigh
                res_athlete_height = athlete
                
        if athlete.birthdate != None:
            tmp_diff = abs((datetime.strptime(athlete.birthdate, '%Y-%m-%d')-datetime.strptime(query_user.birthdate, "%Y-%m-%d")).days)
            if (tmp_diff < birth_diff):
                res_athlete_birth = athlete
                birth_diff = tmp_diff

    print(f"Атлет {res_athlete_height.name} имеет рост {res_athlete_height.height} см")
    print(f"Атлет {res_athlete_birth.name} родился {res_athlete_birth.birthdate} ")

