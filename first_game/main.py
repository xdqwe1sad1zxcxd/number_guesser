from time import sleep
from random import randint


def main_number_guesser():
    while True:
        print('Добро пожаловать в числовую угадайку!')
        sleep(1)
        print('Вы попали в игру, в которой будет загадано случайное число, которое вы должны будете отгадать за наименьшее количество попыток!')
        sleep(1)
        print('Введите число с которого будет начинаться числовая угадайка: ', end='')

        def isvalidfirstdig():  # проверка начального числа
            while True:
                dig1 = input()
                if dig1.isdigit() is True:
                    return int(dig1)
                else:
                    print('Введите корректное число!')

        num1 = isvalidfirstdig()

        print('Введите число которым будет заканчиваться числовая угадайка: ', end='')

        def isvalidseconddig():  # проверка границы угадайки
            while True:
                dig2 = input()
                if dig2.isdigit() is True:
                    if int(dig2) > num1:
                        return int(dig2)
                    elif num1 > int(dig2):
                        print('Граница числовой угадайки должна быть больше начального числа!')
                else:
                    print('Введите корректное число!')

        num2 = isvalidseconddig()

        num = randint(num1, num2)  # загаданное число

        print(f'Введите число в диапазоне от {num1} до {num2}!')

        def isvalidinput():
            while True:
                dig = input()
                if dig.isdigit() is True:
                    dig = int(dig)
                    if num1 <= dig <= num2:
                        return dig
                    else:
                        print(f'Введите число в диапазоне от {num1} до {num2}!')
                else:
                    print(f'Введите корректное число в диапазоне от {num1} до {num2}!')

        def number_guesser():
            counter = 1
            while True:
                number = isvalidinput()
                if num < number:
                    print('Загаданное число меньше вашего! Попробуйте ещё раз')
                    counter += 1
                elif num > number:
                    print('Загаданное число больше вашего! Попробуйте ещё раз')
                    counter += 1
                else:
                    print(f'Поздравляю, вы угадали число! Кол-во попыток: {counter}')
                    break

        number_guesser()
        while True:
            print("Хотите сыграть ещё раз? Введите 'yes' если да, в противном случае - no': ", end='')
            answer = input()
            if answer.lower() == 'no':
                print('Спасибо за игру!')
                return
            elif answer.lower() == 'yes':
                break
            else:
                print('Введите yes или no!')

def main():
    main_number_guesser()


if __name__ == '__main__':
    main()
