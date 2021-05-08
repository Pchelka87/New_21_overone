import time
print("Добро пожаловать в магазин '123'")
tovar1 = "1. АУДИ"
tovar2 = "2. МЕРСЕДЕС"
tovar3 = "3. Вольво"
cena1 = 10000
cena2 = 22000
cena3 = 30000
print(f"У нас в продаже имеются\n{tovar1} - {cena1} руб.\n{tovar2} - {cena2} руб.\n{tovar3} - {cena3} руб.")
consultant = input("Здравствуйте, я - бот, если вам нужна моя помощь нажмите 1, иначе - 0: ")
chek = 0
reclama = "7788 Позвони и мы подбросим"
if consultant == "1":
    budjet = int(input('Какой у Вас бюджет: '))
    if budjet > 10000 and  budjet <= 30000:
        scorost = input("Вам нужен спортивный автомобиль: 1. Да, 2. Нет: ")
        if scorost == "1":
            print("Вам подойдет товар 1. Вольво")
        else:
            print("Вам подойдет товар 2. Мерседес")
    elif budjet == 10000 :
        print("Вам подойдет товар 1. Ауди")
    elif budjet < 10000:
        print("Мы не сможем Вам помочь")
    elif budjet > 30000:
        print("Вы можете выбрать любой автомобиль в бюджетной комплектации, иначе стоимость будет зависеть от идивидуальных потребностей")
    else:
        print("К сожалению не могу Вам помочь")
zapros = input("Если желаете сделать заказ введите 1, для выхода введите 0: ")
t = True
while t:
    if zapros == "1":
        n1 = int(input("Выбери товар или если завершили заказ нажмите 0: "))
        if n1 == 1 or n1 == 2 or n1 == 3:
            pogel =input("Выберите комплектацию: 1. Бюджет, 2. Премиум: ")
            if pogel == "1":
                pogel1 = input("Выберите цвет, если золотой - 1, другой - 2: ")
                if pogel1 == "2":
                    if n1 == 1:
                        col = int(input("Введи количество: "))
                        res = col * cena1
                        print(f"Товар {tovar1} на сумму {res} руб.")
                        chek += res
                    elif n1 == 2:
                        col = int(input("Введи количество: "))
                        res = col * cena2
                        print(f"Товар {tovar2} на сумму {res} руб.")
                        chek += res
                    else:
                        col = int(input("Введи количество: "))
                        res = col * cena3
                        print(f"Товар {tovar3} на сумму {res} руб.")
                        chek += res
                    print("Проверяю наличие на складе...")
                    time.sleep(1)
                    print("Передаю заказ менеджеру...")
                    time.sleep(1)
                    print("Заказ подтвержден")
                    print(reclama)
                else:
                    if n1 == 1:
                        col = int(input("Введи количество: "))
                        res = col * cena1*1.2
                        print(f"Товар {tovar1} на сумму {res} руб.")
                        chek += res
                    elif n1 == 2:
                        col = int(input("Введи количество: "))
                        res = col * cena2*1.2
                        print(f"Товар {tovar2} на сумму {res} руб.")
                        chek += res
                    else:
                        col = int(input("Введи количество: "))
                        res = col * cena3*1.2
                        print(f"Товар {tovar3} на сумму {res} руб.")
                        chek += res
                    print("Проверяю наличие на складе...")
                    time.sleep(1)
                    print("Передаю заказ менеджеру...")
                    time.sleep(1)
                    print("Заказ подтвержден")
            elif pogel == "2":
                pogel1 = input("Выберите цвет, если золотой - 1, другой - 2: ")
                if pogel1 == "2":
                    if n1 == 1:
                        col = int(input("Введи количество: "))
                        res = col * cena1*1.1
                        print(f"Товар {tovar1} на сумму {res} руб.")
                        chek += res
                    elif n1 == 2:
                        col = int(input("Введи количество: "))
                        res = col * cena2*1.1
                        print(f"Товар {tovar2} на сумму {res} руб.")
                        chek += res
                    else:
                        col = int(input("Введи количество: "))
                        res = col * cena3*1.1
                        print(f"Товар {tovar3} на сумму {res} руб.")
                        chek += res
                    print("Проверяю наличие на складе...")
                    time.sleep(1)
                    print("Передаю заказ менеджеру...")
                    time.sleep(1)
                    print("Заказ подтвержден")
                else:
                    if n1 == 1:
                        col = int(input("Введи количество: "))
                        res = col * cena1 * 1.5
                        print(f"Товар {tovar1} на сумму {res} руб.")
                        chek += res
                    elif n1 == 2:
                        col = int(input("Введи количество: "))
                        res = col * cena2 * 1.5
                        print(f"Товар {tovar2} на сумму {res} руб.")
                        chek += res
                    else:
                        col = int(input("Введи количество: "))
                        res = col * cena3 * 1.5
                        print(f"Товар {tovar3} на сумму {res} руб.")
                        chek += res
                    print("Проверяю наличие на складе...")
                    time.sleep(1)
                    print("Передаю заказ менеджеру...")
                    time.sleep(1)
                    print("Заказ подтвержден")
            else:
                t = False
        else:
            t = False
            print(f"Итоговая сумма чека {chek}")
    else:
        print("Спасибо, что посетили нас")
        t = False
f.write