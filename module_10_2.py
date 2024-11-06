# Домашнее задание по теме "Потоки на классах"

import threading
import time

class Knight(threading.Thread):  # Наследуем класс Knight от threading.Thread
    def __init__(self, name, power):
        super().__init__()
        self.name = name  # Инициализация атрибута имени рыцаря
        self.power = power  # Инициализация атрибута силы рыцаря
        self.days_fought = 0  # Количество дней, проведенных в сражении
        self.enemies = 100 # Начальное количество врагов

    def run(self):

        print(f"{self.name}, на нас напали!")

        while self.enemies > 0:  # Пока остаются враги, продолжаем сражение
            if self.enemies < self.power:  # Если оставшееся количество врагов меньше силы рыцаря
                self.enemies -= self.power  # Уменьшаем количество врагов на силу рыцаря
                break  # Прекращаем цикл, так как все враги повержены
            else:
                self.enemies -= self.power  # Уменьшаем количество врагов на силу рыцаря

            self.days_fought += 1  # Увеличиваем счетчик дней, проведенных в сражении
            time.sleep(1)  # Задержка на 1 секунду, имитирующая день сражения
            print(f"{self.name} сражается {self.days_fought} день...., осталось {self.enemies} воинов")

        print(f"{self.name} одержал победу спустя {self.days_fought} дней!")  # Сообщение о победе


if __name__ == "__main__":
    # enemies_left = 100  # Общее количество врагов

    first_knight = Knight('Sir Lancelot', 10)  # Создание первого рыцаря
    second_knight = Knight("Sir Galahad", 20)  # Создание второго рыцаря

    first_knight.start()  # Запуск первого потока
    second_knight.start()  # Запуск второго потока

    first_knight.join()  # Ожидание завершения первого потока
    second_knight.join()  # Ожидание завершения второго потока

    print("Все битвы закончились!")  # Сообщение об окончании битвы