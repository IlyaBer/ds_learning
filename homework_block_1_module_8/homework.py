import numpy as np

def random_predict(number:int=1) -> int:
    
    """Угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    
    Математический метод поиска:
        Метод деления числового отрезка пополам
    """
    count = 0             # счетчик попыток
    divider = 25          # изначальное значение делителя отрезка 
    predict_number = 50   # т.к. нам известен диапазон чисел, из которого будет загадано искомое число, начинаем поиск с середины отрезка
    
    while divider != 0:   # поиск делением отрезка осуществляется до тех пор, пока делитель не будет равен 0. Дальнейшее разделение отрезка бессмысленно
        count += 1
        if number > predict_number:
            predict_number = predict_number + divider   # сокращаем область поиска
        elif number < predict_number:
            predict_number = predict_number - divider   # сокращаем область поиска
        elif number == predict_number:
            break
        divider = divider // 2  # уменьшаем абсолютное значение делителя, т.к. область поиска сократилась вдвое

    while number != predict_number:     # если число не было угадано ранее, будем перебирать ближайшие числа по 1.
        count += 1
        if number > predict_number:
            predict_number += 1
        else:
            predict_number -= 1

    return(count)


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN 
if __name__ == '__main__':
    score_game(random_predict)