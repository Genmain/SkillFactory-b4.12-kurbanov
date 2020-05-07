# импортируем стандартные библиотеки и некоторые функции из них 
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os, platform

# импортируем наши модули
import users, find_athelete

# константа, указывающая способ соединения с базой данных
DB_PATH = "sqlite:///sochi_athletes.sqlite3"
# базовый класс моделей таблиц
Base = declarative_base()

# программа очистки экрана терминала
cls = lambda: os.system('cls') if platform.system().lower()=="windows" else os.system('clear')

# функция соединения с базой данных
def connect_db(DB_PATH):
    """
    Устанавливает соединение к базе данных, создает таблицы, если их еще нет и возвращает объект сессии 
    """
    # создаем соединение к базе данных
    engine = sa.create_engine(DB_PATH)
    # создаем описанные таблицы
    # Base.metadata.create_all(engine)
    # создаем фабрику сессию
    session = sessionmaker(engine)
    # возвращаем сессию
    return session()

# функция выхода из программы. Очистка и простой вывод на экран
def exit_program():
    cls()
    print("До свдидания \U0001F642")

# главная функция
def main():
    session = connect_db(DB_PATH)
    while True:
        cls()    
        mode = input("Выберите режим.\n1 - Ввести пользователя\n2 - Найти атлета\n3 - Вывести всех пользователей\n4 - Выход\n\nВыбор: ")   
        print("-------------------------------------") 
        if mode == "1":
            users.write_user(session)
        if mode == "2":
            find_athelete.find_athlete(session)    
        elif mode=="3" :
            users.print_users_list(session)
        elif mode=="4":
            break
        else:
            cls()
            print("Режим не определен")
        input("\n--Нажмите Enter что бы продолжить--\n")
    exit_program()


if __name__ == "__main__":
    main()