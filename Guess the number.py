#Угадайка чисел
#Описание проекта: программа генерирует случайное число в диапазоне от 1 до указанного числа и просит пользователя угадать это число. 
#Если догадка больше случайного числа, то программа должна вывести сообщение 'Слишком много, попробуйте еще раз'. 
#Если догадка меньше случайного числа, то программа должна вывести сообщение 'Слишком мало, попробуйте еще раз'. 
#Если число угадано, то программа должна поздравить его и вывести сообщение 'Вы угадали, поздравляем!'.
#Проект выводит количество попыток и предлагает провести новую игру


import random
def game():
    print('Добро пожаловать в числовую угадайку.')
    print('Введите максимальное число:')
    num = int(input())
    num_r = random.randint(1, num)
    print('Загадано случайное число от 1 до', num, 'Попробуй угадать!')
    print('Ваше число:')
    num_game = int(input())
    count = 1

    if num_game > num:
        print('Неверное число, попробуй еще:')
        num_game = int(input())

    while num_game != num_r:
        if num_game > num_r:
            print('Слишком много, попробуйте еще раз')
            print('Ваше число:')
            num_game = int(input())
            count += 1
            continue
        elif num_game < num_r:
            print('Слишком мало, попробуйте еще раз')
            print('Ваше число:')
            num_game = int(input())
            count += 1
            continue
    print('Вы угадали, поздравляем!', 'Число угадано с', count, 'попытки/ток')


gaming = game()
print('Спасибо, что играли в числовую угадайку. Еще увидимся...', 'Или сыграем еще?', 'Yes or No ?', sep='\n')
answer = input()
answer = answer.lower()
if answer == 'yes':
    gaming = game()
print('Спасибо, что играли в числовую угадайку.')