"""Игра "Угадай число".
Компьютер самостоятельно загадывает и отгадывает число.
"""

import numpy as np

def random_predict(number: int = np.random.randint(1, 101)) -> int:
    """Рандомно угадываем число
    Args:
        number (int, optional): Загаданное число. Defaults to 1.
    Returns:
        int: Число попыток
    """

    count = 0
    max_number = 100
    min_number = 0
    predict_number = np.random.randint(1, 101)  # предполагаемое число

    while True:
        count += 1

        if predict_number > number:
            max_number = predict_number - 1
            predict_number = (max_number + min_number) // 2

        elif predict_number < number:
            min_number = predict_number + 1
            predict_number = (max_number + min_number) // 2

        else:
            break  # выход из цикла, если угадали
        
    return count

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 100 подходов угадывает наш алгоритм
    Args:
        random_predict ([type]): функция угадывания
    Returns:
        int: среднее количество попыток
    """

    count_ls = []  # список для сохранения количества попыток
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(250))  # загадали список чисел

    i=0
    for number in random_array:
        i+=1
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))  # Находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return (score)

score_game(random_predict)
