print("Программа Мой склад")
import os.path

class Sclad:
    def __init__(self, naimenovanie, ed_iz, cena, colichestvo):
        self.naimenovanie = naimenovanie
        self.ed_iz = ed_iz
        self.cena = cena
        self.colichestvo = colichestvo


def login_user():
    global login
    login = input("Введите вашу почту: ")
    return login

def password_user():
    space = False
    letter_upper = False
    letter_lower = False
    number = False
    symbol = False
    password = input("Введи пароль: ")
    if len(password) >= 8:
        for elem in password:
            if elem.isspace():
                space = True
            if elem.isupper():
                letter_upper = True
            if elem.islower():
                letter_lower = True
            if elem.isdigit():
                number = True
            if not elem.isalnum() and elem.isspace():
                symbol = True
        if not space and letter_lower and letter_upper and number:
            print("Пароль подходит")
            return password
        else:
            print("Пароль не подходит по требованиям")
    else:
        print("Не достаточно символов")

try:
    avtor = input("1. Регистрация, 2. Авторизация, 0. Выход: ")
    t = True
    while t:
        if avtor == "1":
            login_user()
            login_file = open(login + ".txt", "a")
            login_file.write(str(password_user()))
            print(f"Ваш логин {login}, пароль {str(password_user())}")
            login_file.close()
            print("Для дальнейшей работы пройди авторизацию")
            avtor = input("1. Регистрация, 2. Авторизация, 0. Выход: ")

        elif avtor == "2":
            login = input("Введи логин не более 10 символов: ")
            if os.path.isfile(login + ".txt"):
                password = input("Введите пароль: ")
                with open(login + ".txt") as openfile:
                    for line in openfile:
                        for part in line.split():
                            if password in part:
                                print("Авторизация прошла успешно")


####################################################################################################################################################
                                try:
                                    dej = int(input(
                                        "0. Выход\n1. Добавить\n2. Удалить позицию из прихода\n3. Расход\n4. "
                                        "Вывести на экран приход\n5. Вывести на экран расход"))
                                    while dej != 0:
                                        if dej == 1:
                                            prihod_file = open(login+"p.txt", "a")
                                            pozicii = int(input("Количество позиций или 0 для выхода"))
                                            if pozicii != 0:
                                                for i in range(pozicii):
                                                    naimenovanie = input("Наименование:")
                                                    ed_iz = input("Еденица измерения:")
                                                    cena = input("Цена:")
                                                    colichestvo = input("Количество:")
                                                    my_Sclad= Sclad(naimenovanie, ed_iz, cena, colichestvo)
                                                    prihod_file.write(my_Sclad.naimenovanie + ' '+my_Sclad.ed_iz + ' '+my_Sclad.cena + ' '+
                                                                      my_Sclad.colichestvo+'\n')
                                            else:
                                                pass
                                            prihod_file.close()
                                            dej = int(input("0. Выход\n1. Добавить\n2. Удалить позицию из прихода\n3. Расход\n"
                                                            "4. Вывести на экран приход\n5. Вывести на экран расход"))
                                        elif dej == 2:
                                            prihod_file = open(login+"p.txt")
                                            lines = prihod_file.readlines()
                                            print(lines)
                                            prihod_file.close()
                                            prihod_file = open(login+"p.txt", "w")
                                            print("Позиция, которую удаляем")
                                            naimenovanie_user = input("Наименование: ")
                                            ed_iz_user = input("Единица измерения: ")
                                            cena_user = input("Цена: ")
                                            colichestvo_user = input("Количество: ")
                                            for line in lines:
                                                if line != (naimenovanie_user + ' ' + ed_iz_user + ' ' + cena_user + ' ' + colichestvo_user + "\n"):
                                                    prihod_file.write(line)
                                            prihod_file.close()
                                            dej = int(input("0. Выход\n1. Добавить\n2. Удалить позицию из прихода\n3. Расход\n"
                                                      "4. Вывести на экран приход\n5. Вывести на экран расход"))
                                        elif dej == 4:
                                            prihod_file = open(login+"p.txt")
                                            for line in prihod_file:
                                                print(line[:-1])
                                            prihod_file.close()
                                            dej = int(
                                                input("0. Выход\n1. Добавить\n2. Удалить позицию из прихода\n3. Расход\n"
                                                      "4. Вывести на экран приход\n5. Вывести на экран расход"))
    #################################################################################################################################################
                                        elif dej == 3:
                                            rashod = []
                                            rashod_file = open(login+"p.txt")
                                            rashod_file_list = list(rashod_file)
                                            for elem in rashod_file_list:
                                                elem_split = elem.split()
                                            for i in range(len(rashod_file_list)):
                                                rashod.append(
                                                Sclad(elem_split[0], elem_split[1], elem_split[2], elem_split[3]))
                                                rashod_file.close()
                                            ot =[]
                                            otgr = input("Введи количество позиций расхода: ")
                                            for j in range(int(otgr)):
                                                naimenovanie_user = input("Наименование: ")
                                                ot.append(naimenovanie_user)
                                                ed_iz_user = input("Eденица измерения: ")
                                                ot.append(ed_iz_user)
                                                cena_user = input("Цена: ")
                                                ot.append(cena_user)
                                                col_user = input('Количество: ')
                                                for rez in rashod:
                                                    file_otg = open(login+"otg.txt", "a")
                                                    if rez.naimenovanie == naimenovanie_user:
                                                        if rez.ed_iz == ed_iz_user:
                                                            if rez.cena == cena_user:
                                                                if rez.colichestvo < col_user:
                                                                    print('Недостаточное количество')
                                                                else:
                                                                    file_otg.write(naimenovanie_user + " " + ed_iz_user + " " + cena_user + " " + col_user + '\n')
                                                    file_otg.close()
                                            dej = int(input(
                                                "0. Выход\n1. Добавить\n2. Удалить позицию из прихода\n3. Расход\n"
                                                "4. Вывести на экран приход\n5. Вывести на экран расход"))
                                        elif dej == 5:
                                            otgr_file = open(login + "otg.txt")
                                            for line in otgr_file:
                                                print(line[:-1])
                                            otgr_file.close()
                                            dej = int(input(
                                                "0. Выход\n1. Добавить\n2. Удалить позицию из прихода\n3. Расход\n"
                                                "4. Вывести на экран приход\n5. Вывести на экран расход"))
                                        else:
                                            dej = False
                                except ValueError:
                                    print("Не верные данные")
                            else:
                                pass
                avtor = input("1. Регистрация, 2. Авторизация, 0. Выход: ")
            else:
                print("Вам нужно зарегистрироваться")
        elif avtor == "0":
            t = False
        else:
            t = False
            print("Ввели не допустимые данные")
except FileNotFoundError:
    print("Введены недопустимые символы")